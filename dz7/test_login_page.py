from dz7.config import LOGIN
from dz7.locators import LoginPageLocators


def test_login_page(browser):
    browser.get(LOGIN)
    browser.find_element(*LoginPageLocators.CONTINUE_BUTTON)
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
    browser.find_element(*LoginPageLocators.EMAIL_FIELD)
    browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
    browser.find_element(*LoginPageLocators.SIDEBAR)
