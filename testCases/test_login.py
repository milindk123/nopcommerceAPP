import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homepagetitle(self, setup):
        self.logger.info("**Test_001_Login*****")
        self.logger.info("**Verifying Home page Title*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("**Home page title test is passed*****")

        else:
            self.driver.save_screenshot(".//ScreenShots//"+"test_homepagetitle.png")
            self.driver.close()
            self.logger.error("***Home page title test is failed*****")
            assert False

    def test_login(self, setup):
        self.logger.info("**Verifying login test*****")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clearAndSetUserName(self.username)
        self.lp.clearAndSetPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**Login test is passed*****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//ScreenShots//"+"test_login.jpeg")
            self.driver.close()
            self.logger.error("**Login test is failed*****")
            assert False