from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from src.locators.AboutUsLocators import aboutlocs

class AboutUsModal:

    def __init__(self, driver):
        self.driver = driver

    def wdw_locator(self, locator):
        return WDW(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def play_btn_click(self):
        AboutUsModal.wdw_locator(self, aboutlocs['Play_btn']).click()
    def X_btn_click(self):
        AboutUsModal.wdw_locator(self, aboutlocs['X_btn']).click()
    def close_btn_click(self):
        AboutUsModal.wdw_locator(self, aboutlocs['Close_btn']).click()
