import pprint
from categorize.training import train
from categorize.classifier_serializer import serialize
from categorize.classifier_deserializer import deserialize
from categorize.dataset_reading import read_data
from categorize.dataset_splitting import split
from categorize import develop
from categorize.evaluation import ClassifierEvaluator

SAMPLEDATAFILE="categorize/data/sample_data.csv"
DATAFILE="categorize/data/NLPresults.csv"
FORMAT="csv"
OUTPUTFILE = "categorize/data/classifier.pickle"
SAMPLELABELS = ["pos", "neg"]
LABELS =["phys", "pract", "family", "emotion", "spiritual"]

def demo(args):

    with open(DATAFILE, 'r') as istream:
        print "Reading data from \"{}\" ...".format(DATAFILE)
        dataset = read_data(istream, format=FORMAT)

    print "Splitting data set ..."
    train_set, dev_set, test_set = split(dataset, shuffle=False)

    print "Training classifier ..."
    classifier = train(train_set)
    print "Finished training."

    print "Storing classifier in \"{}\"".format(OUTPUTFILE)
    serialize(classifier, filepath=OUTPUTFILE)

    print "Testing classifier against dev set ..."
    develop.test(classifier, dev_set)
    print "Test result:"
    develop.print_errors()

    print "Initializing evaluator instance ..."
    evaluator = ClassifierEvaluator(classifier, test_set)

    accuracy_score = evaluator.accuracy()
    print "Accuracy: {:.2f}".format(accuracy_score)

    for label in LABELS:
        recall_score = evaluator.recall(label)
        precision_score = evaluator.precision(label)
        fmeasure_score = evaluator.f_measure(label)

        print "Recall for '{}': {}".format(label, recall_score)
        print "Precision for '{}': {}".format(label, precision_score)
        print "F for '{}': {}".format(label, fmeasure_score)

    macroRecall = evaluator.macroAvgRecall(LABELS)
    macroPrecision = evaluator.macroAvgPrecision(LABELS)
    microRecall = evaluator.microAvgRecall(LABELS)
    microPrecision = evaluator.microAvgPrecision(LABELS)
    print "Macro averaged recall: {}".format(macroRecall)
    print "Macro averaged precision: {}".format(macroPrecision)
    print "Micro averaged recall: {}".format(microRecall)
    print "Micro averaged precision: {}".format(microPrecision)

if __name__ == '__main__':
    import sys
    demo(sys.argv)
