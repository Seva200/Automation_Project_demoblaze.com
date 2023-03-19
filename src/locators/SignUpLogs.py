from selenium.webdriver.common.by import By

sign_up_locs = dict()

sign_up_locs['Username'] = (By.CSS_SELECTOR, "#sign-username")
sign_up_locs['Password'] = (By.CSS_SELECTOR, "#sign-username")
sign_up_locs['X_btn'] = (By.CSS_SELECTOR, "#signInModal > div > div > div.modal-header > button > span")
sign_up_locs['Close_btn'] = (By.CSS_SELECTOR, "#signInModal > div > div > div.modal-footer > button.btn.btn-secondary")
sign_up_locs['SignUp_btn'] = (By.CSS_SELECTOR, "#signInModal > div > div > div.modal-footer > button.btn.btn-primary")