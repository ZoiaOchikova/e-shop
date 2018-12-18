from selenium import webdriver

from iherb_selenium.iherb_settings import IherbSettings
from source.get_properties import GetProperties


class WebSite:

    def __init__(self):
        self.browser = None
        self.properties = GetProperties.get_inst()
        self.properties.get_properties()

    def init(self):
        self.browser = webdriver.Chrome(executable_path=self.properties.get_property('driver_folder'))
        self.browser.implicitly_wait(self.properties.get_property('timeout_wait_pageLoad'))
        self.browser.maximize_window()
        self.browser.get(IherbSettings.home_page)

    def deinit(self):
        self.browser.quit()
