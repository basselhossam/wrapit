import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from app.config import firebaseAuth


class DBManager:
    def __init__(self):
        try:
            cred = credentials.Certificate(firebaseAuth)

            # Initialize the app with a service account, granting admin privileges
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://wrap-it-9f8b4.firebaseio.com'
            })

            # As an admin, the app has access to read and write all data, regradless of Security Rules
            self.ref = db.reference('/')
        except:
            self.ref = db.reference('/')

    def addArticles(self,articlesList):
        for article in articlesList:
            posts_ref = self.ref.child('sources/' + article['newsApiID'] + '/articles')
            posts_ref.push().set(article)
        return True

    def getSummarizedArticles(self):
        sources_ref = self.ref.child('sources')
        dbSourcesList = sources_ref.get()
        articles = {}
        for sourceKey in dbSourcesList:
            val = dbSourcesList[sourceKey]
            articles[val['name']] = val['articles']
        return articles

    def getSummarizedArticlesURL(self):
        sources_ref = self.ref.child('sources')
        dbSourcesList = sources_ref.get()
        articles = []
        for sourceKey in dbSourcesList:
            val = dbSourcesList[sourceKey]
            for key in val['articles']:
                articles.append(val['articles'][key]['url'])
        return articles

    def getSources(self):
        sources_ref = self.ref.child('sources')
        return sources_ref.get()

    def getNewsApiSourcesIDs(self):
        sources_ref = self.ref.child('sources')
        dbSourcesList = sources_ref.get()
        sourcesList = ''
        for key in dbSourcesList:
            sourcesList = sourcesList + key + ','
        return sourcesList[:-1]
