from fastapi import APIRouter
from app.processors.news_processor import NewsProcessor

router = APIRouter()
processor = NewsProcessor()

@router.get("/analyze")
async def analyze(url: str, lang: str = "en"):
    return processor.process(url, lang)