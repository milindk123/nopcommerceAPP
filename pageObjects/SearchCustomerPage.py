from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchCustomer:
        txtemailbox_id = "SearchEmail"
        txtfirstnamebox_name = "SearchFirstName"
        txtlastnamebox_id = "SearchLastName"
        btnsearch_id = "search-customers"

        table_xpath = "(//table[contains(@class,'table table-bordered table')])[2]"

        tablerow_xpath = "(//table[contains(@class,'table table-bordered table')])[2]//tbody/tr"

        tablecolumn_xpath = "(//table[contains(@class,'table table-bordered table')])[2]//tbody/tr/td"

        def __init__(self, driver):
            self.driver = driver

        def enteremail(self, mail):
            self.driver.find_element(By.ID,self.txtemailbox_id).clear()
            self.driver.find_element(By.ID,self.txtemailbox_id).send_keys(mail)


        def enterfirstname(self, firstname):
            self.driver.find_element(By.ID, self.txtfirstnamebox_name).clear()
            self.driver.find_element(By.ID, self.txtfirstnamebox_name).send_keys(firstname)


        def enterlastname(self, lastname):
            self.driver.find_element(By.ID, self.txtlastnamebox_id).clear()
            self.driver.find_element(By.ID, self.txtlastnamebox_id).send_keys(lastname)


        def clicksearch(self):
            wait = WebDriverWait(self.driver, 10)

            btn = wait.until(
                EC.element_to_be_clickable((By.ID, self.btnsearch_id))
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                btn
            )

            btn.click()




        def getNoOfRow(self):
            return len(self.driver.find_elements(By.XPATH, self.tablerow_xpath))

        def getNoOfcolumn(self):
            return len(self.driver.find_elements(By.XPATH, self.tablecolumn_xpath))


        def searchCustomerByEmail(self, email):
            flag=False
            for r in range(1, self.getNoOfRow() + 1):
                table=self.driver.find_element(By.XPATH,self.table_xpath)
                emailid =table.find_element(By.XPATH,"(//table[contains(@class,'table table-bordered table')])[2]//tbody/tr["+str(r)+"]/td[2]").text
                if emailid== email:
                    flag=True
                    break
            return flag


        def searchCustomerByName(self, name):
            flag = False
            for r in range(1, self.getNoOfRow() + 1):
                table = self.driver.find_element(By.XPATH, self.table_xpath)
                Name= table.find_element(By.XPATH,"(//table[contains(@class,'table table-bordered table')])[2]//tbody/tr["+str(r)+"]/td[3]").text
                if Name==name:
                    flag=True
                    break
            return flag

