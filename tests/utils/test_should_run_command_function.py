from unittest import mock

from specific_import import import_file

autohack = import_file('../../src/autohack')


def test_should_run_command_when_command_output_file_is_none():
    """
    When command_output_file is preexisting,
    the function should return True.
    :return:
    """
    result = autohack.Utils.should_run_command(command_output_file=None)
    assert result is True


@mock.patch('os.path.isfile')
def test_should_run_command_when_command_output_file_is_already_exists(mocked_isfile):
    """
    When command_output_file is preexisting,
    the function should return False.
    :return:
    """
    mocked_isfile.return_value = True
    result = autohack.Utils.should_run_command(
        command_output_file='some_preexisting_output_file'
    )
    assert result is False


@mock.patch('os.path.isfile')
def test_should_run_command_when_command_output_file_does_not_exists(mocked_isfile):
    """
    When command_output_file is not preexisting,
    the function should return True.
    :return:
    """
    mocked_isfile.return_value = False
    result = autohack.Utils.should_run_command(
        command_output_file='some_non_preexisting_output_file'
    )
    assert result is True
