from selenium.webdriver.common.by import By

class MyCoupang:

    def __init__(self, driver):
        self.driver = driver
        
    mycoupang = (By. XPATH, "//span[@class='my-coupang-icon gnb-icon-item']")
    order_list_title = (By. XPATH, "//span[@class='sc-1vjn3x9-2 sc-173hyd4-1 izFbWh QxeWJ']")
    mclnb = (By. XPATH, "//div[@id='mc-left-menu']")
    modify = (By. XPATH, "//li[@id='mc-user-modify-page']")
    checktitle = (By. XPATH, "//h1[@class='usermodify-auth-title']")    
    checkpw = (By. XPATH, "//input[@type='password']")
    check = (By. XPATH, "//button[@type='submit']")
    modifytitle = (By. XPATH, "//h1[@class='usermodify-title']")
    DAM = (By. XPATH, "//a[@id='deliveryAddressPopUp']")
    add_pop_title = (By. XPATH, "//h1[@class='content-head__title']")
    add_address = (By. XPATH, "//button[@class='addressbook__button--new _addressBookFormSubmit']")
    modify_address = (By. XPATH, "//div[@class='content-body content-body--fixed']//div[2]//div[3]//form[1]//button[1]")
    receiver_field = (By. XPATH, "//input[@id='addressbookRecipient']")
    phone_field = (By. XPATH, "//input[@id='addressbookCellphone']")
    savebtn = (By. XPATH, "//button[@class='addressbook__button--save _addressBookFormSubmit']")
    list_name = (By. XPATH, "//div[@class='content-body content-body--fixed']//div[2]//div[1]//div[1]//div[1]")
    list_phone = (By. XPATH, "//body/div[@class='content _addressBookRoot']/div[@class='content-block']/div[contains(@class,'content-wrapper')]/div[@class='content-body content-body--fixed']/div[contains(@class,'content-body__corset')]/div[2]/div[2]/div[2]")
    backbtn = (By. XPATH, "//button[contains(text(),'나가기')]")
    sort = (By. XPATH, "//div[@class='sc-py7v18-0 ghaYID']/div")
    order_year = (By. XPATH, "//div[@class='sc-abukv2-1 kSZYgn']")
    next_btn = (By. XPATH, "//button[contains(text(),'다음')]")
    
    def getmycoupnag(self):
        return self.driver.find_element(*MyCoupang.mycoupang)
    
    def getmclnb(self):
        return self.driver.find_element(*MyCoupang.mclnb)
    
    def getModify(self):
        return self.driver.find_element(*MyCoupang.modify)
    
    def getCheckPw(self):
        return self.driver.find_element(*MyCoupang.checkpw)
    
    def getCheck(self):
        return self.driver.find_element(*MyCoupang.check)
    
    def getCheckTitle(self):
        return self.driver.find_element(*MyCoupang.checktitle)
    
    def getModifyTitle(self):
        return self.driver.find_element(*MyCoupang.modifytitle)
    
    def getDAM(self):
        return self.driver.find_element(*MyCoupang.DAM)
    
    def getADD_adress(self):
        return self.driver.find_element(*MyCoupang.add_address)
    
    def getaddPT(self):
        return self.driver.find_element(*MyCoupang.add_pop_title)
    
    def getModifyAddresses(self):
        return self.driver.find_element(*MyCoupang.modify_address)
    
    def getReceiver(self):
        return self.driver.find_element(*MyCoupang.receiver_field)
    
    def getPhoneField(self):
        return self.driver.find_element(*MyCoupang.phone_field)
    
    def getSaveBtn(self):
        return self.driver.find_element(*MyCoupang.savebtn)
    
    def getListname(self):
        return self.driver.find_element(*MyCoupang.list_name)
    
    def getListphone(self):
        return self.driver.find_element(*MyCoupang.list_phone)
    
    def getBackBTN(self):
        return self.driver.find_element(*MyCoupang.backbtn)
    
    def getSort(self):
        return self.driver.find_elements(*MyCoupang.sort)
    
    def getOrderListTitle(self):
        return self.driver.find_element(*MyCoupang.order_list_title)
    
    def getOrderYear(self):
        return self.driver.find_elements(*MyCoupang.order_year)
    
    def getNextBTN(self):
        return self.driver.find_element(*MyCoupang.next_btn)