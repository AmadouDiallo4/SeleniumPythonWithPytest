import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
    rdFemaleGender_id = "Gender_Female"
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
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrator_xpath)
        elif role == 'Guests':
            # we can Guest only or Registered
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//li[@class='k-button k-state-hover']//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)
        time.sleep(3)
        self.driver.execute_script("argument[0].click;", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_id))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

