import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions                                           
from selenium.webdriver.edge.options import Options as EdgeOptions

chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 감지 방지
chrome_options.add_argument("--disable-gpu")  # GPU 가속 비활성화
chrome_options.add_argument("--disable-software-rasterizer")  # 소프트웨어 래스터라이저 비활성화
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")  # user-agent 전달

edge_options = EdgeOptions()
edge_options.add_argument("--disable-blink-features=AutomationControlled")
edge_options.add_argument("--disable-gpu")
edge_options.add_argument("--disable-software-rasterizer")
edge_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")

driver = None

def pytest_addoption(parser): # 터미널 실행 시 명령어를 통해 브라우저 선택(기본-크롬 브라우저)
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options) # 크롬 드라이버
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=edge_options) # 엣지 드라이버    
    driver.get("https://www.coupang.com/")  # URL 접속
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()
    
# 스크린샷 저장 절대 경로
REPORT_PATH = r"C:/Users\shehd/OneDrive/바탕 화면/rohpython/coupangTestAutomation/Reports/"

# 실패 시 스크린샷 저장 및 HTML 연결
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('setup')
        nodeid = item.nodeid
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f'{nodeid}_{datetime.now().strftime("%Y-%m-%d_%H_%M")}.png'.replace("/", "_").replace("::", "_").replace(".py", "")
            img_path = os.path.join(REPORT_PATH, file_name)
            driver.save_screenshot(img_path)
            screenshot = driver.get_screenshot_as_base64()
           
            image_html = f"""
                <div class="lightbox">
                    <img src="data:image/png;base64,{screenshot}" alt="Screenshot" class="thumbnail" onclick="openLightbox(this.src)">
                </div>
            """
            extra.append(pytest_html.extras.html(image_html))
           
            extra.append(pytest_html.extras.html('''
                <style>
                    .lightbox img { width: 100px; cursor: pointer; }
                </style>
            '''))
            extra.append(pytest_html.extras.html('''
                <script>
                    function openLightbox(src) {
                        var lightbox = document.createElement('div');
                        lightbox.style.position = 'fixed';
                        lightbox.style.top = '0';
                        lightbox.style.left = '0';
                        lightbox.style.width = '100%';
                        lightbox.style.height = '100%';
                        lightbox.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
                        lightbox.style.zIndex = '1000';
                        lightbox.onclick = function() { document.body.removeChild(lightbox); };

                        var img = document.createElement('img');
                        img.src = src;
                        img.style.position = 'absolute';
                        img.style.top = '50%';
                        img.style.left = '50%';
                        img.style.transform = 'translate(-50%, -50%)';
                        img.style.maxWidth = '90%';
                        img.style.maxHeight = '90%';

                        lightbox.appendChild(img);
                        document.body.appendChild(lightbox);
                    }
                </script>
            '''))
        report.extra = extra
