import time
class auth():
    def __init__(self, driver):
        self.driver = driver
        self.customer_fn = "customer_firstname"
        self.customer_ln = "customer_lastname"
        self.customer_email = "email"
        self.password = "passwd"
        self.fn = "firstname"
        self.ln = "lastname"
        self.company = "company"
        self.address1 = "address1"
        self.address2 = "address2"
        self.city = "city"
        self.state = "id_state"
        self.zip = "postcode"
        self.country = "id_country"
        self.info = "other"
        self.phone = "phone"
        self.mobile = "phone_mobile"
        self.alias = "alias"

        self.submitButton = "submitAccount"

    def click_title(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='id_gender1']").click()
    def enter_customer_firstname(self, customer_firstname):
        self.driver.find_element_by_id(self.customer_fn).clear()
        self.driver.find_element_by_id(self.customer_fn).send_keys(customer_firstname)
    def enter_customer_lastname(self, customer_lastname):
        self.driver.find_element_by_id(self.customer_ln).clear()
        self.driver.find_element_by_id(self.customer_ln).send_keys(customer_lastname)
    def enter_email(self, email):
        self.driver.find_element_by_id(self.customer_email).clear()
        self.driver.find_element_by_id(self.customer_email).send_keys(email)
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(password)
    def enter_firstname(self, firstname):
        self.driver.find_element_by_id(self.fn).clear()
        self.driver.find_element_by_id(self.fn).send_keys(firstname)
    def enter_lastname(self, lastname):
        self.driver.find_element_by_id(self.ln).clear()
        self.driver.find_element_by_id(self.ln).send_keys(lastname)
    def enter_company(self, company):
        self.driver.find_element_by_id(self.company).clear()
        self.driver.find_element_by_id(self.company).send_keys(company)
    def enter_address1(self, address1):
        self.driver.find_element_by_id(self.address1).clear()
        self.driver.find_element_by_id(self.address1).send_keys(address1)
    def enter_address2(self, address2):
        self.driver.find_element_by_id(self.address2).clear()
        self.driver.find_element_by_id(self.address2).send_keys(address2)
    def enter_city(self, city):
        self.driver.find_element_by_id(self.city).clear()
        self.driver.find_element_by_id(self.city).send_keys(city)
    def enter_state(self, state):
        self.driver.find_element_by_id(self.state).send_keys(state)
    def enter_postalcode(self, postalcode):
        self.driver.find_element_by_id(self.zip).clear()
        self.driver.find_element_by_id(self.zip).send_keys(postalcode)
    def enter_country(self, country):
        self.driver.find_element_by_id(self.country).send_keys(country)
    def enter_extra(self, extra):
        self.driver.find_element_by_id(self.info).clear()
        self.driver.find_element_by_id(self.info).send_keys(extra)
    def enter_phone(self, phone):
        self.driver.find_element_by_id(self.phone).clear()
        self.driver.find_element_by_id(self.phone).send_keys(phone)
    def enter_mobile_phone(self, mobile_phone):
        self.driver.find_element_by_id(self.mobile).clear()
        self.driver.find_element_by_id(self.mobile).send_keys(mobile_phone)
    def enter_alias(self, alias):
        self.driver.find_element_by_id(self.alias).clear()
        self.driver.find_element_by_id(self.alias).send_keys(alias)
    def click_create_account(self):
        time.sleep(10)
        self.driver.find_element_by_id(self.submitButton).click()
