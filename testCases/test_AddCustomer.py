import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.LoginPage import LoginPage
from pageobjects.addCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger


    def test_addCustomer(self,setup):
        self.logger.info("***** Test_003_AddCustomer ****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)

        self.lp = LoginPage(self.driver)
        self.lp.clearAndSetUserName(self.username)
        self.lp.clearAndSetPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("***** Login succesful ****")

        self.logger.info("*** Starting Add Customer Test ****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("***** Providing customer info ****")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Milind")
        self.addcust.setLastName("Kambale")
        self.addcust.setGender("Male")
        self.addcust.setCompanyName("Just_Dial")
        self.addcust.setCustomerRoles(["Administrators","Forum Moderators"])
        self.addcust.setManagerOfVendor("Vendor 2 ")

        #self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()
        self.logger.info("***** Saving customer info ****")

        self.logger.info("*** Add customer validation started *******")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("*** Add customer Test Passed ***")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("*** Add customer Test Failed ****")
            assert False

        self.driver.quit()
        self.logger.info("*** Ending Add customer test ****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
    driver.quit()