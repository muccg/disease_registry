"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

from pyvirtualdisplay import Display
from selenium import webdriver

class SimpleTest(TestCase):
    def test_molecular_data_page(self):
        display = Display(visible=0, size=(800, 600))
        display.start()
                
        browser = webdriver.Firefox()
        
        browser.get("http://192.168.251.178:8080/admin/")

        usernameInput = browser.find_element_by_name("username")
        usernameInput.send_keys("admin")
        passwordInput = browser.find_element_by_name("password")
        passwordInput.send_keys("admin")

        passwordInput.submit()

        self.assertEqual('Site administration | Django site admin', browser.title)

        browser.get("http://192.168.251.178:8080/admin/genetic/moleculardata/")

        self.assertIsNotNone(browser.find_element_by_xpath("//*[contains(.,'Select molecular data to change')]"))

        browser.get("http://192.168.251.178:8080/admin/logout")

        self.assertEqual('Logged out | Django site admin', browser.title)

        browser.quit()
        display.stop()