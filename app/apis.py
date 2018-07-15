from app import app
from flask import jsonify
from flask import request
import requests
import json
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
        sens, cat = parse(url)
        fs = FrequencySummarizer()
        textsum = fs.summarize(sens, 4)
        s = 0
        if False != textsum:
            for x in textsum:
                s = s + len(x)
            newsResponse['articlesData'][url]["exSummary"] = textsum
            newsResponse['articlesData'][url]["category"] = cat
            newsResponse['articlesData'][url]["ratio"] = s / (len(sens) * 1.0)
        else:
            del newsResponse['articlesData'][url]
    headers = {'content-type': 'application/json'}
    r = requests.post("https://summarizar.localtunnel.me/api", data=json.dumps(list(newsResponse['articlesData'].keys())), headers=headers)
    if r.status_code == 200:
        x = r.json()
        i = 0
        for url in list(newsResponse['articlesData'].keys()):
            newsResponse['articlesData'][url]["abSummary"] = x[i]
            i = i + 1
    else:
        ret = {'status': 'abSummary Failed'}
        return jsonify(ret)
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
