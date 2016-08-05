import os

def loadBrain(interpreter, brain):
    interpreter = _loadDirOrFile(interpreter, brain)
    interpreter.sort_replies()

    return interpreter

def _loadDirOrFile(interpreter, brain):
    new_interpreter = interpreter

    if os.path.isdir(brain):
        new_interpreter.load_directory(brain)
    elif os.path.isfile(brain):
        new_interpreter.load_file(brain)
    else:
        raise ValueError("no directory or file found at specified filepath "
                        "for chatbot brain.")

    return new_interpreter
