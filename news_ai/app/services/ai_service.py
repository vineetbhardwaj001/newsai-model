from app.models.pipeline_loader import ModelLoader
from app.utils.cleaner import clean_text

class AIService:

    def __init__(self):
        self.summarizer = ModelLoader.get_summarizer()

    def summarize(self, text: str):
        text = clean_text(text[:1000])

        prompt = (
            "Summarize the following news strictly based on the text. "
            "Do not add any new information:\n" + text
        )

        try:
            result = self.summarizer(prompt, max_length=120, min_length=50)
            return result[0]['summary_text']
        except Exception:
            return text[:200]

    def eli10(self, text: str):
        text = clean_text(text[:800])

        prompt = "Explain this news in very simple words:\n" + text

        try:
            result = self.summarizer(prompt, max_length=100)
            return result[0]['summary_text']
        except Exception:
            return "Simple explanation unavailable"

    def extract_wwww(self, text: str):
        return {
            "Who": text[:100],
            "What": text[100:250],
            "Why": "This news is important for public awareness"
        }