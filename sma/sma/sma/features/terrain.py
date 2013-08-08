import os
import random
import string

from lettuce import *

from selenium import webdriver
import lettuce_webdriver.webdriver

from django.test.utils import setup_test_environment, teardown_test_environment
from django.core.management import call_command

from django.db import connection
from django.conf import settings

if "DISPLAY" not in os.environ:
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(800, 600))
else:
    display = None

@before.all
def set_browser():
#    setup_test_environment()
#    connection.creation.create_test_db()
    if display: display.start()
    world.browser = webdriver.Firefox()

@after.all
def clean_after_tests(result):
#    connection.creation.destroy_test_db()
#    teardown_test_environment()
    world.browser.quit()
    if display: display.stop()