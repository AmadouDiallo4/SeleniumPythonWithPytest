import time

from selenium.webdriver.common.by import By


class AddCustomer:
    #add customer page
    lnkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtCustomerRoles_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-focused k-state-hover k-state-border-down']//div[@role='listbox']"
    lstitemAdministrator_xpath = "//span[normalize-space()='Administrators']"
    lstitemRegistered_xpath = "//span[normalize-space()='Registered']"
    lstitemGuest_xpath = "//span[normalize-space()='Guests']"
    lstitemVendor_xpath = "//span[normalize-space()='Vendors']"
    drpmgrOfVendor_id ="//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFemalGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.driver.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.driver.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.driver.txtCustomer_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role== 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrator_xpath)
        elif role == 'Gustes':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)
