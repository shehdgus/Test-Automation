import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options                                            #해야할 것 1. 일단 완성 2. 로깅,스샷 추가 3. 엣지 추가 4. 함수화 도전 5. 예외처리 다시 듣기
                                                                                   #예외처리를 입점/판매 문의 이거로하면 될듯? 노출 안되면 다른거로 하게끔(예외처리랑 xfail 등등 이런거 어떻게 써야하지)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilites.baseclass import BaseClass

class TestCounpang(BaseClass) :    
    def test_naver (self, setup):
        setup.get("https://www.naver.com/")
        setup.find_element(By. XPATH, "//i[@class='MyView-module__naver_logo____Y442']").click()
    


# #edge
# options.add_argument("ignoreZoomSetting")  # 줌 레벨을 무시하여 자동화가 멈추지 않도록 함
# options.add_argument("ignoreProtectedModeSettings")  # 보호 모드를 무시
# options.add_argument("requireWindowFocus")  # 윈도우 포커스를 강제로 가져오도록 함
# options.add_argument("nativeEvents")  # 네이티브 이벤트를 활성화
# options.add_argument("--disable-blink-features=AutomationControlled")  # IE에서도 사용할 수 있는지 테스트