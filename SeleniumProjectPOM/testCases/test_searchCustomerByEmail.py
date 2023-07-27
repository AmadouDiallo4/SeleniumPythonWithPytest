import time

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchByCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    email_search = "victoria_victoria@nopCommerce.com"

    def test_searchEmail(self, setup):
        self.logger.info("*********** Test_004_SearchCustomerByEmail ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login successful ************")

        self.logger.info("*********** Starting Search customer By Email ***********")

        self.custom = AddCustomer(self.driver)
        self.custom.clickOnCustomerMenu()
        self.custom.clickOnCustomerMenuItem()

        self.logger.info("****************** searching customer by emailID ************")
        search = SearchByCustomer(self.driver)
        search.setSearchEmail(self.email_search)
        search.clickSearchButton()
        time.sleep(5)
        status = search.searchCustomerByEmail(self.email_search)
        assert True == status
        self.logger.info("************ TC_SearchCustomerByEmail_004 Finished *******")
        self.driver.close()
