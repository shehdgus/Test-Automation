from selenium.webdriver.common.by import By

class CheckOut:

    def __init__(self, driver):
        self.driver = driver
        
    page_title = (By. CSS_SELECTOR, "div[class='ordTitle'] h3[class='title']")
    buyer_info = (By. XPATH, "//td[@class='customer__col customer__col--2']")
    customer_phone = (By. XPATH, "//input[@class='customer-phone__input-tel ']")
    receive_name = (By. XPATH, "//span[@id='delivery-address__name-panel']")
    receive_address = (By. XPATH, "//td[@class='delivery-address__td']")
    receive_phone = (By. XPATH, "//td[@class='delivery-address__td delivery-address__td--no-line']")
    item_name = (By. XPATH, "//div[@class='bundle-info__vendor-item']")
    item_price = (By. XPATH, "//span[@id='totalPriceDisp']")
    total =  (By. XPATH, "//span[@id='totalPriceDisp']")
    coupon =  (By. XPATH, "//div[@class='price']//span[@class='value use-calculation-for-totalprice'][normalize-space()='0']")
    fee = (By. XPATH, "//span[@id='deliveryPriceDisp']")
    ccash = (By. XPATH, "//tr[@class='payCoupangCash']//span[@class='value use-calculation-for-totalprice'][normalize-space()='0']")
    final = (By. XPATH, "//span[@id='totalPayPriceDisp']")
    paytype = (By. XPATH, "//ul[@id='payTypeList']/li")
    banklist = (By. XPATH, "//select[@id='label_rocketBank_bankList']")
    payment = (By. XPATH, "//button[@id='paymentBtn']")
   
    def getBuyer(self):
        return self.driver.find_elements(*CheckOut.buyer_info)
        
    def getCustomerPhone(self):
        return self.driver.find_element(*CheckOut.customer_phone)
    
    def getItemName(self):
        return self.driver.find_element(*CheckOut.item_name)

    def getItemPrice(self):
        return self.driver.find_element(*CheckOut.item_price)
    
    def getPageTitle(self):
        return self.driver.find_element(*CheckOut.page_title)
    
    def getReceiverName(self):
        return self.driver.find_element(*CheckOut.receive_name)

    def getReceiverAddress(self):
        return self.driver.find_element(*CheckOut.receive_address)

    def getReceiverPhone(self):
        return self.driver.find_element(*CheckOut.receive_phone)
    
    def getTotal(self):
        return self.driver.find_element(*CheckOut.total)

    def getCoupon(self):
        return self.driver.find_element(*CheckOut.coupon)
    
    def getFee(self):
        return self.driver.find_element(*CheckOut.fee)
    
    def getCash(self):
        return self.driver.find_element(*CheckOut.ccash)

    def getFinal(self):
        return self.driver.find_element(*CheckOut.final)
    
    def getPayType(self):
        return self.driver.find_elements(*CheckOut.paytype)
    
    def getBankList(self):
        return self.driver.find_element(*CheckOut.banklist)
    
    def getPayment(self):
        return self.driver.find_element(*CheckOut.payment)