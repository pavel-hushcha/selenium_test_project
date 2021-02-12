from .pages.product_page import ProductPage
from .pages.main_page import MainPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    add_product = ProductPage(browser, browser.current_url)
    add_product.add_product_to_basket()
