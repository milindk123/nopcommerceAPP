import time
import pytest

from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import Login
from pageObjects.addCustomerPage import AddCustomer
from utilities.readProprties import  ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    url=ReadConfig.getApplicationURL()
    userName=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("****************  Test_SearchCustomerByEmail_004 ***************")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.lp.clearAndSetUserName(self.userName)
        self.lp.clearAndSetPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Succesful *******************")

        self.logger.info("*********** starting search customer by name")
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("********** Search customer By Name *******************")

        self.searchcust=SearchCustomer(self.driver)
        name="Milind"
        lname="Kambale"

        self.searchcust.enterfirstname(name)
        self.searchcust.enterlastname(lname)
        self.searchcust.clicksearch()
        time.sleep(5)

        status=self.searchcust.searchCustomerByName("Milind Kambale")
        if status:
            self.logger.info(f"Customer FOUND with name: {name and lname}")
            print(f"Customer FOUND with name: {name and lname}")
        else:
            self.logger.error(f" Customer NOT FOUND with email: {name}")
            self.driver.save_screenshot(".//ScreenShots/search_name_fail.png")


        assert status, f"Customer with name '{name and lname}' was NOT found"


        #assert True== status
        self.driver.close()

        self.logger.info("********** Test_SearchCustomerByEmail_005 finished *******************")




