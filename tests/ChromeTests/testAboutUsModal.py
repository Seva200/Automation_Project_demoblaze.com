from time import sleep
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.utils.chromeDriverSetUp import ChromeDriverSetUp
from src.pages.HomePage import HomePage
from src.pages.AboutUsModal import AboutUsModal

hp = HomePage
au = AboutUsModal

class TestAboutUsModal(ChromeDriverSetUp):

    def test_play_btn(self):
        hp.about_us_btn_click(self)
        au.play_btn_click(self)
        sleep(3)
        self.assertGreater(self.driver.find_element(By.CSS_SELECTOR, "#example-video > div.vjs-control-bar > div.vjs-progress-control.vjs-control > div").get_attribute("aria-valuenow"), "0")