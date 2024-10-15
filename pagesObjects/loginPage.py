from selenium.webdriver.common.by import By

class loginPage:

    def __init__(self, driver):
        self.driver = driver

    idfield = (By.XPATH, '//input[@class="member__input _loginIdInput ui-autocomplete-input"]')
    pwfield = (By. XPATH, '//input[@class="member__input _loginPasswordInput"]')
    submitbtn = (By.XPATH, '//button[@type="submit"]')
    emailbtn = (By. XPATH, '//a[@class="password active"]')


    def getIDfield(self):
        return self.driver.find_element(*loginPage.idfield)

    def getPWfield(self):
        return self.driver.find_element(*loginPage.pwfield)

    def getsubmitbtn(self):
        return self.driver.find_element(*loginPage.submitbtn)
       
    def getEmailbtn(self):
        return self.driver.find_element(*loginPage.emailbtn)