import time
import unittest
import warnings
import random, string
from stages.main_menu import main_menu
from stages.sign_up import sign_up
from stages.sign_in import sign_in
from stages.user_home import user_home
from stages.tshirt import tshirt
from stages.cart_menu import cart_menu
from stages.casual_dress import casual_dress
from stages.auth import auth
from stages.sign_out import signingout
from selenium import webdriver



class webtester(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome('T:\selenium\chromedriver_win32\chromedriver.exe')
        self.driver.get("http://automationpractice.com/index.php")
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)


    def test_signup(self):
        driver = self.driver
        signout = signingout(driver)
        email1 =''.join(random.choice(string.digits) for _ in range(10)) + '@Qmail.com'
        email2 =''.join(random.choice(string.digits) for _ in range(10)) + '@Qmail.com'
        password = "thanosbad"
        def signup(driver, email, cus_fn, cus_ln, cus_email, pswrd, fn, ln,company, adrs1, adrs2, city, state, zip, country, info, ph, mph, alias):
            homepage = main_menu(driver)
            homepage.loginClick()
            signupp = sign_up(driver)
            signupp.emailInput(email)
            signupp.create_click()
            authn = auth(driver)
            authn.click_title()
            authn.enter_customer_firstname(cus_fn)
            authn.enter_customer_lastname(cus_ln)
            authn.enter_email(cus_email)
            authn.enter_password(pswrd)
            authn.enter_firstname(fn)
            authn.enter_lastname(ln)
            authn.enter_company(company)
            authn.enter_address1(adrs1)
            authn.enter_address2(adrs2)
            authn.enter_city(city)
            authn.enter_state(state)
            authn.enter_postalcode(zip)
            authn.enter_country(country)
            authn.enter_extra(info)
            authn.enter_phone(ph)
            authn.enter_mobile_phone(mph)
            authn.enter_alias(alias)
            authn.click_create_account()
        def task(emails, password):
            signin = sign_in(self.driver)
            signin.enter_email(emails)
            signin.enter_password(password)
            signin.click_signin()
            userhome = user_home(self.driver)
            userhome.dress_select()
            casuladressess = casual_dress(self.driver)
            casuladressess.click_dress()
            casuladressess.click_tshirt()
            tShirt = tshirt(self.driver)
            tShirt.blue_section()
            tShirt.click_tshirt_checkout()
            cart = cart_menu(self.driver)
            cart.checkout()
            cart.delivery_address()
            cart.shipping_address()
            cart.payment()
            cart.final()
            signout = signingout(self.driver)
            signout.click_signout()
        signup(driver, email1, "Bruce", "Wayne", email1, password, "Bruce", "Wayne", "Wayne Enterprise", "Gotham", "dhaka", "Dhaka", "dhaka", "22211", "Bangladesh", "I hate joker", "01768686868", "99882233", "Batman")
        signout.click_signout()
        signup(driver, email2, "Clark", "Kent", email2, password, "Clark", "Kent", "Daily Planet","Metropolis", "dhaka", "Dhaka", "dhaka", "22212", "Bangladesh", "I wear glasses", "017696969", "0011556622", "Superman")
        signout.click_signout()
        task(email1, password)
        task(email2, password)

    @classmethod
    def tab_close(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
