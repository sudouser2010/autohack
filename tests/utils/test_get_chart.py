from specific_import import import_file

autohack = import_file('../../src/autohack')
Colors = autohack.Colors


def test_get_chart_for_normal_conditions():
    """
        In this circumstance, the chart will consist of
        a combination of ▯ and the ' ' symbols.
    """
    value = 4
    max_value = 10
    size = 30

    scaled_value = int(value / max_value * size)
    expected_chart_text = (
        f'|{Colors.GREEN}{Colors.BOLD}{"▯" * scaled_value}{Colors.END}'
        f'{Colors.CYAN}({value} seconds){Colors.END}'
        f'{" " * (size - scaled_value)}|{Colors.CYAN}({max_value} seconds){Colors.END}'
    )

    chart_text = autohack.Utils.get_chart(
        value=value,
        max_value=max_value,
        size=size,
    )
    assert chart_text == expected_chart_text, 'Unexpected chart text'


def test_get_chart_when_value_is_larger_than_max():
    """
        In this circumstance, when the value is larger than the max_value,
        the chart will be filled with the ▯ symbol.
    """
    value = 400
    max_value = 10
    size = 30

    expected_chart_text = (
        f'|{Colors.GREEN}{Colors.BOLD}{"▯" * size}{Colors.END}'
        f'{Colors.CYAN}({max_value} seconds){Colors.END}'
        f'|{Colors.CYAN}({max_value} seconds){Colors.END}'
    )

    chart_text = autohack.Utils.get_chart(
        value=value,
        max_value=max_value,
        size=size,
    )
    assert chart_text == expected_chart_text, 'Unexpected chart text'


def test_get_chart_when_value_is_negative():
    """
        In this circumstance, when the value is negative,
        the chart will be filled with the ' ' symbol.
    """
    value = -400
    max_value = 10
    size = 30

    expected_chart_text = (
        f'|{Colors.GREEN}{Colors.BOLD}{Colors.END}'
        f'{Colors.CYAN}(0 seconds){Colors.END}'
        f'{" " * size}|{Colors.CYAN}({max_value} seconds){Colors.END}'
    )

    chart_text = autohack.Utils.get_chart(
        value=value,
        max_value=max_value,
        size=size,
    )
    assert chart_text == expected_chart_text, 'Unexpected chart text'
