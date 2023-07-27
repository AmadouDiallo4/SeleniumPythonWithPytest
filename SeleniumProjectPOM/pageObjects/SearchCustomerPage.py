from selenium.webdriver.common.by import By


class SearchByCustomer:
    #search by email
    searchEmail_id = "SearchEmail"
    searchButton_id = "search-customers"
    searchItem_xpath = "//div[@class='icon-search']//i[@class='fas fa-search']"
    searchFirstName_id = "SearchFirstName"
    searchLastName_id = "SearchLastName"

    tblSearchResult_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def clickSearchItem(self):
        self.driver.find_element(By.XPATH, self.searchItem_xpath)


    def setSearchEmail(self, email):
        self.driver.find_element(By.ID, self.searchEmail_id).clear()
        self.driver.find_element(By.ID, self.searchEmail_id).send_keys(email)


    def clickSearchButton(self):
        self.driver.find_element(By.ID, self.searchButton_id).click()

    def setSearchFirstName(self, fname):
        self.driver.find_element(By.ID, self.searchFirstName_id).clear()
        self.driver.find_element(By.ID, self.searchFirstName_id).send_keys(fname)

    def setSearchLastName(self, lname):
        self.driver.find_element(By.ID, self.searchLastName_id).clear()
        self.driver.find_element(By.ID, self.searchLastName_id).send_keys(lname)

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            nameid = table.find_element(By.XPATH, "//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if nameid == name:
                flag = True
                break
        return flag