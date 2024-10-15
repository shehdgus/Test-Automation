from selenium.webdriver.common.by import By

class MainHome:

    def __init__(self, driver):
        self.driver = driver
        
    total_menu_list = ["패션의류/잡화","뷰티","출산/유아동","식품","주방용품","생활용품","홈인테리어","가전디지털",
                       "스포츠/레저","자동차용품","도서/음반/DVD","완구/취미","문구/오피스","반려동물용품","헬스/건강식품","여행/티켓","테마관","입점/판매 신청"]
    drop_down_list = ['전체', '여성패션', '남성패션', '남녀 공용 의류', '유아동패션', '뷰티', '출산/유아동', '식품', '주방용품', '생활용품', '홈인테리어', '가전디지털', '스포츠/레저', '자동차용품', 
                      '도서/음반/DVD', '완구/취미', '문구/오피스', '반려동물용품', '헬스/건강식품', '국내여행', '해외여행', '로켓럭셔리', '로켓설치', '쿠팡 프리미엄', '공간별 집꾸미기', '헬스케어 전문관', 
                    '쿠팡 Only', '싱글라이프', '악기전문관', '결혼준비', '아트/공예', '미세먼지용품', '홈카페', '실버스토어', '로켓펫닥터']
    login_btn = (By.XPATH, '//li[@id="login"]')
    logout_btn = (By. XPATH, '//a[@class="logout"]')
    total_menu = (By.XPATH, '//a[@href="javascript:;"][contains(text(),"카테고리")]')
    total_2depth = (By. XPATH, '//ul[@class="menu shopping-menu-list"]/li/a')
    gnb = (By.XPATH, '//ul[@class="gnb-menu-scroll gnb-menu-animation"]/li/a/span')
    search_dropdown = (By.XPATH, '//select[@class="search_category_filter"]')
    search_dropdown_text = (By.XPATH, '//div[@class="select--category"]')
    search_dropdown_text_current = (By.XPATH, '//div[@class="header-searchForm"]')
    search_dropdown_btn = (By. XPATH, "//*[@id='sbToggle_48298016' and @class='select--category--button']")
    search_dropdown_list = (By.XPATH, '//ul[@class="select--category--option"]/li')
    searchbtn = (By.XPATH, '//a[@class="search"]')
    searchbar = (By.XPATH, "//input[@id='headerSearchKeyword']")
    name = (By. XPATH, "//li[@id='myCoupang']")
    ticket = (By. XPATH, "//ul[@class='menu ticket-menu-list']")
    theme = (By. XPATH, "//li[@class='theme-store']") 
    ingress = (By. XPATH, "//li[@class='ingress-point']") 

    coupangplay =  (By. XPATH, "//a[@class='OpenFeedNavbar_navbarLogo__3Azg9']")
    coupang_rocket_title = (By. XPATH, "//h1[contains(text(),'로켓배송')]") 
    coupang_fresh_title = (By. XPATH, "//h1[contains(text(),'로켓프레시')]") 

    def getLoginbtn(self):
        return self.driver.find_element(*MainHome.login_btn)

    def getLogoutbtn(self):
        return self.driver.find_element(*MainHome.logout_btn)

    def getTotalmenu(self):
        return self.driver.find_element(*MainHome.total_menu)

    def getTotalmenu2depth(self):
        return self.driver.find_elements(*MainHome.total_2depth)

    def getGNB(self):
        return self.driver.find_elements(*MainHome.gnb)

    def getSearchdropdown(self):
        return self.driver.find_element(*MainHome.search_dropdown)

    def getSearchdropdownText(self):
        return self.driver.find_element(*MainHome.search_dropdown_text)
    
    def getSearchdropdownTextCurrent(self):
        return self.driver.find_element(*MainHome.search_dropdown_text_current)
    
    def getSearchdropdownbtn(self):
        return self.driver.find_element(*MainHome.search_dropdown_btn)
    
    def getSearchdropdown_list(self):
        return self.driver.find_elements(*MainHome.search_dropdown_list)
    
    def getDropDownList(self):
        return self.drop_down_list

    def getSearchbtn(self):
        return self.driver.find_element(*MainHome.searchbtn)

    def getSearchbar(self):
        return self.driver.find_element(*MainHome.searchbar)
    
    def getName(self):
        return self.driver.find_element(*MainHome.name)
 
    def getTotalMenuList(self):
        return self.total_menu_list
    
    def getMenu_Ticket(self):
        return self.driver.find_element(*MainHome.ticket)
    
    def getMenu_Theme(self):
        return self.driver.find_element(*MainHome.theme)
    
    def getMenu_Ingress(self):
        return self.driver.find_element(*MainHome.ingress)
    
    def getCoupangPlay(self):
        return self.driver.find_element(*MainHome.coupangplay)
    
    def getCoupangRocketTitle(self):
        return self.driver.find_element(*MainHome.coupang_rocket_title)
    
    def getCoupangFreshTitle(self):
        return self.driver.find_element(*MainHome.coupang_fresh_title)
