import unittest
from signin import sign
class Signin(unittest.TestCase):
    """
    Class for runnining test
    """
    def test_creation(self):
        si = Signin()
        self.assertIsInstance(si, Signin)
    def test_empty_feilds(self):
        self.assertEqual(sign.empty_feilds(), True)        
    def test_combined_name(self):               
        self.assertEqual(sign.combined_name(), 'kalyango john')
    def test_phone_validation(self):
        self.assertEqual(sign.validate_phone(), True)
    def test_validate_email(self):
        self.assertEqual(sign.validate_email(), True)
    def test_submit_inputs(self):
        self.assertEqual(sign.submit_inputs(), "YOU HAVE LOGGED IN SUCCESS FULLY")
        