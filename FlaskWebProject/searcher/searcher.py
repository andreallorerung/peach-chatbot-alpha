from nltk.stem.porter import *

class Searcher:
    '''Runs search'''

    def __init__(self, query, myTokenToUrlsList):
        self.query = query
        self.myTokenToUrlsList = {}
        self.resultsList = {}

    def search(self, query):
        string = (query).split()
        stemmer = PorterStemmer()
        for w in string:
            stemmer.stem(w)

        for i in string:
            for t, lst in (self.myTokenToUrlsList).iteritems():
                if i in t:
                    for key in sorted(lst, reverse=True)[:10]:
                        if (lst[key] != 0) or (i in key):
                            (self.resultsList)[key] = key

        return self.resultsList
