from app import app
from flask import jsonify
from flask import request
from app.FrequencySummarizer import FrequencySummarizer
from app.Parser import parse


@app.route('/summarize', methods=['POST'])
def summarize():
    urls = request.get_json()
    summaries = []
    for url in urls:
        sens = parse(url)
        fs = FrequencySummarizer()
        summaries.append(fs.summarize(sens, 4))
    return jsonify(summaries)
