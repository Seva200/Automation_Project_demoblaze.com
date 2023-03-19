from selenium.webdriver.common.by import By

cart_locs = dict()

cart_locs['Place_order_btn'] = (By.CSS_SELECTOR, "#page-wrapper > div > div.col-lg-1 > button")
cart_locs['Name_fld'] = (By.CSS_SELECTOR, "#name")
cart_locs['Country_fld'] = (By.CSS_SELECTOR, "#country")
cart_locs['City_fld'] = (By.CSS_SELECTOR, "#city")
cart_locs['Credit_card_fld'] = (By.CSS_SELECTOR, "#card")
cart_locs['Month_fld'] = (By.CSS_SELECTOR, "#month")
cart_locs['Year_fld'] = (By.CSS_SELECTOR, "/html/body/div[3]/div/div/div[2]/form/div[6]/input")
cart_locs['X_btn'] = (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-header > button > span")
cart_locs['Close_btn'] = (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-footer > button.btn.btn-secondary")
cart_locs['Purchase_btn'] = (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-footer > button.btn.btn-primary")
cart_locs['Delete_btn'] = (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-header > button > span")