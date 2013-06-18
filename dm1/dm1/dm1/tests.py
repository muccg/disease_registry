import urllib2

from django.test import TestCase
from django.test import LiveServerTestCase
from django.test.client import Client

from pyvirtualdisplay import Display
from selenium import webdriver

class SimpleTest(LiveServerTestCase):
    USERNAME = "admin"
    PASSWORD = "admin"
    
    def setUp(self):
        self.DISPLAY = Display(visible=0, size=(800, 600))
        self.DISPLAY.start()
        self.DRIVER = webdriver.Firefox()
        self.login()
        
    def tearDown(self):
        self.logout()
        self.DRIVER.quit()
        self.DISPLAY.stop()
    
    def test_response_all_pages(self):
        links = self.DRIVER.find_elements_by_tag_name("a")
        
        for link in links:
            attr = link.get_attribute("href")
            if "logout" not in attr:
                response_code = self.get_response_code(attr)
                print "%s -> %s" % (attr, response_code)
                self.assertEqual(int(response_code), 200)

    def test_molecular_data_page(self):
        self.DRIVER.get(self.url("/admin/genetic/moleculardata/"))
        self.assertIsNotNone(self.DRIVER.find_element_by_xpath("//*[contains(.,'Select molecular data to change')]"))
    
    def login(self):
        self.DRIVER.get(self.url("/admin/"))
        usernameInput = self.DRIVER.find_element_by_name("username")
        usernameInput.send_keys(self.USERNAME)
        passwordInput = self.DRIVER.find_element_by_name("password")
        passwordInput.send_keys(self.PASSWORD)
        passwordInput.submit()

    def logout(self):
        self.DRIVER.get(self.url("/admin/logout/"))
        self.assertEqual('Logged out | Django site admin', self.DRIVER.title)

    def get_response_code(self, url):
        response = urllib2.urlopen(url)
        return response.getcode()

    def url(self, path):
        "Return the full URL for path on the Django live testing server."
        return "%s%s" % (self.live_server_url, path)