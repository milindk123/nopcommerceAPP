import pytest
from selenium import webdriver
from utilities.customLogger import LogGen
from utilities.readProprties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()
    def test_homepagetitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".//ScreenShots//"+"test_homepagetitle.png")
            self.driver.close()
            assert False
    def test_login(self, setup):
        self.driver =setup
        self.driver.get(self.baseURL)
        self.lp.clearAndSetUserName(self.username)
        self.lp.clearAndSetPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//ScreenShots//"+"test_login.jpeg")
            self.driver.close()
            assert False