from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class IndexerPositional(object):

    '''Creates a Positional Index:
    Takes urlToTextMap returned by Extractor as input
    Returns positionalIndexMap as output''''

    def __init__(self, myTextDict):
        self.myTextDict = myTextDict
        self.positionalIndex = {}
        self.visitedUrlTokenPair = {}

    def build(self, myTextDict):
        documents = (value for key, value in (self.myTextDict).iteritems())
        stoplist = set(stopwords.words('english'))
        texts = [[word for word in document.lower().split() if word not in stoplist]
                 for document in documents]
        dictionary = corpora.Dictionary(texts)
        for tokenId, token in dictionary.iteritems():
            for docId, text in (self.myTextDict).iteritems():
                docPos = {}
                for word in text.split():
                    if (token == word and ((docId not in visited) or (visited[docId] != token))):
                        indiceList = [i for i, x in enumerate(text.split()) if x == word]
                        docPos[docId] = indiceList
                        self.visitedUrlTokenPair[docId] = token
                        if token in self.positionalIndex:
                            self.positionalIndex[token][docId] = indiceList
                        else:
                            self.positionalIndex[token] = docPos

        return self.positionalIndex
