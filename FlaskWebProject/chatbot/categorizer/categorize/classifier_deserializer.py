'''
Module responsible for deserializing a classifier.

'''
import pickle

def deserialize(filepath="categorize/data/classifier.pickle"):
    '''
    Deserializes a classfifier from file.

    '''
    with open(filepath, "rb") as istream:
        classifier = pickle.load(istream)
    return classifier
