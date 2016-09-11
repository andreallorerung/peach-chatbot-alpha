import postprocess.message_decorator


class MockDecorator(postprocess.message_decorator.MessageDecorator):
    def __init__(self):
        pass

    def decorateMessageWith(self, message, result):
        if message is None:
            return None
        elif len(message) == 0:
            return ""
        else:
            return "You can find more information here: {}".format(result)
    
