from collections import deque
from typing import Deque, Dict, Iterable
from hashlib import sha1
from .models import NewsItem

class MemoryStore:
    def __init__(self, max_items: int = 500):
        self._items: Deque[NewsItem] = deque(maxlen=max_items)
        self._seen: Dict[str, bool] = {}

    @staticmethod
    def _key(title: str, link: str) -> str:
        return sha1(f"{title}|{link}".encode()).hexdigest()

    def dedup_key(self, title: str, link: str) -> str:
        return self._key(title, link)

    def add(self, item: NewsItem) -> bool:
        if item.id in self._seen:
            return False
        self._seen[item.id] = True
        self._items.appendleft(item)
        return True

    def latest(self, limit: int = 20) -> Iterable[NewsItem]:
        return list(self._items)[:limit]

    def size(self) -> int:
        return len(self._items)

