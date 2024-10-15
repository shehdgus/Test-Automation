import pytest
import time
from testData.coupangData import coupnangData
from pagesObjects.myCoupang import MyCoupang
from utilites.baseclass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

@pytest.mark.smoketest
@pytest.mark.tmycoupang
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
    
    #마이 쿠팡 > Default 주문목록 페이지 랜딩 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.mycoupang
    def test_mycoupang_landing(self,setup):
        log = self.getLogger()
        wait = WebDriverWait(setup, 10)
        wait.until(EC.presence_of_element_located(MyCoupang.mycoupang))
        self.mycoupang.getmycoupnag().click()
        lnb = self.mycoupang.getmclnb()
        title = self.mycoupang.getOrderListTitle()
        wait = WebDriverWait(setup, 10)
        wait.until(EC.presence_of_element_located(MyCoupang.mclnb))
        wait.until(EC.presence_of_element_located(MyCoupang.order_list_title))
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert lnb.is_displayed() and title.is_displayed, "MY쿠팡 랜딩 불가 또는 페이지 비정상 노출" #마이 쿠팡 랜딩 후 주문목록 화면 노출 확인
    
    #회원정보확인 페이지 랜딩 확인 케이스    
    @pytest.mark.mycoupang
    @pytest.mark.lnb
    def test_modify_landing(self,setup):
        log = self.getLogger()
        self.mycoupang.getModify().click()
        title = self.mycoupang.getCheckTitle().text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert title == "회원정보확인", "회원정보확인 페이지 랜딩 불가 또는 페이지 비정상 노출" #회원정보확인 페이지 랜딩 후 화면 요소 노출 확인
    
    #회원정보 수정 페이지 랜딩 확인 케이스
    @pytest.mark.mycoupang    
    @pytest.mark.modify    
    def test_checkpw(self,setup):
        log = self.getLogger()
        test_data = coupnangData.test_coupang_data[0] #계정 정보 가져오기
        mypw = test_data["PW"]
        self.mycoupang.getCheckPw().send_keys(mypw)
        self.mycoupang.getCheck().click()
        wait = WebDriverWait(setup, 10)
        wait.until(EC.presence_of_element_located(MyCoupang.modifytitle))
        title = self.mycoupang.getModifyTitle().text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert title == "회원정보 수정", "회원정보 수정 페이지 랜딩 불가 또는 페이지 비정상 노출" #회원정보 수정 페이지 랜딩 후 화면 요소 노출 확인
    
    #배송지 관리 버튼 동작 확인 케이스
    @pytest.mark.mycoupang    
    @pytest.mark.modify    
    def test_dam(self,setup):
        log = self.getLogger()
        main_window = setup.current_window_handle
        dam = self.mycoupang.getDAM()
        assert dam.is_displayed(), "[배송지 관리] 버튼 미노출"
        dam.click()
        time.sleep(2)
        all_windows = setup.window_handles
        for window in all_windows:
            if window != main_window:
                setup.switch_to.window(window)
                break
        title = self.mycoupang.getaddPT().text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert title == "배송지 목록", "배송지 목록 팝업 호출 불가 또는 비정상 노출" #배송지 목록 팝업 호출 여부 확인
     
    #배송지 수정 페이지 랜딩 확인 케이스    
    @pytest.mark.mycoupang    
    @pytest.mark.modify    
    def test_modify_address(self,setup): 
        log = self.getLogger()
        modifyntn = self.mycoupang.getModifyAddresses()
        assert modifyntn.is_displayed(), "수정 버튼 미노출"
        modifyntn.click()
        title = self.mycoupang.getaddPT().text
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert title == "배송지 수정", "배송지 수정 페이지 랜딩 불가 또는 비정상 노출" #배송지 수정 페이지 랜딩 여부 확인
    
    #수정 사항 반영 동작 확인 케이스        
    @pytest.mark.mycoupang    
    @pytest.mark.modify    
    def test_modify_info(self,setup):
        log = self.getLogger()
        real_name = "테스트" #임의 설정 부분
        real_num = "010-0000-0000" #임의 설정 부분
        
        receiver = self.mycoupang.getReceiver()
        receiver.clear() #받는 사람 필드 삭제
        receiver.send_keys(f"{real_name}")  #받는 사람 필드 값 전달
        name = receiver.get_attribute("value")
    
        phone = self.mycoupang.getPhoneField()
        phone.clear() #연락처 필드 삭제
        phone.send_keys(f"{real_num}") #연락처 값 전달
        num = phone.get_attribute("value")
        
        self.mycoupang.getSaveBtn().click()
        time.sleep(2)
        list_name = self.mycoupang.getListname().text
        list_phone = self.mycoupang.getListphone().text
        
        assert name == list_name and num == list_phone, "수정 사항 반영 안됨" #이름,연락처 대조하여 수정 사항 반영 여부 확인
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        setup.close()
        time.sleep(1)
        windowsOpened = setup.window_handles
        setup.switch_to.window(windowsOpened[0])
    
    # 개인정보수정 > 나가기 버튼 동작 확인 케이스           
    @pytest.mark.mycoupang    
    @pytest.mark.modify    
    def test_modify_back(self,setup):
        log = self.getLogger()
        windowsOpened = setup.window_handles
        setup.switch_to.window(windowsOpened[0])
        back_btn = self.mycoupang.getBackBTN()
        self.action.scroll_by_amount(0,500).perform()
        time.sleep(2)
        back_btn.click()
        lnb = self.mycoupang.getmclnb()
        title = self.mycoupang.getOrderListTitle()
        wait = WebDriverWait(setup, 10)
        wait.until(EC.presence_of_element_located(MyCoupang.mclnb))
        wait.until(EC.presence_of_element_located(MyCoupang.order_list_title))
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        assert lnb.is_displayed() and title.is_displayed, "수정 나가기 버튼 동작 비정상"  #마이 쿠팡 랜딩 후 주문목록 화면 노출 확인
    
    #연도별 구매 내역 정렬 동작 확인 케이스
    @pytest.mark.mycoupang    
    @pytest.mark.orderlist
    def test_order_sort(self,setup):
        log = self.getLogger()
        year = "2024"   #임의 설정 부분
        sorting = self.mycoupang.getSort()
        for sort in sorting:
            if sort.text == f"{year}":
                sort.click()
                break
         
        years = []
                    
        while True:
            order_year = self.mycoupang.getOrderYear()
            for orderyear in order_year:
                orderyear = orderyear.text
                oy = orderyear[:4]
                years.append(oy)
            
            next_btn = self.mycoupang.getNextBTN()
            
            if not next_btn.is_enabled():
                break
            
            next_btn.click()
            time.sleep(2)
        
        years.append("2025")
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.info(f"테스트 실행 시각: {current_time}")
        for my_year in years:
            assert year == my_year, "연도 정렬 비정상" #구매 내역에서 연도 추출하여 기준과 일치 여부 확인