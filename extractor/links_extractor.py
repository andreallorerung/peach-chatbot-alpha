import urllib
import urlparse
from bs4 import BeautifulSoup, SoupStrainer
from urlparse import urljoin

class LinkExtractor(object):

    '''Extracts Links from Given Urls:
    Takes urlList returned by Crawler as input
    Returns urlToLinksMap as output
    '''

    def __init__(self, urlList):
        self.urlList = urlList
        self.urlToLinks = {}

    def extract(self, urlList):
        for url in (self.urlList):
            r = urllib.urlopen(url).read()
            soup = BeautifulSoup(response, parse_only=SoupStrainer('a', href=True))
            links = soup.find_all('a')
            links = [l.get('href') for l in links]
            links = [unicode(l) for l in links]
            links = [l for l in links if (l.startswith("https://") or l.startswith("http://"))]
            links = set(links)
            self.urlToLinks[url] = [links]

        return self.urlToLinks
