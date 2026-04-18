import re

def clean_text(text: str):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\n+", " ", text)
    return text.strip()