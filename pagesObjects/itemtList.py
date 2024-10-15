from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class ItemList:

    def __init__(self, driver):
        self.driver = driver
        
    title_keyword = (By. XPATH , "//p[@class='hit-count']")
    filter_rocket = (By. XPATH , "//label[@for='deliveryFilterOption-rocket_all']")
    sorting_low = (By. XPATH , "//label[contains(text(),'낮은가격순')]")
    product_list = (By. XPATH , "//ul[@id='productList']/li")
   
    def getTitleKeyword(self):
        return self.driver.find_element(*ItemList.title_keyword)
    
    def getFilterRocket(self):
        return self.driver.find_element(*ItemList.filter_rocket)
    
    def getFilterRocket(self):
        return self.driver.find_element(*ItemList.filter_rocket)
    
    def getSortingLow(self):
        return self.driver.find_element(*ItemList.sorting_low)
    
    def getProductList(self):
        return self.driver.find_elements(*ItemList.product_list)
    
    def rocketwait(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.presence_of_element_located(ItemList.filter_rocket))
    
    def sortingwait(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.presence_of_element_located(ItemList.sorting_low))