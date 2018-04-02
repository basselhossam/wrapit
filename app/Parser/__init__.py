from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlsplit


def parse(url):
    netloc = "{0.netloc}".format(urlsplit(url))
    if netloc == "edition.cnn.com":
        return textCnn(url)


def textCnn(url):
    final_text = ""
    article = urlopen(url)
    soup = BeautifulSoup(article, 'html.parser')
    name_box = soup.findAll(attrs={'class': 'zn-body__paragraph'})
    for child in name_box:
        final_text += " " + child.text
    return final_text
