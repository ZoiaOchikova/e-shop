from core.web_site import WebSite
from iherb_selenium.iherb_settings import IherbSettings


class IherbTest:

    driver = None
    browser = None
    number_of_items = 2

    def setup_class(self):
        self.driver = WebSite()
        self.driver.init()
        self.browser = self.driver.browser
        self.site_inst = IherbSettings(self.browser)

    def teardown_class(self):
        self.driver.deinit()

    def test_add_two_items_to_cart(self):
        """Verifies the ability to add two most expensive items to the shopping cart from the category
        """
        self.site_inst.click_supplements_link()
        self.site_inst.click_price_high_to_low()
        self.site_inst.click_add_to_cart_buttons(self.number_of_items)
        actual_number_of_items = self.site_inst.get_cart_quantity(self.number_of_items)
        assert self.number_of_items == actual_number_of_items, \
            'Actual number of items (%i) is not equal to expected(%i)' \
            % (actual_number_of_items, self.number_of_items)
