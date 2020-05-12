from selenium.webdriver.common.by import By


class MainPageLocators:
    NAVBAR = (By.CSS_SELECTOR, '.collapse.navbar-collapse.navbar-ex1-collapse')
    SEARCH = (By.XPATH, '//div[@id="search"]')
    CART = (By.CSS_SELECTOR, '#cart')
    SWIPER = (By.CSS_SELECTOR, '.swiper-container.swiper-container-horizontal')
    PRODUCTS = (By.CSS_SELECTOR, '.product-thumb.transition')


class CatalogPageLocators:
    SIDEBAR = (By.CSS_SELECTOR, '#column-left')

