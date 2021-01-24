import pytest

from unit.unit import prettify_string, check_numeric


@pytest.mark.parametrize('actual, expected', [
    ('SOLDIER', 'Soldier'),
    ('soldier\n', 'Soldier'),
    ('\tSoLdIeR', 'Soldier'),
    (' SoLdIeR ', 'Soldier'),
    ('Soldier', 'Soldier')
])
def test_prettify_string(actual, expected):
    assert prettify_string(actual) == expected


def test_prettify_string_exception():
    with pytest.raises(TypeError):
        prettify_string(10000)


@pytest.mark.parametrize('actual, expected', [
    (100, 100),
    (100.0, 100),
    ('100', 100)
])
def test_check_numeric(actual, expected):
    assert check_numeric(actual) == expected


@pytest.mark.parametrize('value, exception_type', [
    (-100, ValueError),
    (0, ValueError),
    ('error', ValueError),
    (dir, TypeError)
])
def test_check_numeric_exception(value, exception_type):
    with pytest.raises(exception_type):
        check_numeric(value)
