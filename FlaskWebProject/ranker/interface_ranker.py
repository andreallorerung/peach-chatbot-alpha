class RankerInterface(object):

    '''Ranker Interface'''

    def __init__(self):
        raise NotImplementedError("RankerInterface is an interface")

    def build(self, occurrence):
        raise NotImplementedError("RankerInterface is an interface")
