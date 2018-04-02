from newsapi.newsapi_client import NewsApiClient
from app.config import newsApiKey, sourcesList, appLanguage


class NewsSources:
    def __init__(self):
        self.news_api = NewsApiClient(api_key=newsApiKey)

    def getNewsFromSources(self):
        return self.news_api.get_everything(sources=sourcesList, language=appLanguage)
