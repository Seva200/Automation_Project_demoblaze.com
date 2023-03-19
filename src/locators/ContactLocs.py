from selenium.webdriver.common.by import By

contact_locs = dict()

contact_locs['Email_fld'] = (By.CSS_SELECTOR, "#recipient-email")
contact_locs['Name_fld'] = (By.CSS_SELECTOR, "#recipient-name")
contact_locs['Message_fld'] = (By.CSS_SELECTOR, "#message-text")
contact_locs['X_btn'] = (By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-header > button > span")
contact_locs['Close_btn'] = (By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-footer > button.btn.btn-secondary")
contact_locs['Send_msg_btn'] = (By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-footer > button.btn.btn-primary")