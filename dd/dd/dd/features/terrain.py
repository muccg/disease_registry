import os
import random
import string

from lettuce import *

from selenium import webdriver
import lettuce_webdriver.webdriver

from registry import steps

if "DISPLAY" not in os.environ:
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(800, 600))
else:
    display = None

@before.all
def set_browser():
    if display: display.start()
    world.browser = webdriver.Firefox()

@before.all
def set_site_url():
    world.site_url = steps.get_site_url("dd", default_url="http://localhost:8004")

@before.all
def set_wait_seconds():
    world.wait_seconds = 3

@after.all
def clean_after_tests(result):
    world.browser.quit()
    if display: display.stop()


@before.each_scenario
def delete_cookies(scenario):
    # delete all cookies so when we browse to a url at the start we have to log in
    world.browser.delete_all_cookies()
