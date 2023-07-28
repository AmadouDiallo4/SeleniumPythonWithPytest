import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from  utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XUtilities
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestDatas/LoginData.xlsx"

    logger = LogGen.loggen() # logger


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("**************************Test_002_DDT_Login **********************")
        self.logger.info("************************* Veriying Login DD test *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        ''' username and password from execl file '''
        self.rows = XUtilities.getRowCount(self.path, 'Sheet1')
        print("Number of Rows ... ", self.rows)
        lst_status = [] # empty list

        for r in range(2,self.rows+1):
            self.user = XUtilities.readData(self.path, 'Sheet1', r, 1)
            self.password = XUtilities.readData(self.path, 'Sheet1', r, 2)
            self.exp = XUtilities.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassWord(self.password)
            self.lp.clickLogin()
            time.sleep(5)


            Actual_Title = self.driver.title
            Expected_Title = "Dashboard / nopCommerce administration"

            if Actual_Title == Expected_Title:
                if self.exp == "Pass":
                    self.logger.info("**** Passed *******")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed *******")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif Actual_Title != Expected_Title:
                if self.exp == "Pass":
                    self.logger.info("**** Failed *******")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** Passed *******")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("************** Login DDT Test passed  ****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("************** Login DDT Test failed  ****************")
            self.driver.close()
            assert False

        self.logger.info("************** End of Login DDT Test   ****************")
        self.logger.info("************** Completed TC_Login_DDT_002   ****************")