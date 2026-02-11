import pytest
from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
        options = webdriver.ChromeOptions()
        # This helps hide the "automation" flag
        options.add_argument("--disable-blink-features=AutomationControlled")
        # This removes the "Chrome is being controlled by automated software" bar
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver=webdriver.Chrome(options=options)
        driver.maximize_window()
        print("Launching Chrome browser......")
        return driver

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

