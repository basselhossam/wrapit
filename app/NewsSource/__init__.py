from newsapi.newsapi_client import NewsApiClient
from app.config import newsApiKey, appLanguage, pageSize
from app.DBAdmin import DBManager


class NewsSources:
    def __init__(self):
        self.db = DBManager()
        self.news_api = NewsApiClient(api_key=newsApiKey)

    def getNewsFromSources(self):
        newsData = self.news_api.get_everything(sources=self.db.getNewsApiSourcesIDs(),
                                                language=appLanguage,
                                                page_size=pageSize)['articles']
        res = {'articlesData': {}, 'articlesURLs': []}
        for article in newsData:
            articleDict = {'title': article['title'], 'url': article['url'],
                           'image': article['urlToImage'], 'time': article['publishedAt'],
                           'newsApiID': article['source']['id']}
            res['articlesData'][article['url']] = articleDict
            res['articlesURLs'].append(article['url'])
        return res
