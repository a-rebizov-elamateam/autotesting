from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "PRODUCT NAME is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "PRODUCT PRICE is not presented"

    def put_in_the_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.PRODUCT_PUT_BASKET)
        basket_button.click()


    def success_product_add(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_MESSAGE_SUCCESS), "PRODUCT_MESSAGE_SUCCESS is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_message_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_NAME).text
        assert product_name == product_message_name, "No product name in the message"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_message_price = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_PRICE).text
        assert product_price == product_message_price, "product_price != product_message_price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_MESSAGE_SUCCESS), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_MESSAGE_SUCCESS), \
            "Success message is disappeared, but should not be"
