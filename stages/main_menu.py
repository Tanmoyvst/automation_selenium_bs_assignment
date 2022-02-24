class main_menu():

    def __init__(self, driver):
        self.driver = driver
        self.login = "login"
    def loginClick(self):
        self.driver.find_element_by_class_name(self.login).click()


