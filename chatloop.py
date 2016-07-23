import os
from botcontroller import macros
from rivescript import RiveScript

USERID = "localuser"
USERNAME = "Nic"
WELCOME = "Bot> Hello {}, welcome.".format(USERNAME)
CHECKLISTMSG = ("Bot> Let me check what your concerns are and we will go through "
"them briefly."
"\nBot> I would like you to gather a bit more information about them ahead of "
"your visit.")
PREISSUES = ("Bot> Here is the list of issues you have selected."
"\nBot> We will look at them from the most distressful to the least distressful:")

def main(args):

    if len(args) < 2:
        brain = "./brain"
    else:
        brain = args[1]

    bot = RiveScript()
    bot.load_directory(brain)
    bot.sort_replies()

    macros.set_issue("userid", "respiratory", 5)
    macros.set_issue("userid", "urinary", 8)
    macros.set_issue("userid", "sleeping", 9)
    macros.set_issue("userid", "chores", 4)
    macros.set_issue("userid", "relative-friend", 10)

    print(WELCOME)
    print(CHECKLISTMSG)
    issue_list = macros.get_all_issues(USERID)
    print(PREISSUES)
    print(macros.format_issue_list(issue_list))

    # macrotopic_for_most_distressful = macros.micro_to_macro[issue_list[0][0]]
    # print "Bot>", bot.reply(USERID, "discuss {}".format(macrotopic_for_most_distressful))
    # print "Bot>", bot.reply(USERID, "discuss issue_list[0][0]") #refactor issue_list to key-value pairs rather than couples

    while True:
        msg = raw_input("You> ")
        if msg == "/q":
            quit()

        reply = bot.reply(USERID, msg)
        print "Bot>", reply

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
