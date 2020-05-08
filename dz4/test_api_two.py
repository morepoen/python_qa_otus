import pytest


# tests for API https://www.openbrewerydb.org
# to run tests enter "pytest --url=https://api.openbrewerydb.org test_api_two.py" in bash


def test_get_all_breweries(api_client):
    res = api_client.get(path='/breweries')
    assert len(res.json()) > 0
    assert res.status_code < 400


@pytest.mark.parametrize('city_var_1, city_var_2', [('san_diego', 'san%20diego'),
                                                    ('lake_havasu_city', 'lake%20havasu%20city')])
def test_get_breweries_by_city(api_client, city_var_1, city_var_2):
    res_1 = api_client.get(path='//breweries?by_city={}'.format(city_var_1))
    res_2 = api_client.get(path='//breweries?by_city={}'.format(city_var_2))
    assert res_1.json() == res_2.json()


@pytest.mark.parametrize('search_term',
                         ['dog', 'brewing'])
def test_get_autocomplete(api_client, search_term):
    res = api_client.get(path='/breweries/autocomplete',
                         params=search_term)
    for item in res.json():
        assert search_term in item['name'].lower()


@pytest.mark.parametrize('brewery_id',
                         ['5', '123', '1111'])
def test_get_brewery(api_client, brewery_id):
    res = api_client.get(path='/breweries/{}'.format(id))
    assert int(brewery_id) == res.json()['id']


@pytest.mark.parametrize('brewery_type',
                         ['micro',
                          'regional',
                          'brewpub',
                          'large',
                          'planning',
                          'bar',
                          'contract',
                          'proprietor'])
def test_get_brewery_by_type(api_client, brewery_type):
    res = api_client.get(path='/breweries?by_type={}'.format(brewery_type))
    for item in res.json():
        assert brewery_type == item['brewery_type'].lower()
