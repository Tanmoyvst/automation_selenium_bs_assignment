class sign_up():
    def __init__(self, driver):
        self.driver = driver
        self.email_id = "email_create"
        self.createButton = "SubmitCreate"
    def emailInput(self, email):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(email)
    def create_click(self):
        self.driver.find_element_by_id(self.createButton).click()