'''Module to write rivescript data to '''
import collections
import rivescript_generation

def write(filepath, writemode='a', *args):
    with open(filepath, writemode) as f:
        for array in args:
            f.write("{}{}".format(array,'\n'))
