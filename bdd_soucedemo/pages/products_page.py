import selenium.webdriver.common.by
from selenium.webdriver.support.select import Select

from bdd_soucedemo.pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCTS_PAGE_TITLE = (selenium.webdriver.common.by.By.CLASS_NAME, "title")
    PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"

    ITEMS_NAME = (selenium.webdriver.common.by.By.CLASS_NAME, "inventory_item_name")
    ITEMS_PRICE= (selenium.webdriver.common.by.By.CLASS_NAME, "inventory_item_price")
    DROPDOWN_SORT = (selenium.webdriver.common.by.By.CLASS_NAME, "product_sort_container")

    ADD_TO_CART_BACKPACK = (selenium.webdriver.common.by.By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (selenium.webdriver.common.by.By.ID, "remove-sauce-labs-backpack")
    CART_ITEM = (selenium.webdriver.common.by.By.CLASS_NAME, "shopping_cart_badge")

    def verify_products_page_title(self, title):
        return self.find(self.PRODUCTS_PAGE_TITLE).text == title

    def verify_current_url(self, expected_url):
        return self.driver.current_url == expected_url

    def verify_product_names_sorted_alphabetically(self):
        list_all_items_elements = self.find_all(self.ITEMS_NAME)

        list_all_items_names = []
        for element in list_all_items_elements:
            list_all_items_names.append(element.text)

        assert list_all_items_names == sorted(list_all_items_names), f"The list is not sorted as expected: {list_all_items_names}"

    def select_dropdown_item(self, text):
        dropdown = Select(self.find(self.DROPDOWN_SORT))
        dropdown.select_by_visible_text(text)

    def verify_product_price_sorted_low_to_high(self):
        list_all_items_elements = self.find_all(self.ITEMS_PRICE)
        list_all_items_price = []
        for element in list_all_items_elements:
            price = element.text.replace("$","")
            list_all_items_price.append(float(price))
        assert list_all_items_price == sorted(list_all_items_price), f"The list is not sorted as expected: {list_all_items_price}"

    def click_add_backpack_button(self):
        self.click_element(self.ADD_TO_CART_BACKPACK)

    def verify_remove_button_is_visible(self):
        assert self.find(self.REMOVE_BACKPACK).is_displayed()

    def verify_cart_item_number(self, number):
        assert self.find(self.CART_ITEM).text == number