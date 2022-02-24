class cart_menu():

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.execute_script(
            "document.getElementsByClassName('button btn btn-default standard-checkout button-medium')[0].click();");
    def delivery_address(self):
        self.driver.find_element_by_name("processAddress").click()
    def shipping_address(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='cgv']").click()
        self.driver.find_element_by_name("processCarrier").click()
    def payment(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name("cheque").click()
    def final(self):
        self.driver.find_element_by_xpath("//span[normalize-space(text())='I confirm my order']").click()
