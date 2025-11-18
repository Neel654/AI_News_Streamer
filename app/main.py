from pathlib import Path 
import asyncio, json
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import StreamingResponse
from .store import MemoryStore
from .models import NewsItem
from .ingest import poll_feeds
from .config import MAX_ITEMS

app = FastAPI(title="AI News Streamer", version="0.1.0")
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/", include_in_schema=False)
async def root():
    return FileResponse(str(STATIC_DIR / "index.html"))
store = MemoryStore(max_items=MAX_ITEMS)
broadcast_queue: asyncio.Queue[NewsItem] = asyncio.Queue()

@app.on_event("startup")
async def _startup():
    print("[startup] launching poll_feeds task…")
    asyncio.create_task(poll_feeds(store, broadcast_queue))

@app.get("/healthz", response_class=PlainTextResponse)
async def healthz():
    return "ok"

@app.get("/api/news", response_model=list[NewsItem])
async def api_news(limit: int = 25):
    return store.latest(limit)

@app.get("/stream")
async def stream(request: Request):
    async def event_gen():
        # replay snapshot
        for it in store.latest(25):
            yield sse_event(it)
        # live tail
        while True:
            if await request.is_disconnected():
                break
            try:
                item = await asyncio.wait_for(broadcast_queue.get(), timeout=1.0)
                yield sse_event(item)
            except asyncio.TimeoutError:
                yield b": keep-alive\n\n"
    return StreamingResponse(event_gen(), media_type="text/event-stream")

def sse_event(item: NewsItem) -> bytes:
    data = json.dumps(item.model_dump(), default=str)
    return f"event: news\ndata: {data}\n\n".encode()

# serve static UI (index.html)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/", include_in_schema=False)
async def root():
    return FileResponse("static/index.html")
