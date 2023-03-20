import time

from selenium.webdriver.common.by import By
from src.utils.DriverSetUp import DriverSetUp

class TestHomePage(DriverSetUp):

# Header
    def test_home_btn(self, driver):
        self.home_page.home_btn_click()
        assert driver.current_url == "https://www.demoblaze.com/index.html"
    def test_contact_btn(self, driver):
        self.home_page.contact_btn_click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR, "#exampleModal").get_attribute("class") == "modal fade show"
    def test_about_us_btn(self, driver):
        self.home_page.about_us_btn_click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR, "#videoModal").get_attribute("class") == "modal fade show"
    def test_cart_btn(self, driver):
        self.home_page.cart_btn_click()
        assert driver.current_url == "https://www.demoblaze.com/cart.html"
    def test_login_btn(self, driver):
        self.home_page.login_btn_click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR, "#logInModal").get_attribute("class") == "modal fade show"
    def test_logout_btn(self, driver):
        self.home_page.logout_btn_click('User30', 'user123')
        assert driver.current_url == "https://www.demoblaze.com/index.html"
    def test_logo_btn(self, driver):
        self.home_page.logo_btn_click()
        assert driver.current_url == "https://www.demoblaze.com/index.html"

# Slide Show
    def test_right_arrow_btn(self, driver):
        self.home_page.right_arrow_click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li.active")\
                   .get_attribute("class") == "active"

    