import os
from botcontroller import topics_model
from botcontroller import rivescriptmacrosmacros
from botinterface import bot_builder
import nltk.stem

USERID = "localuser"
USERNAME = "Nic"
WELCOME = "Bot> Hello {}, welcome.".format(USERNAME)
CHECKLISTMSG = ("Bot> Let me check what your concerns are and we will go through "
"them briefly."
"\nBot> I would like you to gather a bit more information about them ahead of "
"your visit.")
PREISSUES = ("Bot> Here is the list of issues you have selected."
"\nBot> We will look at them from the most distressful to the least distressful:")
HIGHLIGHTED = [("respiratory", 5),
                ("urinary",  8),
                ("sleeping", 2),
                ("chores", 1),
                ("caring-responsibilities", 4),
                ("relative-friend", 7),
                ("faith", 9),
                ("meaning", 11),
                ("regret", 9),
                ("partner", 3)]

def main(args):

    bot = _create_bot(args)
    _set_highlighted_issues(HIGHLIGHTED)
    issue_list = rivescriptmacrosmacros.get_all_issues(USERID)

    print _format_welcome_message(USERID, issue_list)
    micro_most_distressful = issue_list[0][0]
    macrotopic_for_most_distressful = topics_model.micro_to_macro[micro_most_distressful]
    print "micro most distressful: {}".format(micro_most_distressful)
    print "macro most distressful: {}".format(macrotopic_for_most_distressful)
    print "Bot>", bot.reply(USERID, "set global")
    print "Bot>", bot.reply(USERID, "discuss {}".format(macrotopic_for_most_distressful))
    print "Bot>", bot.reply(USERID, "discuss {}".format(micro_most_distressful)) #refactor issue_list to key-value pairs rather than couples

    stemmer = nltk.stem.snowball.SnowballStemmer('english')

    # chatloop:
    while True:
        msg = raw_input("You> ")
        if msg == "/q":
            quit()

        msg = stemmer.stem(msg)

        reply = bot.reply(USERID, msg)
        print "Bot>", reply

def _set_highlighted_issues(highlighted):
    for issue in highlighted:
        rivescriptmacrosmacros.set_issue("userid", *issue)

def _format_welcome_message(userid, issue_list):
    issue_list = rivescriptmacrosmacros.get_all_issues(USERID)

    output = "{}\n{}\n{}\n{}".format(WELCOME,
    CHECKLISTMSG,
    PREISSUES,
    rivescriptmacrosmacros.format_issue_list(issue_list))

    return output

def _create_bot(args):
    brain = _select_brain(args)

    bot = RiveScript()
    bot = _load_brain(bot, brain)
    bot.sort_replies()

    return bot

def _select_brain(args):
    if not args or len(args) <= 1:
        brain = "./brain"
    else:
        brain = args[1]
    return brain

def _load_brain(bot, brain):
    new_bot = bot

    if os.path.isdir(brain):
        new_bot.load_directory(brain)
    elif os.path.isfile(brain):
        new_bot.load_file(brain)
    else:
        raise ValueError("no directory or file found at specified filepath for "
                         "chatbot brain.")

    return new_bot

if __name__ == '__main__':
    import sys
    main(sys.argv)
