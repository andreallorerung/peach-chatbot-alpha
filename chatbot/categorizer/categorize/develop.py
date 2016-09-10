'''
Module responsible for handling the testing of a trained classifier against a
dev set for the purpose of investigating problem-specific implementations of
feature extractors.

See 1.2 in: http://www.nltk.org/book/ch06.html
'''

_errors = []

def test(classifier, dev_set):
    '''
    Returns a list of errors in the form of triples of actual, guess, data
    '''

    for (data, correct_tag) in dev_set:
        guess = classifier.classify(data)
        if guess != correct_tag:
            _errors.append( (correct_tag, guess, data) )

    return _errors

def print_errors(errors=_errors):
    '''
    Prints the list of errors to standard output. The parameter should be the
    output of test(classifier, dev_set)
    '''

    for (correct_tag, guess, data) in sorted(errors):
        print "correct={:<5} guess={:<5} data={:<20}".format(correct_tag, guess,\
                                                            data)
