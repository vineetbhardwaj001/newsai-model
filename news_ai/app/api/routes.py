from fastapi import APIRouter, Query
from app.processors.news_processor import NewsProcessor

router = APIRouter()
processor = NewsProcessor()


@router.get("/")
def home():
    return {
        "status": "running",
        "message": "🚀 News AI API is live"
    }


@router.get("/analyze")
def analyze_news(
    url: str = Query(..., description="News article URL"),
    lang: str = Query("en", description="Language (en, hi, ta, bn)")
):
    try:
        result = processor.process(url, lang)
        return {
            "success": True,
            "data": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }