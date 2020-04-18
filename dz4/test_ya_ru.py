import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url",
                     action="store",
                     default="https://ya.ru",
                     help="This is request url")

    parser.addoption("--status_code",
                     action="store",
                     default="200",
                     help="This is expected status code")


@pytest.fixture()
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def get_status_code(request):
    return request.config.getoption("--status_code")


def test_ya(get_url,
            get_status_code):
    res = requests.get(get_url)
    assert res.status_code == get_status_code
