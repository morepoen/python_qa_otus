import pytest


# tests for DOG API https://dog.ceo/dog-api
# to run tests enter "pytest --url=https://dog.ceo/api test_api_one.py" in bash


@pytest.mark.parametrize('breed',
                         ['hound', 'akita', 'cairn', 'bulldog'])
class TestGetBreedImages:
    def test_get_breed_images_success(self, api_client, breed):
        res = api_client.get(path='/breed/{}/images'.format(breed))
        assert res.json()['status'] == 'success'
        assert len(res.json()['message']) > 0

    def test_get_breed_images_corresponds_to_breed(self, api_client, breed):
        res = api_client.get(path='/breed/{}/images'.format(breed))
        for image_name in res.json()['message']:
            assert breed in image_name.lower()


def test_get_random_image(api_client):
    res = api_client.get(path='/breeds/image/random')
    assert res.json()['status'] == 'success'
    assert 'images' in res.json()['message']


@pytest.mark.parametrize('number',
                         ['1', '25', '49', '50'])
def test_get_random_images(api_client, number):
    res = api_client.get(path='/breeds/image/random/{}'.format(number))
    assert res.json()['status'] == 'success'
    assert len(res.json()['message']) == int(number)


@pytest.mark.parametrize('breed',
                         ['bulldog', 'poodle', 'terrier'])
def test_get_sub_breed_list(api_client, breed):
    res = api_client.get(path='/breed/{}/list'.format(breed))
    assert res.json()['status'] == 'success'
    assert len(res.json()['message']) > 0
