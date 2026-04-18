from newspaper import Article

def fetch_article(url: str) -> str:
    try:
        article = Article(url)
        article.download()
        article.parse()

        text = article.text.strip()

        if len(text) < 300:
            return None

        return text
    except Exception:
        return None