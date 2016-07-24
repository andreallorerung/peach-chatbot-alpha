from rivescript import RiveScript

# set_up
bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

def test_enter_physical_topic():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # perform:
    messages = ["discuss physical", "speak my physical problem"
    "I wish to change the topic talk about physical health problems",
    "wanna discuss the physical",
    "discuss physical issues"]

    for msg in messages:
        reply = bot.reply("localuser", msg)
        # test:
        assert "talk about physical" in reply

def test_problem_questions():
    # enter global topic:
    msg = "set global"
    bot.reply("localuser", msg)

    # enter physical topic:
    msg = "discuss physical"
    bot.reply("localuser", msg)

    # perform:
    messages = ["my breathing problem ...", "It affects ...", "There's also ...",
    "Ok", "this should fail"]

    for msg in messages[:4]:
        reply = bot.reply("localuser", msg)
        # test:
        assert "problem" in reply
