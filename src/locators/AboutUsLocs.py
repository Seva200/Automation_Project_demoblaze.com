from selenium.webdriver.common.by import By

about_us_locs = dict()

about_us_locs['Play_btn'] = (By.CSS_SELECTOR, "#example-video > button > span.vjs-control-text")
about_us_locs['X_btn'] = (By.CSS_SELECTOR, "#videoModal > div > div > div.modal-header > button > span")
about_us_locs['Close_btn'] = (By.CSS_SELECTOR, "#videoModal > div > div > div.modal-footer > button")