class MockMessageProcessor(object):
    def process(self, message):
        return "Processed message: '{}'".format(message)


def getProcessor():
    return MockMessageProcessor()
