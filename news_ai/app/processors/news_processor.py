from app.services.article_service import fetch_article
from app.services.translation_service import translate_text
from app.services.ai_service import AIService
from app.utils.cache import get_cache, set_cache

class NewsProcessor:

    def __init__(self):
        self.ai = AIService()

    def process(self, url: str, lang: str):
        cache_key = f"{url}_{lang}"

        cached = get_cache(cache_key)
        if cached:
            return cached

        text = fetch_article(url)

        if not text:
            return {"error": "Unable to fetch article"}

        summary = self.ai.summarize(text)
        eli10 = self.ai.eli10(text)
        www = self.ai.extract_wwww(text)

        # SAFE TRANSLATION
        text_t = translate_text(text, lang)
        summary_t = translate_text(summary, lang)
        eli10_t = translate_text(eli10, lang)

        result = {
            "FULL_NEWS": text_t,
            "AI_SHORT": summary_t,
            "ELI10": eli10_t,
            "WHO_WHAT_WHY": www
        }

        set_cache(cache_key, result)

        return result