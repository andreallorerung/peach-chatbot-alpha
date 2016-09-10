'''Auxiliary module to load rivescript brain information and initialize the
interpreter properly'''
import os
import rivescript

def loadBrain(interpreter, brain):
    '''To load the brain at filepath'''
    interpreter = _loadDirOrFile(interpreter, brain)
    interpreter.sort_replies()

    return interpreter

def _loadDirOrFile(interpreter, brain):
    '''To load either a directory or a file of rivescript brain data'''
    new_interpreter = interpreter

    if os.path.isdir(brain):
        new_interpreter.load_directory(brain)
    elif os.path.isfile(brain):
        new_interpreter.load_file(brain)
    else:
        raise ValueError("no directory or file found at specified filepath "
                        "for chatbot brain:'{}'".format(brain))

    return new_interpreter
