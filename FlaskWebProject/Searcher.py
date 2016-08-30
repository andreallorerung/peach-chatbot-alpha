from nltk.stem.porter import *

class Searcher:
    '''Runs search'''

    resultsList = []

    def __init__(self, query, myTokenToUrlsList):
        self.query = query
        self.myTokenToUrlsList = myTokenToUrlsList
        Searcher.resultsList = resultsList

    def search(self):
        string = (self.query).split()
        stemmer = PorterStemmer()
        for w in string:
            stemmer.stem(w)

        for i in string:
            for t, lst in (self.myTokenToUrlsList).iteritems():
                if i in t:
                    for key in sorted(lst, reverse=True)[:10]:
                        if (lst[key] != 0) or (i in key):
                            (Searcher.resultsList).append(key)

        return Searcher.resultsList
