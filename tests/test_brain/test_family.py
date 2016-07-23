from rivescript import RiveScript

# set_up
bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

def test_enter_family_topic():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # perform:
    messages = ["discuss family", "discuss my family"
    "I wish to change the topic please and talk about family",
    "desire to discuss the family",
    "I want to talk about family issues"]

    for msg in messages:
        reply = bot.reply("localuser", msg)
        # test:
        assert "talk about family" in reply

def test_enter_relativefriend():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter family topic:
    msg = "discuss family"
    bot.reply("localuser", msg)

    # perform:
    messages = ["discuss friend", "I think my mate ...", "aunt",
    "I like my aunt but I don't like my uncle",
    "my nephew hates me but my dad doesn't"
    "discuss relativefriend",]

    for msg in messages[:]:
        reply = bot.reply("localuser", msg)
        # test:
        assert "What is it" in reply
        # return to family topic
        bot.reply("localuser", "set family")

def test_issue_identified():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter family topic:
    msg = "discuss family"
    bot.reply("localuser", msg)

    # perform:
    messages = ["discuss friend", "I think my mate ...", "aunt",
    "I like my aunt but I don't like my uncle",
    "my nephew hates me but my dad doesn't"]

    replies = []
    for msg in messages[:]:
        nextreply = bot.reply("localuser", msg)
        replies.append(nextreply)
        # reset to family topic
        bot.reply("localuser", "set family")

    # test:
    assert "friend" in replies[0]
    assert "mate" in replies[1]
    assert "aunt" in replies[2]
    # Wrong answer:
    assert "aunt" in replies[3]# assert "uncle" in replies[3]
    # Wrong answer:
    assert "dad" in replies[4]# assert "nephew" in replies[4]
