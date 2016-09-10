'''
Evaluates a classifier against a test set.
'''
import collections
from nltk.metrics import scores

class ClassifierEvaluator(object):

    def __init__(self, classifier, gold):
        self._classifier = classifier
        self._gold = gold
        self._referenceSets, self._testSets = \
                            self._get_reference_and_test_sets(classifier, gold)

    def _get_reference_and_test_sets(self, classifier, test):
        '''
        Gets a reference and test set for the classifier over the specified test
        set.

        See: http://streamhacker.com/2010/05/17/text-classification-sentiment-analysis-precision-recall/
        '''
        reference_sets = collections.defaultdict(set)
        test_sets = collections.defaultdict(set)
        for i, (data_point, label) in enumerate(test):
            reference_sets[label].add(i)
            guess = classifier.classify(data_point)
            test_sets[guess].add(i)

        return reference_sets, test_sets

    def precision(self, label):
        return scores.precision(self._referenceSets[label], \
                                self._testSets[label])

    def recall(self, label):
        return scores.recall(self._referenceSets[label], \
                            self._testSets[label])

    def f_measure(self, label, alpha=0.5):
        return scores.f_measure(self._referenceSets[label], \
                                self._testSets[label], alpha)

    def accuracy(self):
        return self._classifier.accuracy(self._gold)

    def macroAvgPrecision(self, labels):
        return self._macroAvg(labels, self.precision)

    def macroAvgRecall(self, labels):
        return self._macroAvg(labels, self.recall)

    def _macroAvg(self, labels, function):
        sumScores = 0
        for label in labels:
            resultOnSingleLabel = function(label)
            toAdd = resultOnSingleLabel if resultOnSingleLabel is not None else 0
            sumScores = sumScores + toAdd

        if len(labels) > 0:
            return sumScores / len(labels)

    def microAvgPrecision(self, labels):
        return self._microAvg(labels, self._testSets)

    def microAvgRecall(self, labels):
        return self._microAvg(labels, self._referenceSets)

    def _microAvg(self, labels, denominatorSets):
        numerator = 0
        denominator = 0

        for label in labels:
            numerator = numerator + len(self._referenceSets[label].intersection(self._testSets[label]))
            denominator = denominator + len(denominatorSets[label])

        if denominator > 0:
            return numerator / float(denominator)
        else:
            return 0
