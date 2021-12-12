import random
import time
import unittest
import requests
from unittest import skip
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # self.driver=webdriver.Chrome("C:\Tools\Drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(
            executable_path="C:/Users/Elena Dobrovolskaia/PycharmProjects/firstPythonProject/tests/browser_drivers/chromedriver.exe")
        self.driver.get("https://www.wta.org/login")
        self.wait = WebDriverWait(self.driver, 25)
       # Select.select_by_index()

    def test_find_logo(self):
        driver = self.driver
        driver.find_element_by_id('__ac_name').send_keys('ajohnson12@example.com')
        driver.find_element_by_id('__ac_password').send_keys('12345')
        driver.find_element_by_name('submit').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='You are now logged in']")))
        logo_element = driver.find_element_by_id("main-logo").find_element_by_xpath("//a/img[@class='logo']")
        logo_size = logo_element.size
        # or just like this because logo is always first image on the page
        # driver.find_element_by_css_selector("img")
        self.assertEqual(190, logo_size.get('height'))
        self.assertTrue(logo_size.get('width') == 159)
        self.assertDictEqual({'width': 159, 'height': 190}, logo_size)

        window_size = driver.get_window_size()
        logo_location = logo_element.location
        top_right_logo_corner_x_location = logo_size.get('width') + logo_location.get('x')
        # the entire logo (width) fits within the left half of the window
        self.assertTrue(top_right_logo_corner_x_location < (window_size.get('width')/2))

    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('__ac_name').send_keys('ajohnson12@example.com')
        driver.find_element_by_id('__ac_password').send_keys('12345')
        driver.find_element_by_name('submit').click()
        time.sleep(2)
        welcome_text = driver.find_element_by_xpath("//h1[contains(text(),'You are now logged in')]").text
        self.assertEqual('You are now logged in', welcome_text)

    def test_selector(self):
        driver = self.driver
        driver.find_element_by_id('__ac_name').send_keys('ajohnson12@example.com')
        driver.find_element_by_id('__ac_password').send_keys('12345')
        driver.find_element_by_name('submit').click()
        time.sleep(2)
        welcome_text = driver.find_element_by_xpath("//h1[contains(text(),'You are now logged in')]").text
        self.assertEqual('You are now logged in', welcome_text)

    def test_invalid_password(self):
        driver = self.driver
        random_password = randint(100000, 999999)
        driver.find_element_by_id('__ac_name').send_keys('ajohnson12@example.com')
        driver.find_element_by_id('__ac_password').send_keys(random_password)
        driver.find_element_by_name('submit').click()
        time.sleep(2)
        error_message = driver.find_element_by_xpath("//p[contains(text(),' do not match.')]").text
        self.assertEqual('The email and/or password do not match.', error_message)

    def test_empty_password(self):
        driver = self.driver
        driver.find_element_by_id('__ac_name').send_keys('ajohnson12@example.com')
        driver.find_element_by_name('submit').click()
        time.sleep(2)
        error_message = driver.find_element_by_xpath("//p[contains(text(),' do not match.')]").text
        self.assertEqual('The email and/or password do not match.', error_message)

    def test_tear_down(self):
        self.driver.quit()

    skip("disabling for debugging")

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        # TODO ED just kidding


if __name__ == '__main__':
    unittest.main()
