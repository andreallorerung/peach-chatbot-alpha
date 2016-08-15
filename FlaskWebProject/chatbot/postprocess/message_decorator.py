'''Module to define the interface a system output message decorator is expected
to implement'''


class MessageDecorator(object):
    '''Interface a system output decorator is expected to implement'''
    def __init__(self):
        raise NotImplementedError("MessageDecorator is an interface")

    def decorateMessageWith(self, message, decorationData):
        '''To decorate the message with the decoration'''
        raise NotImplementedError("MessageDecorator is an interface")
