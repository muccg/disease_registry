from django.test import TestCase
from groups.ip import *
from groups.models import IPRange


class IPTest(TestCase):
    def test_is_cidr_netmask(self):
        self.assertTrue(is_cidr_netmask("0.0.0.0"))
        self.assertTrue(is_cidr_netmask("255.0.0.0"))
        self.assertTrue(is_cidr_netmask("255.255.0.0"))
        self.assertTrue(is_cidr_netmask("255.255.255.0"))
        self.assertTrue(is_cidr_netmask("255.255.255.240"))
        self.assertTrue(is_cidr_netmask("255.255.255.255"))

        self.assertFalse(is_cidr_netmask("255.0.255.255"))
        self.assertFalse(is_cidr_netmask("255.0.0.255"))
        self.assertFalse(is_cidr_netmask("255.255.255.253"))

        self.assertRaises(ValueError, lambda: is_cidr_netmask("0.0.0."))
        self.assertRaises(ValueError, lambda: is_cidr_netmask("0.0.0.0."))
        self.assertRaises(ValueError, lambda: is_cidr_netmask("0.0.0.256"))
        self.assertRaises(ValueError, lambda: is_cidr_netmask("0.0.0.x"))

    def test_to_int(self):
        self.assertEqual(to_int("0.0.0.0"), 0)
        self.assertEqual(to_int("1.2.3.4"), 16909060)
        self.assertEqual(to_int("10.0.0.0"), 167772160)
        self.assertEqual(to_int("255.255.255.255"), 4294967295)

        self.assertRaises(ValueError, lambda: to_int("0.0.0."))
        self.assertRaises(ValueError, lambda: to_int("0.0.0.0."))
        self.assertRaises(ValueError, lambda: to_int("0.0.0.256"))
        self.assertRaises(ValueError, lambda: to_int("0.0.0.x"))


class IPRangeTest(TestCase):
    def assert_matches(self, range):
        # Test boundary values.
        self.assertFalse(range.match("9.255.255.255"))
        self.assertFalse(range.match("10.0.1.0"))
        self.assertTrue(range.match("10.0.0.0"))
        self.assertTrue(range.match("10.0.0.255"))

        # Test non-boundary values.
        self.assertFalse(range.match("0.0.0.0"))
        self.assertFalse(range.match("255.255.255.255"))
        self.assertTrue(range.match("10.0.0.127"))

    def test_match(self):
        self.assert_matches(IPRange(address="10.0.0.0", netmask="255.255.255.0"))
        self.assert_matches(IPRange(address="10.0.0.127", netmask="255.255.255.0"))

    def test_match_validation(self):
        range = IPRange(address="10.0.0.0", netmask="255.0.0.0")

        self.assertRaises(ValueError, lambda: range.match("0.0.0."))
        self.assertRaises(ValueError, lambda: range.match("0.0.0.0."))
        self.assertRaises(ValueError, lambda: range.match("0.0.0.256"))
        self.assertRaises(ValueError, lambda: range.match("0.0.0.x"))
