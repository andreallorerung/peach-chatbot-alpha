from rivescript import RiveScript

# set_up
bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

def test_faith():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss spiritual"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I don't know what to believe anymore",
    "I have lost faith", "I stopped going to church"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Have you spoken to anyone in your spiritual community about this?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_meaning():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss spiritual"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I don't believe there is any meaning to life",
    "I don't think I value my life",
    "what is the purpose of it all?"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Do you feel this lack of meaning is due to not having or being able to pursue goals or objectives in your life?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_regret():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss spiritual"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I believe I have been immoral",
    "I have have been evil and regret it",
    "I worry for my conscience",
    "I wish I could go back"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Do you believe there is any way for you to make up for your mistakes?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply
