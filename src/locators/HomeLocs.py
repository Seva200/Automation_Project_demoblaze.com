from selenium.webdriver.common.by import By



home_locs = dict()

# Header
home_locs['Home'] = (By.CSS_SELECTOR, "#navbarExample > ul > li.nav-item.active > a")
home_locs['Contact'] = (By.CSS_SELECTOR, "#navbarExample > ul > li:nth-child(2) > a")
home_locs['AboutUs'] = (By.CSS_SELECTOR, "#navbarExample > ul > li:nth-child(3) > a")
home_locs['Cart'] = (By.CSS_SELECTOR, "#cartur")
home_locs['LogIn'] = (By.CSS_SELECTOR, "#login2")
home_locs['SignUp'] = (By.CSS_SELECTOR, "#signin2")
home_locs['LogOut'] = (By.CSS_SELECTOR, "#logout2")
home_locs['Logo']  = (By.CSS_SELECTOR, "#nava")

# Slide Show = slsh
home_locs['slsh_right_arrow'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > a.carousel-control-next > span.carousel-control-next-icon")
home_locs['slsh_left_arrow'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > a.carousel-control-prev > span.carousel-control-prev-icon")
home_locs['slsh_left_indicator'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li.active")
home_locs['slsh_middle_indicator'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li.active")
home_locs['slsh_right_indicator'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li.active")

# Body
home_locs['Categories'] = (By.CSS_SELECTOR, "#cat")
home_locs['Phones'] = (By.XPATH, '//*[@id="itemc"]')
home_locs['Laptops'] = (By.CSS_SELECTOR, "#itemc")
home_locs['Monitors'] = (By.XPATH, "/html/body/div[5]/div/div[1]/div/a[4]")
home_locs['Item'] = (By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div > div > h4 > a")
home_locs['Previous'] = (By.CSS_SELECTOR, "#prev2")
home_locs['Next'] = (By.CSS_SELECTOR, "#next2")