import time

import pytest
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    driver=None
    if browser=="chrome":
        driver=webdriver.Chrome()
        driver.maximize_window()
        print("Launching Chrome browser......")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        print("Launching firefox browser")
    else:
        driver=webdriver.Chrome() # default chrome browser if browser is not supported
    yield driver
    driver.quit()


def pytest_addoption(parser): # this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return the browser value to setup method
    return request.config.getoption("--browser")

############# pytest HTML  Report ######################
# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    if hasattr(config,'_metadata'):
        config._metadata['project Name']='nop commerce'
        config._metadata['module Name'] = 'customer'
        config._metadata['Tester'] = 'Milind'

# It is hook for delete/modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
# @pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)


