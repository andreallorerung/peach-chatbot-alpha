from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class IndexerInverted(object):

    '''Creates an Inverted Index:
    Takes urlToTextMap returned by Extractor as input
    Returns invertedIndexMap as output''''

    def __init__(self, myTextDict):
        self.myTextDict = myTextDict
        self.invertedIndex = {}

    def build(self, myTextDict):
        documents = (value for key, value in (self.myTextDict).iteritems())
        stoplist = set(stopwords.words('english'))
        texts = [[word for word in document.lower().split() if word not in stoplist]
                 for document in documents]
        dictionary = corpora.Dictionary(texts)
        for tok in dictionary:
            for key, value in (self.myTextDict).iteritems():
                if dictionary[tok] in value:
                    if any(dictionary[tok] is term for term, urls in (self.invertedIndex).iteritems()):
                        if key not in self.invertedIndex[(dictionary[tok])]:
                            self.invertedIndex[(dictionary[tok])].append(key)
                    else:
                        self.invertedIndex[(dictionary[tok])] = [key]

        return self.invertedIndex
