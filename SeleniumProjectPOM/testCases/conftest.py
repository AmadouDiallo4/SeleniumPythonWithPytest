from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("\n*********************launching Chrome browser............")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("\n**********************launching Firefox browser............")
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):  # this will get the value from CLI (hooks)
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")


############# pytest HTML report ########################
# it is hook for adding environment info to HTML Report
'''def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    #config._metadata['Project Name'] = 'nop Commerce tuto'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Amadou'

# it is hook for delete/modify environment info to HTML Report"
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

'''
