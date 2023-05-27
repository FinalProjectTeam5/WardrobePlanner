from unittest import TestCase, main, mock
from unittest.mock import patch
from WardrobePlanner.functions.login import fetch_password, verify_password, get_new_password, login, show_user_id


class TestLogin(TestCase):
    def test_fetch_password_True(self):
        self.assertEqual("MyPassword123", fetch_password("Anna")[0][0])

    def test_fetch_password_False(self):
        self.assertIsNot("MyPassword123", fetch_password("Maria")[0][0])

    def test_fetch_password_non_existing_user(self):
        self.assertEqual([], fetch_password("Kasia"))

    def test_verify_password_True(self):
        self.assertTrue(verify_password("MyPassword123", [("MyPassword123", "Awwww")]))

    def test_get_new_username_valid_input(self):
        with mock.patch('builtins.input', side_effect=["LongPassword"]):
            self.assertTrue(get_new_password("Anna"))

    def test_login_valid_input(self):
        with mock.patch('builtins.input', side_effect=["Anna", "MyPassword123"]):
            self.assertEqual(login(), "Anna")

    def test_show_user_id(self):
        with mock.patch('WardrobePlanner.classes.db_utils.DBSearch.get_user_id', return_value=1):
            self.assertEqual(show_user_id("Anna"), 1)


