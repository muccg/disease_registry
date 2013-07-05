from lettuce import *

from selenium import webdriver
import lettuce_webdriver.webdriver

from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))

@before.all
def set_browser():
    display.start()
    world.browser = webdriver.Firefox()

@after.all
def clean_after_tests(result):
    world.browser.quit()
    display.stop()