'''
Module responsible for serializing and writing the classifier to file.

See: http://stackoverflow.com/questions/10017086/save-naive-bayes-trained-classifier-in-nltk
'''
import pickle

def serialize(classifier, filepath):
    '''
    Method that serializes a classifier into a .pickle file at the specified
    filepath
    '''
    with open(filepath, "wb") as ostream:
        pickle.dump(classifier, ostream)
