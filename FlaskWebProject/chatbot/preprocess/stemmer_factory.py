'''Module to create objects that know how to stem words'''
import nltk.stem.lancaster

def get_stemmer():
    '''To retrun a suitable stemmer'''
    return nltk.stem.lancaster.LancasterStemmer()
