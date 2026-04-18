from transformers import pipeline
from app.config import MODEL_SUMMARY

class ModelLoader:
    _summarizer = None

    @classmethod
    def get_summarizer(cls):
        if cls._summarizer is None:
            cls._summarizer = pipeline(
                "summarization",
                model=MODEL_SUMMARY
            )
        return cls._summarizer