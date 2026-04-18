from deep_translator import GoogleTranslator

def translate_text(text: str, lang: str):
    try:
        if lang == "en":
            return text
        return GoogleTranslator(source='auto', target=lang).translate(text)
    except Exception:
        return text