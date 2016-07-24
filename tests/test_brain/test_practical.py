from rivescript import RiveScript

# set_up
bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

def test_enter_practical():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # perform:
    messages = ["discuss practical"]

    for msg in messages:
        reply = bot.reply("localuser", msg)
        # test:
        assert "talk about practical" in reply

def test_responsibility():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I need to look after my children", "I care for my mother",
    "I have an obligation towards my partner's finanaces"]

    for msg in messages:
        # enter responsibilities discussion:
        msg = "discuss responsibility"
        bot.reply("localuser", msg)

        reply = bot.reply("localuser", msg)
        # test:
        assert "Do you believe this is relevant to your relationship with family or friends?" in reply

def test_responsibility_no():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # enter responsibilities discussion:
    msg = "discuss responsibility"
    bot.reply("localuser", msg)

    # enter responsibilities discussion:
    msg = "look after"
    bot.reply("localuser", msg)

    msg = "no"
    reply = bot.reply("localuser", msg)

    assert "Ok ..." in reply

def test_responsibility_yes():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # enter responsibilities discussion:
    msg = "discuss responsibility"
    bot.reply("localuser", msg)

    # enter responsibilities discussion:
    msg = "look after"
    bot.reply("localuser", msg)

    msg = "something something yes"
    reply = bot.reply("localuser", msg)

    assert "Adding topic or checking if already exists ..." in reply

def test_work():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I am underperforming at work because of stress","Something about work ...", "I am afraid to lose my job"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Are you afraid for your job security?",
        "Would you say this is also a money concern?",
        "How has your condition been affecting your work?"]

        for good_reply in good_replies:
            if good_reply == reply:
                found = True
                break

        assert found, reply

def test_education():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["School is not going well",
    "I am afraid I am going to lose my scholarship",
    "I do not see the point to going to university anymore"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["How is your condition affecting your performance?",
        "Are you concerned about how this may affect your future?",
        "Have you looked into equal opportunities policies your school may have for people affected by serious conditions?"]

        for good_reply in good_replies:
            if good_reply == reply:
                found = True
                break

        assert found, reply

def test_finance():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["money is tight", "I have some economic problems",
    "I received a tax bill I cannot pay"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Is your condition the primary reason for your financial problems?",
        "Are you receiving benefits?"]

        for good_reply in good_replies:
            if good_reply == reply:
                found = True
                break

        assert found, reply

def test_housing():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I have become homeless",
    "the other tenants are making my life difficult",
    "my landlord wants to evict me"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Are you afraid your housing situation is worsening?"]

        for good_reply in good_replies:
            if good_reply == reply:
                found = True
                break

        assert found, reply

def test_travel():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I want to travel abroad but I am worried about insurance",
    "I need to travel to visit my family"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Is travelling important for you at this time?"]

        for good_reply in good_replies:
            if good_reply == reply:
                found = True
                break

        assert found, reply

def test_transport():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["commuting is becoming impossible",
    "I cannot cycle anymore"]

    for msg in messages[:]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["Is the transportation issue affecting other areas of your life, such as your work or other duties?"]

        for good_reply in good_replies:
            if good_reply == reply:
                found = True
                break

        assert found, reply

def test_communication():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I find it difficult to talk on the phone to set up an appointment",]

    for msg in messages[:1]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["How would you prefer to communicate with the NHS?"]

        for good_reply in good_replies:
            if good_reply == reply:
                found = True
                break

        assert found, reply

def test_chores():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter practical topic:
    msg = "discuss practical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["I find it difficult to get dressed", "I cannot do housework anymore", "cooking has become a nightmare", "taking a bath is uncomfortable"]

    for msg in messages[:1]:

        reply = bot.reply("localuser", msg)
        # test:
        found = False
        good_replies = ["help you with"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply
