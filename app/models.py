from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class NewsItem(BaseModel):
    id: str                   # hash of title+link
    source: str               # feed title/domain
    title: str
    link: HttpUrl
    published_at: Optional[datetime] = None
    summary: str
    sentiment: float          # VADER compound (-1..+1)
    category: Optional[str] = None

