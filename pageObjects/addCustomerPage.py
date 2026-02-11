import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AddCustomer:

    # ---------- LOCATORS ----------
    lnkCustomers_menu_xpath = "//a[@href='#']/p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p"

    btnAddnew_xpath = "//a[contains(@class,'btn-primary') and normalize-space()='Add new']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"

    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"

    txtCompanyName_xpath = "//input[@id='Company']"

    # Select2 Customer Roles
    txtcustomerRoles_xpath = "//span[contains(@class,'select2-selection--multiple')]"
    btnRegisteredCancle_xpath="(//span[contains(@class,'select2-selection')])[2]"
    txtBoxCustomerRole_xpath="//input[contains(@class,'select2-search__field')]"

    # Select2 Manager Vendor
    mgr_vendor_dropdown_xpath = "//span[@id='select2-VendorId-container']"

    txtAdminContent_xpath = "//textarea[@id='AdminComment']"

    btnSave_xpath = "//button[@name='save']"

    # ---------- INIT ----------
    def __init__(self, driver):
        self.driver = driver

    # ---------- ACTIONS ----------
    def clickOnCustomersMenu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menu_xpath))
        ).click()

    def clickOnCustomersMenuItem(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menuitem_xpath))
        ).click()

    def clickOnAddnew(self):

        wait = WebDriverWait(self.driver, 30)

        addnew_btn = wait.until(EC.element_to_be_clickable((By.XPATH, self.btnAddnew_xpath)))

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", addnew_btn)

        # JS click avoids animation / overlay issues
        self.driver.execute_script("arguments[0].click();", addnew_btn)

    def setEmail(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.txtEmail_xpath))
        ).send_keys(email)

    def setPassword(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.txtPassword_xpath))
        ).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    # ---------- SIMPLE SELECT2 ROLE ----------
    def setCustomerRoles(self, role):

        wait = WebDriverWait(self.driver, 15)

        # open dropdown
        role_box = wait.until(EC.element_to_be_clickable((By.XPATH, self.txtcustomerRoles_xpath)))
        role_box.click()
        time.sleep(1)

        # if Registered exists -> remove it
        registered = self.driver.find_elements(By.XPATH,self.btnRegisteredCancle_xpath)
        if registered:
            registered[0].click()
            time.sleep(1)

        # search box
        search_box = wait.until(EC.visibility_of_element_located((By.XPATH,self.txtBoxCustomerRole_xpath)))

        search_box.clear()
        search_box.send_keys(role)

        # select role
        option = wait.until(EC.element_to_be_clickable(( By.XPATH,f"//li[contains(@class,'select2-results__option') and text()='{role}']")))
        option.click()
        time.sleep(1)

        # verify role added
        added_role = self.driver.find_elements(By.XPATH,f"//li[contains(@class,'select2-selection__choice') and contains(.,'{role}')]")

        if added_role:
            print(f" Role '{role}' added successfully")
        else:
            raise Exception(f" Role '{role}' was NOT added")

    def scrollDown(self):
         element=self.driver.find_element(By.XPATH,"//span[@id='select2-VendorId-container']")
         self.driver.execute_script("arguments[0].scrollIntoView();",element)

    def pauseScript(self):
         time.sleep(5)
    # ---------- SIMPLE SELECT2 MANAGER ----------
    def setManagerOfVendor(self, value):

        wait = WebDriverWait(self.driver, 10)

        # Open dropdown
        wait.until(EC.element_to_be_clickable((By.XPATH, self.mgr_vendor_dropdown_xpath))).click()

        # Click value
        wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(@class,'select2-results__option') and text()='{value}']"))).click()

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
