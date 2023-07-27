import time

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchByCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    fname_search = "Victoria"
    lname_search = "Terces"

    def test_searchName(self, setup):
        self.logger.info("*********** Test_005_SearchCustomerByName ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login successful ************")

        self.logger.info("*********** Starting Search customer By Name ***********")

        self.custom = AddCustomer(self.driver)
        self.custom.clickOnCustomerMenu()
        self.custom.clickOnCustomerMenuItem()

        self.logger.info("****************** searching customer by nameID ************")
        search = SearchByCustomer(self.driver)
        search.setSearchFirstName(self.fname_search)
        search.setSearchLastName(self.lname_search)

        search.clickSearchButton()
        time.sleep(5)
        status = search.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("************ TC_SearchCustomerByName_005 Finished *******")
        self.driver.close()
