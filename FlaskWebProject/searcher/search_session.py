import pickle

class SearchSession:

    def __init__(self):
        self.query = None
        self.index = None
        self.resultsList = []

    def search(self, query):
        self.query = query
        string = self.query
        if string in (self.index).keys():
            for key in (self.index)[string]:
                self.resultsList.append(key)
        else:
            self.resultsList.append('no results found')

        return self.resultsList

    def add_index(self, index):
        with open(index, 'rb') as handle:
            indexList = pickle.loads(handle.read())
        self.index = indexList
