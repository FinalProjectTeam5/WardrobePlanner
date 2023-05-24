from unittest import TestCase, main, mock
from WardrobePlanner.functions.login import fetch_password, verify_password


class TestLogin(TestCase):
    def test_fetch_password_True(self):
        self.assertEqual("MyPassword123", fetch_password("Anna")[0][0])

    def test_fetch_password_non_existing_user(self):
        self.assertEqual([], fetch_password("Kasia"))

    def test_verify_password_True(self):
        self.assertTrue(verify_password("MyPassword123", [("MyPassword123", "Awwww")]))




