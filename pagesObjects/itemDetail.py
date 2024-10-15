from selenium.webdriver.common.by import By

class ItemDetail:

    def __init__(self, driver):
        self.driver = driver
        
    product_name = (By. XPATH, "//h1[@class='prod-buy-header__title']")
    product_price = (By. CSS_SELECTOR, "span[class='total-price'] strong")
    cartbtn = (By. XPATH, "//button[contains(text(), '장바구니 담기')]")
    # cartbtn = (By. XPATH, "//button[@class='prod-cart-btn']")
   
    def getProductName(self):
        return self.driver.find_element(*ItemDetail.product_name)
    
    def getProductPrice(self):
        return self.driver.find_element(*ItemDetail.product_price)
    
    def getCartbtn(self):
        return self.driver.find_element(*ItemDetail.cartbtn)