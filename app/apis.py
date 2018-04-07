from app import app
from flask import jsonify
from flask import request
from app.FrequencySummarizer import FrequencySummarizer
from app.Parser import parse
from app.NewsSource import NewsSources
from app.DBAdmin import DBManager


@app.route('/summarize', methods=['POST'])
def summarize():
    urls = request.get_json()
    summaries = []
    for url in urls:
        sens = parse(url)
        fs = FrequencySummarizer()
        summaries.append(fs.summarize(sens, 4))
    return jsonify(summaries)


@app.route('/getnews', methods=['GET'])
def getnews():
    db = DBManager()
    api = NewsSources()
    newsResponse = api.getNewsFromSources()
    newArticles = list(set(newsResponse['articlesURLs']) - set(db.getSummarizedArticlesURL()))
    for url in newArticles:
        sens = parse(url)
        fs = FrequencySummarizer()
        textsum = fs.summarize(sens, 4)
        if False != textsum:
            newsResponse['articlesData'][url]["exSummary"] = textsum
        else:
            del newsResponse['articlesData'][url]
    ret = {'status': 'Failed'}
    if db.addArticles(newsResponse['articlesData'].values()):
        ret = {'status': 'ok', 'summarizedCount': len(newsResponse['articlesData'].values())}
    return jsonify(ret)

@app.route('/getsummarizedarticles', methods=['GET'])
def getSummarizedArticles():
    db = DBManager()
    return jsonify(db.getSummarizedArticles())

@app.route('/getsources', methods=['GET'])
def getSources():
    db = DBManager()
    return jsonify(db.getSources())
