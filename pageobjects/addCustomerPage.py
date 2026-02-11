import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testCases import test_AddCustomer

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']/p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p"
    Reg_button_cancle_xpath="//span[@class='select2-selection__choice__remove']"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtcustomerRoles_xpath = "//ul[@class='select2-selection__rendered']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//*[@id='select2-VendorId-container']"
    drpmgrOfVendor1_xpath = "//li[contains(text(),'Vendor 1')]"
    drpmgrOfVendor2_xpath = "//li[text()='Vendor 2']"
    drpmgrOfnotvendor_xpath="//*[@id='select2-VendorId-result-hoxe-0']"
    txtAdminContent_xpath=("//textarea[@id='AdminComment']")
    btnSave_xpath="//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        #self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,self.lnkCustomers_menu_xpath))).click()

    def clickOnCustomersMenuItem(self):
        #self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menuitem_xpath))).click()
        try:  #
            # Find the 'x' button specifically for the 'Registered' tag
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH,self.Reg_button_cancle_xpath))).click()
            time.sleep(5)  # Visual pause to see removal
        except:
            # If 'Registered' isn't there, just move on
            pass

    def clickOnAddnew(self):
        #self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.btnAddnew_xpath))).click()

    def setEmail(self, email):
        #self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.txtEmail_xpath))).send_keys(email)

    def setPassword(self, password):
        #self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,self.txtPassword_xpath))).send_keys(password)

    def setCustomerRoles(self, roles):

        wait = WebDriverWait(self.driver, 20)

        # -------- REMOVE DEFAULT ROLE --------
        try:
            while True:
                removes = self.driver.find_elements(
                    By.XPATH,
                    "//span[contains(@class,'select2-selection_choice_remove')]"
                )
                if len(removes) == 0:
                    break

                for r in removes:
                    r.click()
                    time.sleep(0.5)
        except:
            pass

        # make list
        if isinstance(roles, str):
            roles = [roles]

        for role in roles:
            # -------- OPEN DROPDOWN --------
            role_box = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//ul[contains(@class,'select2-selection__rendered')]")
            ))
            role_box.click()

            # -------- WAIT FOR RESULT PANEL --------
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//ul[contains(@class,'select2-results__options')]")
            ))

            # -------- XPATH + DEBUG PRINTS --------
            option_xpath = (
                f"//li[contains(@class,'select2-results__option') "
                f"and normalize-space()='{role}']"
            )

            print("Trying to select role:", role)
            print("XPath used:", option_xpath)

            option = wait.until(EC.element_to_be_clickable(
                (By.XPATH, option_xpath)
            ))

            self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
            option.click()

            time.sleep(0.7)

    def setManagerOfVendor(self, vendor):

        wait = WebDriverWait(self.driver, 25)

        # ---- CLOSE CUSTOMER ROLE DROPDOWN IF STILL OPEN ----
        try:
            self.driver.find_element(By.TAG_NAME, "body").click()
            time.sleep(1)
        except:
            pass

        # ---- OPEN VENDOR DROPDOWN ----
        vendor_box = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@id='select2-VendorId-container']")
        ))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", vendor_box)
        vendor_box.click()

        # ---- WAIT FOR OPTIONS PANEL ----
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ul[contains(@class,'select2-results__options')]")
        ))

        # ---- OPTION XPATH ----
        option_xpath = (
            f"//li[contains(@class,'select2-results__option') "
            f"and normalize-space()='{vendor}']"
        )

        print("Trying to select vendor:", vendor)
        print("Vendor XPath:", option_xpath)

        option = wait.until(EC.presence_of_element_located(
            (By.XPATH, option_xpath)
        ))

        self.driver.execute_script("arguments[0].click();", option)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()