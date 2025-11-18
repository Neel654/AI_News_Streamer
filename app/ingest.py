import asyncio
import httpx
import feedparser
from datetime import datetime, timezone
from urllib.parse import urlparse

from .config import FEEDS, POLL_INTERVAL
from .store import MemoryStore
from .summarize import summarize_text, sentiment_score
from .models import NewsItem

UA = "AI-News-Streamer/0.1 (+https://localhost)"
TIMEOUT = httpx.Timeout(10.0, connect=5.0)

def _domain(url: str) -> str:
    try:
        return urlparse(url).netloc or "unknown"
    except Exception:
        return "unknown"

async def _fetch(client: httpx.AsyncClient, url: str) -> str | None:
    try:
        r = await client.get(url, headers={"User-Agent": UA})
        r.raise_for_status()
        return r.text
    except Exception as ex:
        print(f"[ingest] fetch error for {url}: {ex}")
        return None

async def poll_feeds(store: MemoryStore, out_queue: asyncio.Queue):
    async with httpx.AsyncClient(timeout=TIMEOUT, follow_redirects=True) as client:
        while True:
            try:
                for feed_url in FEEDS:
                    text = await _fetch(client, feed_url)
                    if not text:
                        continue
                    parsed = feedparser.parse(text)
                    source = parsed.feed.get("title") or _domain(feed_url)

                    # If feed is empty, log once
                    if not getattr(parsed, "entries", None):
                        print(f"[ingest] no entries from {feed_url}")
                        continue

                    for e in parsed.entries[:25]:
                        title = (e.get("title") or "").strip()
                        link  = (e.get("link")  or "").strip()
                        desc  = (e.get("summary") or e.get("description") or "").strip()
                        if not title or not link:
                            continue

                        key = store.dedup_key(title, link)

                        published = None
                        try:
                            if "published_parsed" in e and e.published_parsed:
                                published = datetime(*e.published_parsed[:6], tzinfo=timezone.utc)
                        except Exception:
                            published = None

                        summary = summarize_text(title, desc)
                        senti = sentiment_score(summary)

                        item = NewsItem(
                            id=key, source=source, title=title, link=link,
                            published_at=published, summary=summary, sentiment=senti,
                            category=None
                        )
                        if store.add(item):
                            print(f"[ingest] + {source}: {title[:80]}")
                            await out_queue.put(item)
                # brief pause between feed batches
            except Exception as ex:
                print(f"[ingest] loop error: {ex}")

            await asyncio.sleep(POLL_INTERVAL)

