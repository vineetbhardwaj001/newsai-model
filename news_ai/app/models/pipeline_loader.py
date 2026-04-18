from transformers import pipeline

class ModelLoader:
    _summarizer = None

    @classmethod
    def get_summarizer(cls):
        if cls._summarizer is None:
            cls._summarizer = pipeline(
                "text2text-generation",
                model="facebook/bart-large-cnn"
            )
        return cls._summarizer