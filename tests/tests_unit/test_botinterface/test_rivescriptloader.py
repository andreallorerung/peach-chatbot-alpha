from botinterface.rivescript_loader import loadBrain, _loadDirOrFile
import rivescript

def test_loaddirorfile():

    path_to_mockfile =     "tests/tests_unit/test_botinterface/mock_brain.rive" # ".\\tests\\tests_unit\\test_botinterface\mock_brain.rive"
    path_to_mockdir = "tests/tests_unit/test_botinterface/mock_brain_dir" #".\\tests\\tests_unit\\test_botinterface\mock_brain_dir"
    interpreter = _loadDirOrFile(rivescript.RiveScript(), path_to_mockfile)
    actual_bot_name_from_file = interpreter.get_variable("name")

    interpreter = _loadDirOrFile(rivescript.RiveScript(), path_to_mockdir)
    actual_bot_name_from_dir = interpreter.get_variable("name")

    expected_bot_name = "mocked"
    assert expected_bot_name == actual_bot_name_from_file
    assert expected_bot_name == actual_bot_name_from_dir

def test_loadbrain():

    logfile_to_verify_sorting = "tests/tests_unit/test_botinterface/rivescriptlog"
    path_to_mockfile = "tests/tests_unit/test_botinterface/mock_brain.rive" #".\\tests\\tests_unit\\test_botinterface\mock_brain.rive"
    interpreter = loadBrain(
                        rivescript.RiveScript(log=logfile_to_verify_sorting),
                        path_to_mockfile)

    with open(logfile_to_verify_sorting, 'r') as f:
        logfile_content = f.read()

    assert "Sorting triggers..." in logfile_content
    clear_logfile_content(logfile_to_verify_sorting)

def clear_logfile_content(filename):
    open(filename, 'w').close()
