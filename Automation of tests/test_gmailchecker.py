import unittest
from gmailcheck import gmail_check


class TestGmailCheck(unittest.TestCase):

    def test_email_with_invalid_domain(self):
        self.assertFalse(gmail_check('johnmoore@gmail.org'))

    def test_email_with_only_letters(self):
        self.assertTrue(gmail_check('johnmoore@gmail.com'))

    def test_email_with_valid_characters(self):
        self.assertTrue(gmail_check('john.moore1@gmail.com'))

    def test_namestartswithhyphen(self):
        self.assertFalse(gmail_check('john=moore@gmail.com'))

    def test_email_too_short(self):
        self.assertFalse(gmail_check("j1@gmail.com "))

    def test_email_start_with_point(self):
        self.assertFalse(gmail_check('.johnmoore@gmail.com'))

    def test_email_with_more_tha_one_period(self):
        self.assertFalse(gmail_check('john..moore@gmail.com'))
