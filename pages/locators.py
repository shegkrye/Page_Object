from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//input[@name='login-redirect_url']")
    
class LoginPageLocators():
    Registration_link = (By.XPATH, "//input[@name='registration-redirect_url']")
    