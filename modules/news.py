def execute():
    from GoogleNews import GoogleNews

    googlenews = GoogleNews(lang='en', region='US')
    googlenews.get_news()

    for i, result in enumerate(googlenews.results()[:5], start=1):
        print(f"{result['date']}, {result['reporter'] or 'anonymous'} with {result['media'] or 'unknown outlet'} posted:")
        print(f"-> {result['title']} - Read here: {result['link']}")
    
metadata = {
    "name": "news",
    "description": "Lists breaking news.",
    "args": ""
}

__all__ = ['execute', 'metadata']