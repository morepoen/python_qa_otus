from dz7.config import CATALOG
from dz7.locators import MainPageLocators


def test_catalog_page(browser):
    browser.get(CATALOG)
    browser.find_element(*MainPageLocators.CART)
    browser.find_element(*MainPageLocators.NAVBAR)
    browser.find_element(*MainPageLocators.SEARCH)
    browser.find_element(*MainPageLocators.SWIPER)