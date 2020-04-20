import requests


def test_ya(get_url,
            get_status_code):
    res = requests.get(get_url)
    assert res.status_code == int(get_status_code)
