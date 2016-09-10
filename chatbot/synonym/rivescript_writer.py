'''Module to write rivescript data to '''
import store_synonyms


class RivescriptArrayWriter(store_synonyms.SynonymWriter):
    '''Class to provide a concrete implementation of a synonym writer for
    rivescript, compliant with rivescript 2.0 standard:
    https://www.rivescript.com/wd/RiveScript'''

    @staticmethod
    def writetofile(filepath, writemode='a', *args):
        with open(filepath, writemode) as f:
            for array in args:
                f.write("{}{}".format(array,'\n'))
