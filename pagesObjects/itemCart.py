from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class ItemCart:

    def __init__(self, driver):
        self.driver = driver
        
    productname_cart = (By. XPATH, "//span[contains(@class,'modify-color')]")
    productprice_cart = (By. XPATH, "//div[contains(@class,'unit-total-sale-price')]")
    excepted_price = (By. XPATH, "//em[contains(@class,'order-product-price')]")
    paybtn = (By. XPATH, "//a[@id='btnPay']")
   
    def getProductNameCart(self):
        return self.driver.find_element(*ItemCart.productname_cart)
    
    def getProductPriceCart(self):
        return self.driver.find_element(*ItemCart.productprice_cart)

    def getProductExcepted(self):
        return self.driver.find_element(*ItemCart.excepted_price)
    
    def getPayBtn(self):
        return self.driver.find_element(*ItemCart.paybtn)
    
    # def getPayBtn(self):
    #     wait = WebDriverWait(self.driver, 5)
    #     return wait.until(EC.presence_of_element_located(ItemCart.paybtn))