import pytest
import logging
import inspect
from pagesObjects.MainHome import MainHome
from pagesObjects.loginPage import loginPage
from pagesObjects.itemtList import ItemList
from pagesObjects.itemDetail import ItemDetail
from pagesObjects.itemCart import ItemCart
from pagesObjects.CheckOut import CheckOut
from pagesObjects.myCoupang import MyCoupang
from selenium.webdriver.common.action_chains import ActionChains

class BaseClass : 
    @pytest.fixture(autouse=True)
    def setup_mainhome(self, setup):
        self.mainhome = MainHome(setup)
    
    @pytest.fixture(autouse=True)    
    def setup_loginpage(self, setup):
        self.loginpage = loginPage(setup)
    
    @pytest.fixture(autouse=True)    
    def setup_itemlist(self, setup):
        self.itemlist = ItemList(setup)
    
    @pytest.fixture(autouse=True)    
    def setup_itemdetail(self, setup):
        self.itemdetail = ItemDetail(setup)  
        
    @pytest.fixture(autouse=True)    
    def setup_itemCart(self, setup):
        self.itemcart = ItemCart(setup)        
        
    @pytest.fixture(autouse=True)    
    def setup_checkOut(self, setup):
        self.checkout = CheckOut(setup)     
            
    @pytest.fixture(autouse=True)    
    def setup_action(self, setup):
        self.action = ActionChains(setup)

    @pytest.fixture(autouse=True)    
    def setup_mycoupang(self, setup):
        self.mycoupang = MyCoupang(setup)
        
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        
        logger.addHandler(filehandler)
        
        logger.setLevel(logging.INFO)
        return logger