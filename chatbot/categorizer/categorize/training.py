'''
Module responsible for the training of a categorizer.

'''
import textblob.classifiers

def train(train_set):
    '''
    Trains a classifier over the train_set data

    '''

    classifier = textblob.classifiers.MaxEntClassifier(train_set)
    return classifier
