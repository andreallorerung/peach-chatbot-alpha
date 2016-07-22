from rivescript import RiveScript

# set_up
bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

def test_change_topic():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # perform:
    messages = ["desire to change topic", "I want to change the topic",
    "I wish to change the topic please", "desire discuss other",
    "I want to talk about something else"]

    for msg in messages:
        reply = bot.reply("localuser", msg)

        # test:
        assert "would you like to" in reply

def test_not_change_topic():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # perform:
    messages = ["do not desire to change topic", "I no want to change the topic",
    "I will nay wish to change the topic please"]

    for msg in messages:
        reply = bot.reply("localuser", msg)

        # test:
        assert "the topic then" in reply

def test_discuss():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # perform:
    messages = ["discuss physical", "want talk emotional",
    "wish discuss spiritual",
    "I wish to discuss my spiritual",
    "I wish to discuss my spiritual concerns please"]

    for msg in messages:
        reply = bot.reply("localuser", msg)

        # test:
        assert "talk about" in reply
        bot.reply("localuser", "set global")

def test_change_topic_and():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # perform:
    messages = ["do desire to change topic and discuss physical",
    "I want to change the topic and talk emotional problems",
    "I really want change the topic please and speak about family"]

    for msg in messages:
        reply = bot.reply("localuser", msg)

        # test:
        assert "'s talk about" in reply
