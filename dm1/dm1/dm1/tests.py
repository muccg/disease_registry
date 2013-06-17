"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import LiveServerTestCase

from pyvirtualdisplay import Display
from selenium import webdriver

class SimpleTest(LiveServerTestCase):
    def test_molecular_data_page(self):
        display = Display(visible=0, size=(800, 600))
        display.start()

        browser = webdriver.Firefox()

        browser.get(self.url("/admin/"))

        usernameInput = browser.find_element_by_name("username")
        usernameInput.send_keys("admin")
        passwordInput = browser.find_element_by_name("password")
        passwordInput.send_keys("admin")

        passwordInput.submit()

        self.assertEqual('Site administration | Django site admin', browser.title)

        browser.get(self.url("/admin/genetic/moleculardata/"))

        self.assertIsNotNone(browser.find_element_by_xpath("//*[contains(.,'Select molecular data to change')]"))

        browser.get(self.url("/admin/logout"))

        self.assertEqual('Logged out | Django site admin', browser.title)

        browser.quit()
        display.stop()

    def url(self, path):
        "Return the full URL for path on the Django live testing server."
        return "%s%s" % (self.live_server_url, path)
