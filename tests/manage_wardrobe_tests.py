import unittest
from unittest import mock, TestCase
from WardrobePlanner.functions.manage_wardrobe import laundry

class TestLaundry(TestCase):
    def test_laundry_clean_clotches(self):
        with mock.patch('builtins.input', return_value='y'):
            self.assertEqual("All of your clothes are clean now!", laundry(1))

    def test_laundry_skip_cleaning(self):
        with mock.patch('builtins.input', return_value='n'):
            self.assertEqual("Ok, maybe later.", laundry(1))




if __name__ == '__main__':
    unittest.main()