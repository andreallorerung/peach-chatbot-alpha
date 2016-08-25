import preprocess.tokenizer_simple
import preprocess.stopwords_remover_lenient
import preprocess.stemmer_factory
import botinterface.preprocessor

def build():
    return botinterface.preprocessor.MessagePreprocessor(tokenizer=preprocess.tokenizer_simple.SimpleTokenizerProxy(),
                                        stopwordRemover=preprocess.stopwords_remover_lenient.StopwordRemoverLenient(),
                                        stemmer=preprocess.stemming_lancaster.Lancaster())
