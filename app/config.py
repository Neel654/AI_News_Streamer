from dotenv import load_dotenv
import os
load_dotenv()

def env_list(key: str, default: str) -> list[str]:
    raw = os.getenv(key, default)
    return [s.strip() for s in raw.split(",") if s.strip()]

# TEMP: only one stable feed for testing
FEEDS = [
    "https://feeds.bbci.co.uk/news/rss.xml"
]

# poll faster while debugging
POLL_INTERVAL = 15
MAX_ITEMS = 500

