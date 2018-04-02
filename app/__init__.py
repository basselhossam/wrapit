
# coding: utf-8

# In[ ]:


from flask import Flask
from flask import jsonify
from flask import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from copy import deepcopy

class FrequencySummarizer:
  def __init__(self, min_cut=0.2, max_cut=0.8):
    """
     Initilize the text summarizer.
     Words that have a frequency term lower than min_cut
     or higer than max_cut will be ignored.
    """
    self._min_cut = min_cut
    self._max_cut = max_cut
    self._stopwords = set(stopwords.words('english') + list(punctuation))

  def _compute_frequencies(self, word_sent):
    """
      Compute the frequency of each of word.
      Input:
       word_sent, a list of sentences already tokenized.
      Output:
       freq, a dictionary where freq[w] is the frequency of w.
    """
    freq = defaultdict(int)
    for s in word_sent:
      for word in s:
        if word not in self._stopwords:
          freq[word] += 1
    # frequencies normalization and fitering
    m = float(max(freq.values()))
    k=deepcopy(freq)
    for w in k.keys():
      freq[w] = freq[w]/m
      if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
          del freq[w]
    return freq

  def summarize(self, text, n):
    """
      Return a list of n sentences
      which represent the summary of text.
    """
    sents = sent_tokenize(text)
    assert n <= len(sents)
    word_sent = [word_tokenize(s.lower()) for s in sents]
    self._freq = self._compute_frequencies(word_sent)
    ranking = defaultdict(int)
    for i,sent in enumerate(word_sent):
      for w in sent:
        if w in self._freq:
          ranking[i] += self._freq[w]
    sents_idx = self._rank(ranking, n)
    return [sents[j] for j in sents_idx]

  def _rank(self, ranking, n):
    return nlargest(n, ranking, key=ranking.get)

def textCnn(newsurl):
    finaltext = ""
    article = urlopen(newsurl)
    soup = BeautifulSoup(article, 'html.parser')
    name_box = soup.findAll(attrs={'class': 'zn-body__paragraph'})
    for child in name_box:
        finaltext += " " + child.text
    return finaltext

app = Flask(__name__)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print(content['url'])
    sens = textCnn(content['url'])
    fs = FrequencySummarizer()
    summary = fs.summarize(sens, 4)
    return jsonify(summary)

