from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from src.locators.ContactLocs import contact_locs

class ContactModal:
    def __init__(self, driver):
        self.driver = driver

    def wdw_locator(self, locator):
        return wdw(self.driver, 5).until(ec.visibility_of_element_located(locator))

    def set_email(self, email):
        ContactModal.wdw_locator(self, contact_locs['Email_fld']).send_keys(email)
    def set_name(self, name):
        ContactModal.wdw_locator(self, contact_locs['Name_fld']).send_keys(name)
    def set_message(self, message):
        ContactModal.wdw_locator(self, contact_locs['Message_fld']).send_keys(message)
    def x_btn_click(self):
        ContactModal.wdw_locator(self, contact_locs['X_btn']).click()
    def close_btn_click(self):
        ContactModal.wdw_locator(self, contact_locs['Close_btn']).click()
    def send_message_click(self):
        ContactModal.wdw_locator(self, contact_locs['Send_msg_btn']).click()