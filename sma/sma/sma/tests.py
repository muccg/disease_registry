from django.test import TestCase

from django.core.management import call_command

class LettuceLoginTests(TestCase):
    def test_patient(self):
        call_command('harvest', 'sma/sma/features/login.feature')
        call_command('harvest', 'sma/sma/features/report_links.feature')

class LettuceReportLinksTests(TestCase):
    def test_report_links(self):
        call_command('harvest', 'sma/sma/features/report_links.feature')
