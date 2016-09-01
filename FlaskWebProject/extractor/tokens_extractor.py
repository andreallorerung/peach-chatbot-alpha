import urllib
import urlparse
from bs4 import BeautifulSoup, SoupStrainer
from urlparse import urljoin

class TokenExtractor(object):

    '''Extracts Tokens from Given Urls:
    Takes urlList returned by Crawler as input
    Returns idToTokensMap as output
    '''

    def __init__(self, urlList):
        self.urlList = urlList
        self.idToToken = {}

    def extract(self, urlList):
        documents = (value for key, value in (extract_text()).iteritems())
        stoplist = set(stopwords.words('english'))
        texts = [[word for word in document.lower().split() if word not in stoplist]
                 for document in documents]
        self.idToToken = corpora.Dictionary(texts)

        return self.idToToken
