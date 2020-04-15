import pytest


def test_dict_one():
    my_dict = {'a': 'b',
               'c': 'd'}
    my_dict.clear()
    assert my_dict == {}


@pytest.mark.parametrize('x',
                         ['q', 'w', 'e'])
def test_dict_two(x):
    dict_1 = {x: '1',
              'a': 2,
              'b': 3}
    dict_2 = dict_1.copy()
    assert dict_1 == dict_2


def test_dict_three():
    my_dict = {'a': 'b',
               'c': 'd'}
    exp_val = 'b'
    assert my_dict.get('a') == exp_val


def test_dict_four():
    my_dict = {'a': 'b',
               'c': 'd'}
    assert my_dict.get('r') is None


def test_dict_five():
    my_dict = {'a': 'b'}
    del my_dict['a']
    assert my_dict == {}

