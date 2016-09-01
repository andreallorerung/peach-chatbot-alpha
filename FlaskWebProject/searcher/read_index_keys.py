from inverted_indexer import IndexerInverted
import pickle

# read dict from file
with open('inverted_integration_test.txt', 'rb') as handle:
    inverted = pickle.loads(handle.read())
