import pytest


@pytest.mark.parametrize('b',
                         [7, 'fff', ('df', 66)])
def test_list_one(b):
    a = ['gv']
    a.append(b)
    assert b in a


def test_list_two():
    a = []
    len_a = len(a)
    a.append('dfvdf')
    assert len(a)>len_a


def test_list_three():
    a = ['bla', 1, 10,('s','d')]
    len_a = len(a)
    a.pop()
    assert len_a > len(a)


def test_list_four():
    a = ['bla', 1, 10, ('s', 'd')]
    third_item = a[2]
    a.pop(2)
    assert third_item not in a


def test_list_five():
    a = ['bla', 1, 10, ('s', 'd')]
    insert_item = 9
    a.insert (1, insert_item)
    assert a[1] == insert_item
