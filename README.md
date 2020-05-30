# Wrapit News Summarization

This is the Server Side for Mobile App that allows users to subscribe to news sources and use [News API](https://newsapi.org/) 
to get new news from these sources and get the new links
____________________________________________________________
## Libraries:
* [Flask Python](http://flask.pocoo.org/)
* [FireBase Real Time Database](https://firebase.google.com/docs/database/)
* [News API](https://newsapi.org/)
* [NLTK](https://www.nltk.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
____________________________________________________________
## How it works:
1. We fetch the news from newsapi and then check if these articles are summarized or not
2. get the new articles and then parse it to extract the content
3. pass the content to the summarization modules and then store the result in the database so the app can retrieve it
____________________________________________________________
## Demo APIs:
#### Get all sumarized news from database: 
https://wrapit2018.herokuapp.com/getsummarizedarticles `HTTP GET`
#### Fetch new news and add them to the database: 
https://wrapit2018.herokuapp.com/getnews `HTTP GET`
____________________________________________________________
## Supported Sources:
* [CNN](https://edition.cnn.com/)

Working on Adding more in the future
____________________________________________________________
## Mobile App:
[Flutter App Repo](https://github.com/basselhossam/wrapit-flutter)
____________________________________________________________
##### this is my graduation project for Faculty of Engineering Cairo University 2017/2018
