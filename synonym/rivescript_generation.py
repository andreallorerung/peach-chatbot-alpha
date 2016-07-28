

class RivescriptGenerator(object):

    def generateArray(word, synonyms):

        fomrattedSynonyms = "|".join(synonyms)
        return "! array {}".format(word, formattedSynonyms)

    def writeToRivescriptFile(filepath):
        with open(filepath) as f:
            f.write(?)
