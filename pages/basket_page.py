from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEM
        ), "There are items in the basket"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_TEXT
        ), "Empty basket text is not presented"
