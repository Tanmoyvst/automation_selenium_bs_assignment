
class sign_in():
    def __init__(self, driver):
        self.driver = driver
        self.email_id = "email"
        self.pass_id = "passwd"
        self.submitButton = "SubmitLogin"
    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(email)
    def enter_password(self, password):
        self.driver.find_element_by_id(self.pass_id).clear()
        self.driver.find_element_by_id(self.pass_id).send_keys(password)
    def click_signin(self):
        self.driver.find_element_by_id(self.submitButton).click()


