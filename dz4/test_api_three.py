import random

import pytest


# tests for API https://jsonplaceholder.typicode.com
# to run tests enter "pytest --url=https://jsonplaceholder.typicode.com test_api_three.py" in bash


@pytest.mark.parametrize('input_title, output_title',
                         [('bla', 'bla'),
                          ('111', '111'),
                          ('@', '@')])
@pytest.mark.parametrize('input_body, output_body',
                         [('bla', 'bla'),
                          ('111', '111'),
                          ('@', '@')])
@pytest.mark.parametrize('input_id, output_id',
                         [('0', '0'),
                          ('111', '111'),
                          ('-1', '-1'),
                          ('99999', '99999')])
def test_crate_resource(api_client,
                        input_title,
                        output_title,
                        input_body,
                        output_body,
                        input_id,
                        output_id):
    res = api_client.post(path='/posts',
                          data={'title': input_title,
                                'body': input_body,
                                'userId': input_id},
                          headers={"Content-type": "application/json; charset=UTF-8"})
    res_json = res.json()
    assert res_json['title'] == output_title
    assert res_json['body'] == output_body
    assert res_json['userId'] == output_id


def test_update_post(api_client):
    res = api_client.put(path='/posts/1',
                         data={'id': 1,
                               'title': 'input_title',
                               'body': 'input_body',
                               'userId': 'input_id'},
                         headers={"Content-type": "application/json; charset=UTF-8"})
    assert res.json()['id'] == 1


def test_get_all_resources(api_client):
    res = api_client.post(path='/posts')
    assert res.status_code < 400
    assert len(res.json()) > 0


@pytest.mark.parametrize('album_id, res_album_id',
                         [(1, 1),
                          (15, 15),
                          (99, 99)])
def test_api_album_nesting(api_client,
                             album_id,
                             res_album_id):
    res = api_client.get(path="/photos",
                         params={'albumId': album_id})
    rand_album_num = random.randint(1, 49)
    assert len(res.json()) > 0
    assert res.json()[rand_album_num]['albumId'] == res_album_id


def test_api_delete(api_client):
    res = api_client.delete(path="/posts/52")
    assert res.status_code == 200
