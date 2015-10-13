# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, string

class NewPatient(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8002"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_new_patient(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[17]").click()
        driver.find_element_by_id("id_consent").click()
        Select(driver.find_element_by_id("id_working_group")).select_by_visible_text("Western Australia")
        driver.find_element_by_id("id_family_name").clear()
        driver.find_element_by_id("id_family_name").send_keys(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
        driver.find_element_by_id("id_given_names").clear()
        driver.find_element_by_id("id_given_names").send_keys(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
        Select(driver.find_element_by_id("date_of_birth_day")).select_by_visible_text("2")
        Select(driver.find_element_by_id("date_of_birth_month")).select_by_visible_text("February")
        driver.find_element_by_id("date_of_birth_year").send_keys("1984")
        Select(driver.find_element_by_id("id_sex")).select_by_visible_text("Male")
        driver.find_element_by_id("id_address").clear()
        driver.find_element_by_id("id_address").send_keys("Address")
        driver.find_element_by_id("id_suburb").clear()
        driver.find_element_by_id("id_suburb").send_keys("Suburb")
        Select(driver.find_element_by_id("id_state")).select_by_visible_text("Western Australia")
        driver.find_element_by_id("id_postcode").clear()
        driver.find_element_by_id("id_postcode").send_keys("6666")
        driver.find_element_by_id("id_patientdoctor_set-0-relationship").send_keys("Primary Care")
        Select(driver.find_element_by_id("id_patientdoctor_set-0-doctor")).select_by_visible_text("EXAMPLE John")
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Log out").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
