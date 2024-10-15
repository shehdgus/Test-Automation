# .\.venv\Scripts\Activate 가상환경 실행
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time
from pagesObjects.MainHome import MainHome
from pagesObjects.loginPage import loginPage
from testData.coupangData import coupnangData

# @pytest.mark.smoketest
@pytest.mark.usefixtures("setup")
class TestCounpang :
    
    @pytest.fixture(autouse=True)
    def setup_mainhome(self, setup):
        self.mainhome = MainHome(setup)
    
    @pytest.fixture(autouse=True)    
    def setup_loginpage(self, setup):
        self.loginpage = loginPage(setup)
    
    @pytest.fixture(autouse=True)    
    def setup_action(self, setup):
        self.action = ActionChains(setup)
     
    # 드롭박스 디폴트 값 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.mdropdown
    def test_search_dropdown_default(self,setup) :
        dropdown_default = self.mainhome.getSearchdropdownText().text
        assert dropdown_default == "전체", "드롭다운 디폴트 값 비정상"
    
    # 드롭박스 리스트 스펙 확인 케이스
    @pytest.mark.mainhome
    @pytest.mark.mdropdown
    def test_search_dropdown_listing(self,setup) :
        setup.get("https://gall.dcinside.com/board/lists/?id=sh_new")
        setup.find_element(By. XPATH, "//div[@class='select_box array_num']").click()
        c = setup.find_elements(By. XPATH, "//div[@class='select_box array_num']/ul/li")
        list = []
        for a in c:
            a = a.text
            list.append(a)
        print(list)
        # dropdownbtn = (self.mainhome.getSearchdropdownText())
        # self.action.click(dropdownbtn).perform()
        time.sleep(3)
    #     ddlist = self.mainhome.getSearchdropdown_list()
    #     dditems = []
    #     for item in ddlist :
    #         item = item.text
    #         dditems.append(item)
    #     specitems = self.mainhome.getDropDownList()
    #     specitems.sort()
    #     dditems.sort()
    #     assert dditems == specitems, "드롭다운 리스트 값 비정상"    
    
    # # 드롭박스 내 아이템 임의 선택 동작 확인 케이스
    # @pytest.mark.mainhome
    # @pytest.mark.mdropdown
    # def test_search_dropdown_select(self,setup) :
    #     item = "식품" # 임의 선정 부분
    #     self.action.move_to_element(setup.find_element(By. XPATH, f"//a[contains(text(), '{item}')]")).click().perform()
    #     dropdown_selected = self.mainhome.getSearchdropdownTextCurrent().text
    #     a = list(dropdown_selected)
    #     current = a[3]+a[4] # 임의 선정한 글자 수에 따라 조정 필요
    #     assert current == f"{item}", "드롭다운 선택 값 일치 하지 않음"