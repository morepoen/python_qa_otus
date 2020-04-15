import pytest


@pytest.mark.parametrize('x',
                         [1, 'r', ('a','e')])
def test_set_first(x):
    s = set()
    s.add(x)
    assert x in s


def test_set_two():
    s = {1, 4, 'd', 5}
    s.remove(4)
    assert 4 not in s


def test_set_three():
    a = {1, 2, 3}
    b = {4}
    a_and_b= a.union(b)
    assert 4 in a_and_b


def test_set_four():
    a = {1, 2, 3}
    b = {3, 4, 5}
    common_el = a.intersection(b)
    assert common_el == {3}


def test_set_five():
    a ={'a', 'b', 'c'}
    b = {'c', 'b', 'e'}
    diff = {'a', 'e'}
    symm_set = a.symmetric_difference(b)
    assert diff == symm_set
