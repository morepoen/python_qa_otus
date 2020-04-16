import pytest


@pytest.mark.parametrize('x',
                         ['qer', '123', '435342'])
def test_str_one(x):
    my_str = x
    assert my_str.isalnum()


def test_str_two():
    my_str = '234'
    assert my_str.isdigit()


def test_str_three():
    my_str = 'cfg'
    assert my_str.isalpha()


def test_str_four():
    my_str = 'i am the best'
    exp_str = 'I Am The Best'
    titled_str = my_str.title()

    assert titled_str == exp_str


def test_str_five():
    my_str = 'a b c'
    assert my_str.startswith('a')