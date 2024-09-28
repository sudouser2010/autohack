from specific_import import import_file

autohack = import_file('../../src/autohack')


def test_get_site_packages():
    """
    Verify that get_site_packages returns a list of strings
    """
    site_packages = autohack.Utils.get_site_packages()
    assert type(site_packages) is list
