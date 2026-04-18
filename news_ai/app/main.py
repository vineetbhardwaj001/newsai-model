from app.processors.news_processor import NewsProcessor

def run():
    processor = NewsProcessor()

    url = input("Enter news URL: ")
    lang = input("Language (en/hi/ta/bn): ")

    result = processor.process(url, lang)

    print("\n===== RESULT =====\n")
    for k, v in result.items():
        print(f"{k}:\n{v}\n")

if __name__ == "__main__":
    run()