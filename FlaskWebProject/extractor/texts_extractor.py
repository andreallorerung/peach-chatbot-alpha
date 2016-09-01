import urllib
import urlparse
from bs4 import BeautifulSoup, SoupStrainer
from urlparse import urljoin

class TextExtractor(object):

    '''Extracts Texts from Given Urls:
    Takes urlList returned by Crawler as input
    Returns urlToTextMap as output
    '''

    def __init__(self, urlList):
        self.urlList = urlList
        self.urlToText = {}

    def extract(self, urlList):
        for url in (self.urlList):
            r = urllib.urlopen(url).read()
            soup = BeautifulSoup(r, "lxml")
            for s in soup(["script", "style"]):
                s.extract()
            t = soup.get_text()
            lines = (line.strip() for line in t.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            t = ' '.join(chunk for chunk in chunks if chunk)
            self.urlToText[url] = t

        return self.urlToText
