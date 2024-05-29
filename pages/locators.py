from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT_REPEAT = (
        By.CSS_SELECTOR,
        "#id_registration-password2",
    )
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
    BOOK_TITLE = (
        By.CSS_SELECTOR,
        "#content_inner > article > div.row > div.col-sm-6.product_main > h1",
    )
    BOOK_TITLE_IN_CART = (
        By.CSS_SELECTOR,
        "#messages > div:nth-child(1) > div > strong",
    )
    BOOK_PRICE = (
        By.CSS_SELECTOR,
        "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color",
    )
    CART_PRICE = (
        By.CSS_SELECTOR,
        "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong",
    )
    ALERT_SUCCES = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (
        By.CSS_SELECTOR,
        "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a",
    )
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
