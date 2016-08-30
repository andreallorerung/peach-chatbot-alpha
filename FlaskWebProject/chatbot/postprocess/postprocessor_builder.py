import postprocess.keyword_extractor_single
import postprocess.message_decorator_single
import botinterface.postprocessor

def build():
    return None
    # botinterface.postprocessor.MessagePostprocessor(keywordExtractor=postprocess.keyword_extractor_single.SingleKeywordExtractor(),
    #                                                         searchAdapter= the real search adapter,
    #                                                         messageDecorator=postprocess.message_decorator_single.MessageDecoratorSingle())
