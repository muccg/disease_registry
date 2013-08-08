from django.test import TestCase

from django.core.management import call_command

class LettuceTests(TestCase):
    def test_run(self):
        call_command('harvest', 'sma/sma/features/')
