from specific_import import import_file

autohack = import_file('../../src/autohack')


def test_alpha_to_int_with_a_string_number():
    """
    Verify a string-number is converted to a number
    """
    result = autohack.Utils.alpha_to_int('22')
    assert result == 22, 'Unexpected Result'


def test_alpha_to_int_with_a_string():
    """
    Verify a string is not converted to a number
    """
    result = autohack.Utils.alpha_to_int('abc')
    assert result == 'abc', 'Unexpected Result'
