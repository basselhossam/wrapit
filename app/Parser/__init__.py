from bs4 import BeautifulSoup
from urllib import urlopen


def parse(newsurl):
    finaltext = ""
    category = ""
    try:
        article = urlopen(newsurl)
        soup = BeautifulSoup(article, 'html.parser')
        if "dailymail" in newsurl:
            name_box = soup.findAll("p", {"class": "mol-para-with-font"})
        elif "abcnews" in newsurl:
            name_box = soup.findAll('p')
        elif "bleacherreport" in newsurl:
            name_box = soup.findAll('p')
            category = "sports"
        for child in name_box:
            finaltext += " " + child.text.strip()
        if "Sports" in newsurl:
            category = "sports"
        elif "US" in newsurl:
            category = "us"
        elif "International" in newsurl:
            category = "international"
        elif "Politics" in newsurl:
            category = "politics"
        elif "Technolog" in newsurl:
            category = "tech"
        elif "Lifestyle" in newsurl:
            category = "lifestyle"
        elif "Entertainment" in newsurl:
            category = "entertainment"
        elif "Wellness" in newsurl:
            category = "health"
        elif "Health" in newsurl:
            category = "health"
        elif "femail" in newsurl:
            category = "femail"
        elif "wires" in newsurl:
            category = "wires"
        elif "travel" in newsurl:
            category = "travel"
        elif "sciencetech" in newsurl:
            category = "tech"
        elif "sport" in newsurl:
            category = "sports"
        elif "tvshowbiz" in newsurl:
            category = "tvshowbiz"
        elif "news" in newsurl:
            category = "news"
        elif "health" in newsurl:
            category = "health"
        return finaltext, category
    except:
        return ""