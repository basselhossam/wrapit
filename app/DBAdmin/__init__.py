import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from app.config import firebaseAuth


class DBManager:
    def __init__(self):
        try:
            print(firebaseAuth)
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
        posts_ref = self.ref.child('articles')
        for article in articlesList:
            posts_ref.push().set(article)
        return True

    def getSummarizedArticles(self):
        posts_ref = self.ref.child('articles')
        return posts_ref.get()

    def getSummarizedArticlesURL(self):
        posts_ref = self.ref.child('articles')
        articlesList = posts_ref.get()
        articlesURLs = []
        for key in articlesList:
            articlesURLs.append(articlesList[key]['url'])
        return articlesURLs

    def getSources(self):
        sources_ref = self.ref.child('sources')
        return sources_ref.get()

    def getNewsApiSourcesIDs(self):
        sources_ref = self.ref.child('sources')
        dbSourcesList = sources_ref.get()
        sourcesList = ''
        for val in dbSourcesList:
            sourcesList = sourcesList + val['newsApiID'] + ','
        return sourcesList[:-1]
