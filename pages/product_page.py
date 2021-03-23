from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        name_good = self.browser.find_element(*ProductPageLocators.NAME_GOOD).text
        price_good = self.browser.find_element(*ProductPageLocators.PRICE_GOOD).text
        name_good_in_basket = self.browser.find_element(*ProductPageLocators.NAME_GOOD_BASKET).text
        price_good_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_GOOD_BASKET).text
        assert name_good == name_good_in_basket, "This product isn't in basket"
        assert price_good == price_good_in_basket, "The basket amount is not equal price of product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),  "Success message is presented," \
                                                                                   " but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
