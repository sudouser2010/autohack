import multiprocessing

from specific_import import import_file

autohack = import_file('../../src/autohack')


def test_get_lock():
    """
    Verify that get_lock returns the expected Lock object
    :return:
    """
    process_lock = autohack.Utils.get_lock()
    assert type(process_lock) is multiprocessing.synchronize.Lock
