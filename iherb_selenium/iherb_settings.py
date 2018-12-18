from selenium.common.exceptions import WebDriverException
from iherb_selenium.waiter import waiter_decorator
from source.get_properties import GetProperties


class IherbSettings:
    properties = GetProperties.get_inst()
    properties.get_properties()
    home_page = properties.get_property('domain')

    search_field_id = 'txtSearch'
    search_button_id = 'searchBtn'
    supplements_link_selector = 'a[data-ga-event-action=\"header-supplements\"]'
    price_high_to_low_selector = 'div.col-lg-4.panel-content.sort-by' \
                                 ' select.dropdown-sort' \
                                 ' option:nth-child(5)'
    add_to_cart_button_name = 'AddToCart'
    cart_quantity_id = 'cart-qty'

    def __init__(self, browser):
        self.browser = browser

    def get_search_field(self):
        return self.browser.find_element_by_id(self.search_field_id)

    def send_keys_to_search_filed(self, msg):
        self.get_search_field().send_keys(msg)

    def click_search_button(self):
        self.browser.find_element_by_id(self.search_button_id).click()

    def click_supplements_link(self):
        self.browser.find_element_by_css_selector(self.supplements_link_selector).click()

    def click_price_high_to_low(self):
        self.browser.find_element_by_css_selector(self.price_high_to_low_selector).click()

    def click_add_to_cart_buttons(self, number_of_items):
        for i in range(number_of_items):
            self.click_add_to_cart_button(i)

    @waiter_decorator
    def click_add_to_cart_button(self, number_of_item):
        try:
            items = self.browser.find_elements_by_name(self.add_to_cart_button_name)
            items[number_of_item].click()
        except WebDriverException:
            return False
        else:
            return True

    @waiter_decorator
    def check_cart_quantity(self, expected_number_of_items):
        cart_quantity = int(self.browser.find_element_by_id(self.cart_quantity_id).text)
        if expected_number_of_items != cart_quantity:
            return False
        else:
            return True

    def get_cart_quantity(self, expected_number_of_items):
        self.check_cart_quantity(expected_number_of_items)
        return int(self.browser.find_element_by_id(self.cart_quantity_id).text)
