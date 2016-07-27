from rivescript import RiveScript

# set_up
bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

def test_enter_emotional():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # perform:
    messages = ["discuss emotional"]

    for msg in messages:
        reply = bot.reply("localuser", msg)
        # test:
        assert "talk about emotional" in reply

def test_planning_interests():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss emotional"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I do not want to make plans anymore", "I used to work on my projects I don't anymore", "I do not enjoy sport", "I used to have hobbies"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Do you believe your loss of interest may be related to a loss of meaning or purpose?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_expressing():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss emotional"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I find difficulties voicing my state", "I never want to show how I feel", "conveying my emotions has always been difficult"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Do you feel you have problems expressing yourself in general or in particular situatons/with particular people?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_anger():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss emotional"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I throw tantrums for no reason","I am disappointed with my parents behaviour", "I lose my temper more easily now"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["What is it that frustrates you?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_guilt():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss emotional"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I feel guilty", "I had a lapse"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Does your guilt arises from something you take responsibility for?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_loneliness():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss emotional"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I am so lonely", "I feel alienated",
    "none of my friends are there for me"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Have you lost contact with friends and family?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_depression():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss emotional"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I never felt down for this long before",
    "it's like I'm permanently unhappy",
    "I believe I am depressed"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Do you feel there is something other than your condition causing you to feel this way?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_worry():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss emotional"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I am afraid of what will happen next",
    "I am anxious for the future of those I will be leaving behind",
    "I suffer from anxiety and panic attacks"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Have you expressed these feelings to anyone before?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply
