import pytest
import postprocess.message_decorator_single

RESOURCE = "http://cats.com"

REPLYSMOKING = "You can find more information here: {{ 'smoking' }}"
SIMPLETEMPLATE = "Oh look {{'interesting'}}"
ANOTHERTEMPLATE = "Let me tell you a {{'story'}} ... And they lived happily ever after"

MANYTEMPLATES = "There are three templates here: {{'more'}} {{'than'}} {{'can be handled'}}"
MANYKEYWORDS = "How many keywords are in here? {{ 'one' 'two' 'three' }}"
MANYTEMPLATESANDKEYWORDS = "Oh no! {{ 'this' 'means' }} {{ 'trouble' }}"

NOTEMPLATES = "Forgot to add templates"
NOKEYWORDS = "Here is an empty template: {{ }}"

messageDecorator = postprocess.message_decorator_single.MessageDecoratorSingle()

def test_init():
    assert hasattr(messageDecorator, "decorateMessageWith")

def test_decorateMessageWith():
    actual = messageDecorator.decorateMessageWith(REPLYSMOKING, RESOURCE)
    expected = "You can find more information here: {}".format(RESOURCE)

    assert expected == actual

def test_decorateMessageWith_another():
    actual = messageDecorator.decorateMessageWith(SIMPLETEMPLATE, RESOURCE)
    expected = "Oh look {}".format(RESOURCE)

    assert expected == actual

def test_decorateMessageWith_story():
    actual = messageDecorator.decorateMessageWith(ANOTHERTEMPLATE, RESOURCE)
    expected = "Let me tell you a {} ... And they lived happily ever after".format(RESOURCE)

    assert expected == actual

def test_decorateMessageWith_many_templates():
    actual = messageDecorator.decorateMessageWith(MANYTEMPLATES, RESOURCE)
    expected = "There are three templates here: " + RESOURCE + " {{'than'}} {{'can be handled'}}"# this is bad it should be fixed


    assert expected == actual

def test_decorateMessageWith_many_keywords():
    actual = messageDecorator.decorateMessageWith(MANYKEYWORDS, RESOURCE)
    expected = "How many keywords are in here? {}".format(RESOURCE)

    assert expected == actual

def test_decorateMessageWith_many_templates_keywords():
    actual = messageDecorator.decorateMessageWith(MANYTEMPLATESANDKEYWORDS, RESOURCE)
    expected = "Oh no! " + RESOURCE + " {{ 'trouble' }}"

    assert expected == actual

def test_decorateMessageWith_no_templates():
    actual = messageDecorator.decorateMessageWith(NOTEMPLATES, RESOURCE)
    expected = "Forgot to add templates"

    assert expected == actual

def test_replaceDelimitedSubstring_no_templates():
    actual = messageDecorator._replaceDelimitedSubstring(NOTEMPLATES)
    expected = "Forgot to add templates"

    assert expected == actual

def test_decorateMessageWith_no_keyword():
    actual = messageDecorator.decorateMessageWith(NOKEYWORDS, RESOURCE)
    expected = "Here is an empty template: {}".format(RESOURCE)

    assert expected == actual

def test_decorateMessageWith_empty_message():
    actual = messageDecorator.decorateMessageWith("", RESOURCE)
    expected = ""

    assert expected == actual

def test_decorateMessageWith_null_message():
    with pytest.raises(AttributeError):
        actual = messageDecorator.decorateMessageWith(None, RESOURCE)

def test_decorateMessageWith_empty_resource():
    actual = messageDecorator.decorateMessageWith(REPLYSMOKING, "")
    expected = "You can find more information here: {}".format("")

    assert expected == actual

def test_decorateMessageWith_null_resource():
    actual = messageDecorator.decorateMessageWith(REPLYSMOKING, None)
    expected = "You can find more information here: {}".format(None)

    assert expected == actual
