from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import re

_sia = SentimentIntensityAnalyzer()

def strip_html(text: str) -> str:
    return re.sub("<[^>]+>", "", text or "")

def _safe_sent_tokenize(text: str):
    try:
        return sent_tokenize(text)
    except LookupError:
        # fallback: split on sentence punctuation
        return re.split(r'(?<=[.!?])\s+', text or "")

def summarize_text(title: str, desc: str | None, max_sentences: int = 2) -> str:
    parts = []
    if title:
        parts.append(title.strip())
    if desc:
        sents = [s.strip() for s in _safe_sent_tokenize(strip_html(desc)) if s.strip()]
        if sents:
            parts.append(sents[0])
    seen, uniq = set(), []
    for p in parts:
        if p not in seen:
            uniq.append(p); seen.add(p)
    text = " — ".join(uniq)
    if not text and desc:
        text = " ".join(_safe_sent_tokenize(strip_html(desc))[:max_sentences])
    return text[:400]

def sentiment_score(text: str) -> float:
    return float(_sia.polarity_scores(text or "")["compound"])

