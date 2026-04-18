from app.models.pipeline_loader import ModelLoader
from app.utils.cleaner import clean_text

class AIService:

    def __init__(self):
        self.summarizer = ModelLoader.get_summarizer()

    def summarize(self, text: str):
        text = clean_text(text[:800])
        try:
            result = self.summarizer(text, max_length=80, min_length=30)
            return result[0]['summary_text']
        except Exception:
            return text[:150]

    def eli10(self, text: str):
        prompt = "Explain simply: " + text[:500]
        try:
            result = self.summarizer(prompt, max_length=100)
            return result[0]['summary_text']
        except Exception:
            return "Simple explanation unavailable"

    def extract_wwww(self, text: str):
        return {
            "Who": text[:80],
            "What": text[80:200],
            "Why": "Important for public awareness"
        }