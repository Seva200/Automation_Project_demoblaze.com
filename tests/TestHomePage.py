import time

from selenium.webdriver.common.by import By
from src.utils.DriverSetUp import DriverSetUp
import allure
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

    def test_left_arrow_btn(self, driver):
        self.home_page.left_arrow_click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li:nth-child(3)") \
                   .get_attribute("class") == "active"

    def test_left_indicator(self, driver):
        self.home_page.left_indicator_click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li:nth-child(1)") \
                   .get_attribute("class") == "active"

    def test_middle_indicator(self, driver):
        self.home_page.middle_indicator_click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li.active") \
                   .get_attribute("class") == "active"
    def test_right_indicator(self, driver):
        self.home_page.right_indicator_click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li:nth-child(3)") \
                   .get_attribute("class") == "active"

# Body
    def test_categories_btn(self, driver):
        self.home_page.categories_btn_click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#cat").get_attribute("text") == "CATEGORIES"

    def test_phones_btn(self, driver):
        self.home_page.phones_btn_click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#itemc").get_attribute("text") == "Phones"

    def test_laptops_btn(self, driver):
        self.home_page.laptops_btn_click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#itemc").get_attribute("text") == "Laptops"
    def test_monitors_btn(self, driver):
        self.home_page.monitors_btn_click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#itemc").get_attribute("text") == "Monitors"
    def test_item_btn(self, driver):
        self.home_page.item_click()
        assert self.driver.current_url == "https://www.demoblaze.com/prod.html?idp_=1"
    
