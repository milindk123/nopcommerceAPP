import time
import pytest
from selenium import webdriver
from utilities.customLogger import LogGen
from utilities import XLUtils
from utilities.readProprties import ReadConfig

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"


    logger=LogGen.loggen()

    def test_login__ddt(self, setup):
        self.driver =setup
        self.driver.get(self.baseURL)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in a Excel:",self.rows)
        list_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.clearAndSetUserName(self.user)
            self.lp.clearAndSetPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.lp.clickLogOut()
                    list_status.append("pass")
                elif self.exp=='Fail':
                    self.lp.clickLogOut()
                    list_status.append("fail")
            elif act_title!=exp_title:
                    if self.exp=="Pass":
                        list_status.append("fail")
                    elif self.exp=='Fail':
                        list_status.append("pass")

        if "Fail" not in list_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
