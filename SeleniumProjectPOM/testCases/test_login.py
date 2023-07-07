import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from  utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************************** Test_001_Login ******************************")
        self.logger.info("*************************Verifying Home Page Title *********************")
        self.driver = setup
        self.driver.get(self.baseURL)

        Expexted_Title = "Your store. Login"
        Actual_Title = self.driver.title

        if Actual_Title == Expexted_Title:
            assert True
            self.driver.close()
            self.logger.info("*************************Home page title test is passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************************Home page title test is failed *********************")
            assert False

    def test_login(self,setup):
        self.logger.info("************************* Veriying Login test *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()

        Actual_Title = self.driver.title
        Expected_Title = "Dashboard / nopCommerce administration"

        if Actual_Title == Expected_Title:
            assert True
            self.logger.info("************************* Login test is passed *********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************************* Login test is failed *********************")
            assert False