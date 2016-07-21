import os
from rivescript import RiveScript

def main(args):

    if len(args) <= 1:
        brain = "./brain"
    else:
        brain = args[1]

    bot = RiveScript()
    bot.load_directory(brain)
    bot.sort_replies()

    while True:
        msg = raw_input("You> ")
        if msg == "/q":
            quit()

        reply = bot.reply("localuser", msg)
        print "Bot> ", reply

def _create_bot(brain):
    if not args or not len(args):
        brain = "./brain"
    else:
        brain = args[0]

    bot = RiveScript()

    if os.path.isdir(brain):
        bot.load_directory(brain)
    elif os.path.isfile(brain):
        bot.load_file(brain)
    else:
        raise ValueError("no directory or file found at specified filepath for "
                         "chatbot brain.")
    bot.sort_replies()

    return bot

if __name__ == '__main__':
    import sys
    main(sys.argv)
