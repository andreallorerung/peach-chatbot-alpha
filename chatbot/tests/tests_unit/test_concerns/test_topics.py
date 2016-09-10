from concerns import topics

def test_allTopicsMapped():
    checkTopicsAreIn(topics.PHYSICAL1, "physical")
    checkTopicsAreIn(topics.PHYSICAL2, "physical")
    checkTopicsAreIn(topics.PHYSICAL3, "physical")
    checkTopicsAreIn(topics.PHYSICAL4, "physical")
    checkTopicsAreIn(topics.PRACTICAL1, "practical")
    checkTopicsAreIn(topics.PRACTICAL2, "practical")
    checkTopicsAreIn(topics.FAMILY, "family")
    checkTopicsAreIn(topics.EMOTIONAL1, "emotional")
    checkTopicsAreIn(topics.EMOTIONAL2, "emotional")
    checkTopicsAreIn(topics.SPIRITUAL, "spiritual")

def checkTopicsAreIn(microTopicsList, macroTopic):
    for microTopic in microTopicsList:
        expectedMacroTopic = macroTopic
        actualMacroTopic = topics.macrotopicFor[microTopic]

        assert expectedMacroTopic == actualMacroTopic
