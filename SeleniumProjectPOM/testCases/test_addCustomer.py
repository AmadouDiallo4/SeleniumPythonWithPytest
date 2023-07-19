import time

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login successful ************")

        self.logger.info("************ starting Add Customer Test *******")
        self.addCust = AddCustomer(self.driver)
        time.sleep(5)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuItem()

        #self.driver.close()
