from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class casual_dress():
    def __init__(self, driver):
        self.driver = driver
        self.product_class = "product-container"
        self.dresses_class = "sf-with-ul"
    def click_dress(self):
        wait = WebDriverWait(self.driver, 5)
        actions = ActionChains(self.driver)
        men_menu = self.driver.find_element_by_class_name(self.product_class)
        actions.move_to_element(men_menu).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Add to cart']"))).click()
        time.sleep(10)
        self.driver.execute_script(
            "document.getElementsByClassName('continue btn btn-default button exclusive-medium')[0].click();");
    def click_tshirt(self):
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)
        men_menu = self.driver.find_element_by_class_name(self.dresses_class)
        actions.move_to_element(men_menu).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='T-shirts']"))).click()
