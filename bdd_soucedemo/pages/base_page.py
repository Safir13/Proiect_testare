from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from bdd_soucedemo.browser import Browser


class BasePage(Browser):
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def click_element(self, locator):
        self.find(locator).click()

    def wait_for_element(self, locator):
        return self.driver.find_element(locator).is_displayed()
