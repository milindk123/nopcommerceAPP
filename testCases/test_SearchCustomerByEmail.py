import time
import pytest

from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import Login
from pageObjects.addCustomerPage import AddCustomer
from utilities.readProprties import  ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    url=ReadConfig.getApplicationURL()
    userName=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

  #  @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("****************  Test_SearchCustomerByEmail_004 ***************")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.lp.clearAndSetUserName(self.userName)
        self.lp.clearAndSetPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Succesful *******************")

        self.logger.info("*********** starting search customer by email")
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("********** Search customer By Email ID *******************")

        self.searchcust=SearchCustomer(self.driver)
        email="james_pan@nopCommerce.com"
        self.searchcust.enteremail(email)
        self.searchcust.clicksearch()
        time.sleep(5)

        status=self.searchcust.searchCustomerByEmail("james_pan@nopCommerces.com")
        if status:
            self.logger.info(f"Customer FOUND with email: {email}")
        else:
            self.logger.error(f" Customer NOT FOUND with email: {email}")

        assert status, f"Customer with email '{email}' was NOT found"

        #assert True== status
        self.driver.close()

        self.logger.info("********** Test_SearchCustomerByEmail_004 finished *******************")




