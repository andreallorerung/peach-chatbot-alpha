'''
Module responsible for deserializing a classifier.

See: http://stackoverflow.com/questions/10017086/save-naive-bayes-trained-classifier-in-nltk
'''
import pickle

def deserialize(filepath="categorize/data/classifier.pickle"):
    '''
    Deserializes a classfifier from file.

    '''
    with open(filepath, "rb") as istream:
        classifier = pickle.load(istream)
    return classifier
