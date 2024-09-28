from specific_import import import_file

autohack = import_file('../../src/autohack')


def test_extract_matching_string_when_match_is_present():
    needle = 'foo'
    haystack = 'hello-world foo-bar'
    result = autohack.Utils.extract_matching_string(needle, haystack)
    assert result == haystack, 'Unexpected Result'


def test_extract_matching_string_when_match_is_not_present():
    needle = 'foo'
    haystack = 'hello-world zoo-bar'
    result = autohack.Utils.extract_matching_string(needle, haystack)
    assert result is None, 'Unexpected Result'
