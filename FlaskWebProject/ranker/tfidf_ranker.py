import math
from decimal import *
import operator

class Tfidf:

    '''Creates a TFIDF Ranked Inverted Index:
    Takes urlToText and tokenToUrlsList maps as input
    Returns tokenToTfidfUrls map as output '''

    tokenToTfidfUrls = {}
    tokenToDocOcc = {}

    def __init__(self, myTextDict, myInvertedDict):
        self.myTextDict = myTextDict
        self.myInvertedDict = myInvertedDict
        self.tokenToTfidfUrls = {}
        self.tokenToDocOcc = {}

    def build(self):
        self.tokenToDocOcc = self.get_occurrence()
        for tok, list_docs in self.tokenToDocOcc.iteritems():
            list_urls_score = {}
            for key, value in (self.myTextDict).iteritems():
                term_freq = value.count(tok)
                getcontext().prec = 9
                idf = Decimal(len(map_url_text))/Decimal(1+list_docs)
                log_idf = math.log(idf, 2)
                score_tfidf = Decimal(term_freq*log_idf)
                list_urls_score[key] = score_tfidf
            self.tokenToTfidfUrls[tok] = list_urls_score

        return self.tokenToTfidfUrls

    def _get_occurrence(self):
        for tok in (self.myInvertedDict):
            docs = []
            for k_url, value in (self.myTextDict).iteritems():
                if self.myInvertedDict[tok] in value:
                    docs.append(k_url)
                self.tokenToDocOcc[dictionary_bis[tok]] = len(docs)

        return self.tokenToDocOcc
