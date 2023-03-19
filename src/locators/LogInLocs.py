from selenium.webdriver.common.by import By

log_in_locs = dict()

log_in_locs['Username'] = (By.CSS_SELECTOR, "#loginusername")
log_in_locs['Password'] = (By.CSS_SELECTOR, "#loginpassword")
log_in_locs['X_btn'] = (By.CSS_SELECTOR, "#logInModal > div > div > div.modal-header > button > span")
log_in_locs['Close_btn'] = (By.CSS_SELECTOR, "#logInModal > div > div > div.modal-header > button > span")
log_in_locs['LogIn_btn'] = (By.CSS_SELECTOR, "#logInModal > div > div > div.modal-footer > button.btn.btn-primary")