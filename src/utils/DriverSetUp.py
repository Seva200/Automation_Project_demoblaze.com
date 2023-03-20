import pytest
from selenium import webdriver
from src.pages.HomePage import HomePage
from src.pages.ContactModal import ContactModal


class DriverSetUp:

    @pytest.fixture()
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        self.home_page = HomePage(self.driver)
        self.contact_modal = ContactModal(self.driver)
        yield self.driver
        self.driver.quit()
