from pages.base_page import BasePage
from pages.locators import ProductPageLotators


class ProductPage(BasePage):
    def test_add_product_to_cart_and_verify(self):
        self.should_be_add_product_to_cart_btn()
        self.add_product_to_cart()
        self.solve_quiz_and_get_code()
        self.should_be_alert_success()
        self.should_equals_cart_and_book_price()
        self.should_equals_book_title_and_cart_title()

    def add_product_to_cart(self):
        add_product_btn = self.browser.find_element(
            *ProductPageLotators.ADD_TO_CART_BTN
        )
        add_product_btn.click()

    def should_be_add_product_to_cart_btn(self):
        assert self.is_element_present(
            *ProductPageLotators.ADD_TO_CART_BTN
        ), "Add product to cart btn not presented"

    def should_be_alert_success(self):
        assert self.is_element_present(
            *ProductPageLotators.ALERT_SUCCES
        ), "Succes alert not presented"

    def should_equals_cart_and_book_price(self):
        book_price = self.browser.find_element(*ProductPageLotators.BOOK_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLotators.CART_PRICE).text
        assert (
            book_price == cart_price
        ), f"Incorrect price in cart: {cart_price} in book price: {book_price}"

    def should_equals_book_title_and_cart_title(self):
        book_title = self.browser.find_element(*ProductPageLotators.BOOK_TITLE).text
        book_title__in_cart = self.browser.find_element(
            *ProductPageLotators.BOOK_TITLE_IN_CART
        ).text
        assert (
            book_title == book_title__in_cart
        ), f"Incorrect book title in book: {book_title} in cart: {book_title__in_cart}"
