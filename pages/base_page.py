from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def visible_elements(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def visible_all_elements(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def present_elements(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def all_present_elements(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def not_visible_elements(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def click_element(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable())

    def scroll_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntiView;", element)