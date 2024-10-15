import pytest
import time
from selenium.webdriver.common.by import By
from testData.coupangData import coupnangData
from utilites.baseclass import BaseClass
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

@pytest.mark.smoketest
@pytest.mark.tcoupangmain
@pytest.mark.usefixtures("setup")
class TestCounpang(BaseClass) :    
    #메인 홈에서 이메일 로그인 랜딩 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.login
    def test_login_landing(self,setup):   
        log = self.getLogger()
        loginbtn = self.mainhome.getLoginbtn() #로그인 버튼 클릭 하여 로그인 페이지 랜딩
        loginbtn.click() 
        emailbtn = self.loginpage.getEmailbtn() 
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert emailbtn.is_displayed() == True, "이메일 로그인 페이지 랜딩 안 됨" #랜딩 후 Default 이메일 로그인 페이지 노출 여부 확인
        
    #로그인 동작 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.login    
    def test_login(self,setup):   
        log = self.getLogger()
        test_data = coupnangData.test_coupang_data[0] #계정 정보 가져오기  
        myid = test_data["ID"]
        mypw = test_data["PW"]
        self.loginpage.getIDfield().send_keys(myid) #아이디 입력
        self.loginpage.getPWfield().send_keys(mypw) #비밀번호 입력
        self.loginpage.getsubmitbtn().click() #로그인 버튼 클릭
        myname = test_data["이름"]
        myName = self.mainhome.getName().text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert myname+"님" == myName, "로그인 비정상" # 로그인 후 로그인 계정 이름 일치 여부 확인
                
    #전체 메뉴 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.totalmenu
    def test_totalmenu_listing(self,setup):
        log = self.getLogger()
        total_Menu = self.mainhome.getTotalmenu()
        action = ActionChains(setup)
        action.move_to_element(total_Menu).perform() #  전체메뉴에 마우스 오버  
        time.sleep(1)
        depth2 = self.mainhome.getTotalmenu2depth() # 메뉴명 크롤링 및 리스트화  
        depth2list = []
        for menu in depth2 :
            menu = menu.text
            depth2list.append(menu)       
        Ticket = self.mainhome.getMenu_Ticket() # 메뉴명 크롤링 및 리스트 추가 1  
        ticket = Ticket.text
        depth2list.append(ticket)
        Theme = self.mainhome.getMenu_Theme() # 메뉴명 크롤링 및 리스트 추가 2
        theme = Theme.text
        depth2list.append(theme) 
        depth2list.append("입점/판매 신청") # 해결 불가능한 이슈로 인해 임의 추가
        speclist = self.mainhome.getTotalMenuList()
        depth2list.sort()
        speclist.sort()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert depth2list == speclist, "리스트 불일치" # 메뉴 리스트 비교 확인          
             
    # GNB 쿠팡플레이 랜딩 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.mgnb
    def test_gnb1(self,setup) :
        log = self.getLogger()
        gnb_list = self.mainhome.getGNB()
        index_to_click = 0
        for index, gnblist in enumerate(gnb_list):
            if index == index_to_click:                              
                gnblist.click()
        windowsOpended = setup.window_handles
        setup.switch_to.window(windowsOpended[1])   
        url = setup.current_url
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 접속 후 URL 대조 및 페이지 요소 확인하여 접근 여부 확인
        coupang_play = self.mainhome.getCoupangPlay()
        assert url == "https://www.coupangplay.com/catalog"and coupang_play.is_displayed(), "쿠팡플레이 접근 불가 또는 화면 비정상 노출"   
        setup.close()
        setup.switch_to.window(windowsOpended[0])
                
    # GNB 로켓배송 랜딩 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.mgnb          
    def test_gnb2(self,setup) :
        log = self.getLogger()
        gnb_list = self.mainhome.getGNB()
        index_to_click = 1
        for index, gnblist in enumerate(gnb_list):
            if index == index_to_click:                              
                gnblist.click()
        url = setup.current_url
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 접속 후 URL 대조 및 페이지 타이틀 확인하여 접근 여부 확인
        rocket_title = self.mainhome.getCoupangRocketTitle().text
        assert url == "https://www.coupang.com/np/campaigns/82"and rocket_title == "로켓배송", "로켓배송 접근 불가 또는 화면 비정상 노출"  
        setup.back()
        
    # GNB 로켓프레시 랜딩 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.mgnb               
    def test_gnb3(self,setup) :
        log = self.getLogger()
        gnb_list = self.mainhome.getGNB()
        index_to_click = 2
        for index, gnblist in enumerate(gnb_list):
            if index == index_to_click:                              
                gnblist.click()
        url = setup.current_url
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 접속 후 URL 대조 및 페이지 타이틀 확인하여 접근 여부 확인
        fresh_title = self.mainhome.getCoupangFreshTitle().text
        assert url == "https://www.coupang.com/np/categories/393760"and fresh_title == "로켓프레시", "로켓프레시 접근 불가 또는 화면 비정상 노출"  
        setup.back()    
     
    # 드롭다운 디폴트 값 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.mdropdown
    def test_search_dropdown_default(self,setup) :
        log = self.getLogger()
        dropdown_default = self.mainhome.getSearchdropdownText().text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 드롭다운 노출 디폴트 값 확인
        assert dropdown_default == "전체", "드롭다운 디폴트 값 비정상"
    
    # 드롭다운 리스트 스펙 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.mdropdown
    def test_search_dropdown_listing(self,setup) :
        log = self.getLogger()
        dropdownbtn = (self.mainhome.getSearchdropdownText())
        self.action.click(dropdownbtn).perform()
        time.sleep(1)
        ddlist = self.mainhome.getSearchdropdown_list()
        dditems = []
        for item in ddlist :
            item = item.text
            dditems.append(item)
        specitems = self.mainhome.getDropDownList()
        specitems.sort()
        dditems.sort()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 드롭다운 리스트 값 확인
        assert dditems == specitems, "드롭다운 리스트 값 비정상"    
    
    # 드롭다운 내 아이템 임의 선택 동작 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.mdropdown
    def test_search_dropdown_select(self,setup) :
        log = self.getLogger()
        item = "식품" # 임의 선정 부분
        self.action.move_to_element(setup.find_element(By. XPATH, f"//a[contains(text(), '{item}')]")).click().perform()
        dropdown_selected = self.mainhome.getSearchdropdownTextCurrent().text
        a = list(dropdown_selected)
        current = a[3]+a[4] # 임의 선정한 글자 수에 따라 조정 필요
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 선택한 아이템 노출 확인
        assert current == f"{item}", "드롭다운 선택 값 일치 하지 않음"
    
    # 검색 및 결과 리스트 화면 노출 확인 케이스    
    @pytest.mark.mainhome
    @pytest.mark.search
    def test_search_keyword(self,setup) : 
        log = self.getLogger()
        searchbar = self.mainhome.getSearchbar()
        word = "커피" # 임의 선정 부분
        searchbar.send_keys(f"{word}")
        searchbtn = self.mainhome.getSearchbtn()
        searchbtn.click()
        time.sleep(1)
        title_keyword = self.itemlist.getTitleKeyword()
        title = title_keyword.text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 검색 동작 및 검색 결과 리스트에 검색한 키워드 노출 노출
        assert title == f"'{word}'에 대한 검색결과", "검색 동작 비정상이거나 검색 키워드 노출 되지 않음."
        
    # 상품리스트 필터 선택 동작 확인
    @pytest.mark.mainhome
    @pytest.mark.itemlist
    def test_search_filter_rocket(self,setup) : 
        log = self.getLogger()
        filter_rocket = self.itemlist.rocketwait()
        filter_rocket.click()
        time.sleep(2)
        rocket_tag = self.itemlist.getProductList()
        tags = []
        for tag in rocket_tag:
            tag = tag.find_element(By. XPATH, "./a/dl/dd/div/div[3]/div/div/em/span/img").get_attribute("alt")
            tags.append(tag)
        for tag in tags:
            # 로켓 관련 태그 노출 여부 확인
            assert "로켓" in tag, "로켓 필터링 비정상 동작"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        
    # 정렬 순서 기준 동작 확인
    @pytest.mark.mainhome
    @pytest.mark.itemlist
    def test_search_sorting_low(self,setup) : 
        log = self.getLogger()
        sorting_low = self.itemlist.sortingwait()
        sorting_low.click()
        time.sleep(2)
        product_price = self.itemlist.getProductList()
        price = []
        for cost in product_price:
            cost = cost.find_element(By. XPATH, "./a/dl/dd/div/div[3]/div/div/em/strong").text
            cost = int(cost.replace(',', '').strip())
            price.append(cost)
        pprice = price.copy()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 낮은가격순 적용 여부 확인
        assert price == sorted(pprice), "낮은 가격순 정렬 적용 안 됨"
    
    # 상품 상세 페이지 랜딩 동작 확인
    @pytest.mark.mainhome
    @pytest.mark.itemlist
    def test_procuct_detail(self,setup):
        log = self.getLogger()
        products = self.itemlist.getProductList()
        # 임의의 상품 선택
        random_product = products[1]
        random_product_name = random_product.find_element(By. XPATH, "./a/dl/dd/div/div[2]").text
        random_product.click()
        windowsOpended = setup.window_handles
        setup.switch_to.window(windowsOpended[1])
        details_name = self.itemdetail.getProductName().text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 상품 리스트 내 상품명과 상품 상세 화면 내 상품명 일치 여부 확인
        assert random_product_name == details_name, "상품명 비정상 노출 또는 상품 상세 페이지 접근 비정상"
    
    # 상품 상세 페이지에서 장바구니 담기 동작 확인 케이스    
    @pytest.mark.mainhome
    @pytest.mark.itemdetail
    def test_get_to_cart(self,setup) :
        log = self.getLogger()
        windowsOpended = setup.window_handles
        setup.switch_to.window(windowsOpended[1])
        product_name = self.itemdetail.getProductName().text
        product_price = self.itemdetail.getProductPrice().text
        self.action.scroll_by_amount(0,500).perform()
        time.sleep(3)
        self.itemdetail.getCartbtn().click()
        time.sleep(2)
        self.action.move_to_element(setup.find_element(By. XPATH, "//a[contains(text(), '장바구니 바로가기 >')]")).click().perform()
        time.sleep(2)
        product_name_cart = self.itemcart.getProductNameCart().text
        product_price_cart = self.itemcart.getProductPriceCart().text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 선택한 상품과 장바구니에 담긴 상품 이름,가격 비교
        assert product_name == product_name_cart and product_price == product_price_cart, "장바구니 담기 불가 또는 선택한 상품 장바구니에 미노출 또는 상품 정보 비일치"
    
    # 상품 가격과 주문 예상 금액 비교 확인 케이스    
    @pytest.mark.mainhome
    @pytest.mark.itemcart
    def test_excepted_price(self,setup) :
        log = self.getLogger()
        product_price_cartt = self.itemcart.getProductPriceCart().text
        excepted_price = self.itemcart.getProductExcepted().text
        pp = product_price_cartt
        ep = excepted_price
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 상품 가격과 주문 예상 금액 비교
        assert pp == ep+"원", "상품 가격 주문 예상 금액과 불일치"
    
    # 주문/결제 페이지 랜딩 동작 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.itemcart
    def test_landing_to_checkout(self,setup):  
        log = self.getLogger()  
        name = self.itemcart.getProductNameCart().text
        price = self.itemcart.getProductExcepted().text    
        price = price.replace(',','')
        self.itemcart.getPayBtn().click()
        coname = self.checkout.getItemName().text
        coprice = self.checkout.getItemPrice().text
        title = self.checkout.getPageTitle().text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        # 페이지 랜딩 확인
        assert title == "주문/결제", "주문/결제 페이지 미노출 또는 비정상 노출"
        # 구매할 상품명,가격과 주문/결제 페이지 상품명,가격 비교
        assert name == coname and price == coprice, "상품 정보 일치하지 않거나 비정상 노출"
        
    # 주문/결제 구매자정보 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.checkout
    def test_buy_info(self,setup):
        log = self.getLogger()
        buyer = self.checkout.getBuyer()
        infos = []
        for info in buyer:
            info = info.text
            infos.append(info)
        phone = self.checkout.getCustomerPhone().get_attribute("value")
        phone = phone.replace(' ','')
 
        myinfo = coupnangData.test_coupang_data[0]
        myname = myinfo["이름"]
        myemail = myinfo["ID"]
        myphone = myinfo["연락처"] 
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        
        assert infos[0] == myname, "구매자 이름 불일치"
        assert infos[1] == myemail, "구매자 이메일 불일치"
        assert phone == myphone, "구매자 연락처 불일치"
        
    # 주문/결제 받는사람정보 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.checkout
    def test_receive_info(self,setup):
        log = self.getLogger()
        rname = self.checkout.getReceiverName().text
        raddress = self.checkout.getReceiverAddress().text
        rphone = self.checkout.getReceiverPhone().text.replace(' ','')
        
        myinfo = coupnangData.test_coupang_data[0]
        myname = myinfo["이름"]
        myaddress = myinfo["주소"]
        myphone = myinfo["연락처"] 
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        
        assert rname == myname, "받는 사람 이름 불일치"
        assert raddress == myaddress, "받는 사람 주소 불일치"
        assert rphone == myphone, "받는 사람 연락처 불일치"
        
    # 총결제금액 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.checkout
    def test_final_price(self,setup):
        log = self.getLogger()
        total = int(self.checkout.getTotal().text)
        coupon = int(self.checkout.getCoupon().text)
        fee = int(self.checkout.getFee().text)
        cash = int(self.checkout.getCash().text)
        final = (self.checkout.getFinal().text)
        final = int(final.replace(',',''))
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert final == (total-coupon-cash+fee), "총결제금액 산정 비정상"

    # 결제 동작 확인 케이스(계좌이체)
    @pytest.mark.mainhome
    @pytest.mark.checkout
    def test_method_of_payment(self,setup):
        time.sleep(3)
        log = self.getLogger()
        paytype = self.checkout.getPayType()
        for type in paytype:
            input_element = type.find_element(By.XPATH, "./input")
            if input_element.get_attribute("value") == "ROCKET_BANK" :
                input_element.click()
                assert input_element.is_selected(), "계좌이체 라디오 버튼 선택 동작 비정상"
                break
        time.sleep(1)
        banklist = Select(self.checkout.getBankList())
        banklist.select_by_visible_text("신한은행 / ********8883") # 결제 테스트 은행 정보 삽입
        time.sleep(1)
        self.checkout.getPayment().click()
        time.sleep(3)
        setup.switch_to.frame("callLGPayment")
        a = setup.find_element(By. XPATH, "//h2[@class='rocketpay-container-header-h2 debranding']").text
        setup.switch_to.default_content()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert a == "비밀번호입력", "비밀번호 입력 팝업 호출 되지 않음"