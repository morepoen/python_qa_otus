from selenium.webdriver.common.by import By


class MainPageLocators:
    NAVBAR = (By.CSS_SELECTOR, '.collapse.navbar-collapse.navbar-ex1-collapse')
    SEARCH = (By.XPATH, '//div[@id="search"]')
    CART = (By.CSS_SELECTOR, '#cart')
    SWIPER = (By.CSS_SELECTOR, '.swiper-container.swiper-container-horizontal')
    PRODUCTS = (By.CSS_SELECTOR, '.product-thumb.transition')


class CatalogPageLocators:
    HEADER = (By.CSS_SELECTOR, '#top')
    SIDEBAR = (By.CSS_SELECTOR, '#column-left')
    CURRENT_CATEGORY = (By.XPATH, '//h2')
    CATEGORY_DESCRIPTION = (By.CSS_SELECTOR, '.col-sm-10')
    PRODUCTS = (By.CSS_SELECTOR, '.product-thumb')


class LoginPageLocators:
    CONTINUE_BUTTON = (By.XPATH, '//div[@class="well"]/a[contains(@href, "register")]')


