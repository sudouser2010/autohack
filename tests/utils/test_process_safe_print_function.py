from unittest import mock

from specific_import import import_file

autohack = import_file('../../src/autohack')


@mock.patch('builtins.print')
@mock.patch.object(autohack.Utils, 'get_lock')
def test_process_safe_print(mock_get_lock, mock_print):
    """
    Verifies the process safe print:
        acquires the lock
        prints
        releases the lock

    :param mock_get_lock:
    :return:
    """
    process_lock = mock_get_lock.return_value
    expected_string = 'Placeholder Output'

    mock_print.assert_not_called()
    assert process_lock.acquire.call_count == 0, 'Lock acquire should not be called yet'
    assert process_lock.release.call_count == 0, 'Lock release should not be called yet'

    autohack.Utils.process_safe_print('Placeholder Output')

    mock_print.assert_called_with(expected_string)
    assert process_lock.acquire.call_count == 1, 'Lock acquire should be called'
    assert process_lock.release.call_count == 1, 'Lock release should be called'
