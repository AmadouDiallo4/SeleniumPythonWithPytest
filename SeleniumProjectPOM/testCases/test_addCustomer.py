import random
import string
import time
from selenium.webdriver.common.by import By
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
        #time.sleep(5)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuItem()

        self.addCust.clickOnAddnew()

        self.logger.info("******************* Providing customer info ********************")

        self.mail = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.mail)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Amadou")
        self.addCust.setLastName("Diallo")
        self.addCust.setGender("Male")
        self.addCust.setDob("2/07/1985")
        self.addCust.setCompanyName("just4Test")
        self.addCust.setCustomerRoles("Administrators")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setAdminContent("This is for testing ...........")
        self.addCust.clickOnSave()

        self.logger.info("***************** Saving Customer info *************")

        self.logger.info("***************** Add customer validation started *******************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("************* Add customer Test passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_src.png") # screenshot
            self.logger.error("********** Add Customer Test Failed ******************")
            assert False

        self.driver.close()
        self.logger.info("************* Ending Add customer test *******************")



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))
