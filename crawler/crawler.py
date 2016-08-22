import urllib
import urlparse
from bs4 import BeautifulSoup, SoupStrainer

class Crawler:

    '''Instatiates a Spider:
    Takes a seed url and domain name as input
    Returns a list of all urls in domain as output'''

    def __init__(self, url, domain):
        self.url = url
        self.domain = domain
        self.visitedUrls = []
        self.toVisitUrls = []

    def visit(self, url):
        response = urllib.urlopen(url).read()
        self.visitedUrls.append(url)
        soup = BeautifulSoup(response, parse_only=SoupStrainer('a', href=True))
        links = soup.find_all('a')
        links = [l.get('href') for l in links]
        links = [unicode(l) for l in links]
        links = [l for l in links if (l.startswith("https://") or l.startswith("http://"))]
        links = set(links)
        for l in links:
            if l not in self.visitedUrls:
                self.toVisitUrls.append(l)
        for url in self.toVisitUrls:
            self.visit(url)

        return self.visitedUrls
