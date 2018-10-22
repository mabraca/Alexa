from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/register/')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        logout = selenium.find_element_by_id('logout')

        submit = selenium.find_element_by_name('register')

        #Fill the form with data
        username.send_keys('Test2')
        password1.send_keys('123456Test')
        password2.send_keys('123456Test')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #logout
        logout = logout.click()

    def test_table_and_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        assert "Alexa's Domains" in selenium.title
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')

        username.send_keys('Test3')
        password.send_keys('123456Test')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        url = selenium.find_element_by_id('nameURL')
        submit = selenium.find_element_by_name('getInfo')
        table = selenium.find_element_by_id('tableDomain')

        #Fill the input with data
        url.send_keys('https://www.alexa.com/topsites/category/Top/Science')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #Wait for information
        self.wait_for_item('table')
        time.sleep(3)

        #check the returned result
        assert 'Check your email' in selenium.page_source