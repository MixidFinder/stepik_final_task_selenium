import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize(
    "promo_offer",
    [
        pytest.param(i, marks=pytest.mark.xfail(i == 7, reason="No one will fix it"))
        for i in range(10)
    ],
)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.test_add_product_to_cart_and_verify()
