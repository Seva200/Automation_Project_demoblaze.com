import time

from selenium.webdriver.common.by import By
from src.utils.DriverSetUp import DriverSetUp
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec

class TestContactModal(DriverSetUp):

    def test_sending_valid_message(self, driver):
        self.home_page.contact_btn_click()
        self.contact_modal.set_email("jhon34@mail.com")
        self.contact_modal.set_name("Jhon")
        self.contact_modal.set_message("Hello world!")
        self.contact_modal.send_message_click()
        wdw(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == "Thanks for the message!!"
        alert.accept()

    def test_sending_invalid_email_message(self, driver):
        self.home_page.contact_btn_click()
        self.contact_modal.set_email("dseg123")
        self.contact_modal.set_name("Jhon")
        self.contact_modal.set_message("Hello world!")
        self.contact_modal.send_message_click()
        wdw(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text != "Thanks for the message!!"
        alert.accept()

    def test_sending_invalid_name_message(self, driver):
        self.home_page.contact_btn_click()
        self.contact_modal.set_email("jhon34@mail.com")
        self.contact_modal.set_name(1234)
        self.contact_modal.set_message("Hello world!")
        self.contact_modal.send_message_click()
        wdw(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text != "Thanks for the message!!"
        alert.accept()

    def test_sending_invalid_message_without_char(self, driver):
        self.home_page.contact_btn_click()
        self.contact_modal.send_message_click()
        wdw(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text != "Thanks for the message!!"
        alert.accept()

    def test_name_length_more_than_10_char(self, driver):
        self.home_page.contact_btn_click()
        self.contact_modal.set_email("jhon34@mail.com")
        self.contact_modal.set_name("Jhon"*10)
        self.contact_modal.set_message("Hello world!")
        self.contact_modal.send_message_click()
        wdw(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text != "Thanks for the message!!"
        alert.accept()

    def test_message_length_more_than_256_char(self, driver):
        self.home_page.contact_btn_click()
        self.contact_modal.set_email("jhon34@mail.com")
        self.contact_modal.set_name("Jhon")
        self.contact_modal.set_message("Hello world!"*256)
        self.contact_modal.send_message_click()
        wdw(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text != "Thanks for the message!!"
        alert.accept()

    def test_X_btn(self, driver):
        self.home_page.contact_btn_click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR, "body").get_attribute("class") == "modal-open"
        self.contact_modal.x_btn_click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR, "body").get_attribute("class") != "modal-open"

    def test_close_btn(self, driver):
        self.home_page.contact_btn_click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR, "body").get_attribute("class") == "modal-open"
        self.contact_modal.close_btn_click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR, "body").get_attribute("class") != "modal-open"
