'''Module to implement a lenient stopwords remover'''
import stopwords_remover


class StopwordRemoverLenient(stopwords_remover.StopwordRemover):
    '''Class to remove stopwords, but allow most words to stay, in particular
    pronouns and negations as well as declinations of 'to be' '''
    def __init__(self):
        super(stopwords_remover.StopwordRemover)
        self.stopwords = set(['do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
        'but', 'if', 'or', 'as', 'of', 'at', 'by', 'for', 'with', 'about',
        'against', 'between', 'into', 'through', 'above', 'below', 'to', 'from',
        'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'such', 'too',
        'very', 's', 'can', 'will', 'just'])
