import os
from concerns import topics
from concerns import rivescriptmacros
import rivescript

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
    bot = rivescript.RiveScript()
    bot.load_directory("./brain")
    bot.sort_replies()
    # chatloop:
    while True:
        msg = raw_input("You> ")
        if msg == "/q":
            quit()

        reply = bot.reply(USERID, msg)
        print "Bot>", reply

def _set_highlighted_issues(highlighted):
    for issue in highlighted:
        rivescriptmacrosmacros.setIssue("userid", *issue)

def _format_welcome_message(userid, issue_list):
    issue_list = rivescriptmacrosmacros.get_all_issues(USERID)

    output = "{}\n{}\n{}\n{}".format(WELCOME,
    CHECKLISTMSG,
    PREISSUES,
    rivescriptmacrosmacros.format_issue_list(issue_list))

    return output

def _create_bot(args):
    brain = _select_brain(args)

    bot = bot_builder.build()
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
