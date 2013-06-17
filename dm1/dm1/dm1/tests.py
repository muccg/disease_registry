import urllib2

from django.test import TestCase
from django.test.client import Client

from pyvirtualdisplay import Display
from selenium import webdriver

class SimpleTest(TestCase):
    USERNAME = "curator"
    PASSWORD = "curator"
    HOST = "http://192.168.251.178:8080"
    
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
        self.DRIVER.get("%s/admin/genetic/moleculardata/" % self.HOST)
        self.assertIsNotNone(self.DRIVER.find_element_by_xpath("//*[contains(.,'Select molecular data to change')]"))

    def get_response_code(self, url):
        response = urllib2.urlopen(url)
        return response.getcode()
    
    def login(self):
        self.DRIVER.get("%s/admin/" % self.HOST)
        usernameInput = self.DRIVER.find_element_by_name("username")
        usernameInput.send_keys(self.USERNAME)
        passwordInput = self.DRIVER.find_element_by_name("password")
        passwordInput.send_keys(self.PASSWORD)
        passwordInput.submit()
    
    def logout(self):
        self.DRIVER.get("%s/admin/logout" % self.HOST)
        self.assertEqual('Logged out | Django site admin', self.DRIVER.title)