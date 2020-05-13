from dz7.config import ADMIN
from dz7.locators import AdminPageLocators


def test_product_page(browser):
    browser.get(ADMIN)
    browser.find_element(*AdminPageLocators.USERNAME)
    browser.find_element(*AdminPageLocators.PASSWORD)
    browser.find_element(*AdminPageLocators.LOGIN_BUTTON)
    browser.find_element(*AdminPageLocators.FORGOT_PASSWORD)
    browser.find_elements(*AdminPageLocators.FORM_TITLE)
