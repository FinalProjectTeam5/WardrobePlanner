from unittest import TestCase, main, mock
from WardrobePlanner.classes.db_utils import DBSearch

class Test_User(TestCase):
    def test_username_check_if_returns_all_users(self):
        """This function is always returning a list of all created users, regardless of existing / non-existing username
        - so only 1 test has been created"""
        username = "Anna"
        result = DBSearch.username_check(username)
        expected = [('Anna',), ('Maria',), ('Jenny',), ('Lucy',)]
        self.assertEqual(expected, result)

    def test_password_check_valid_input(self):
        username = "Anna"
        result = DBSearch.password_check(username)
        expected = [('MyPassword123',)]
        self.assertEqual(expected, result)

    def test_password_check_non_existing_user(self):
        username = "A"
        result = DBSearch.password_check(username)
        expected = []
        self.assertEqual(expected, result)

    def test_get_user_info_valid_input(self):
        username = "Anna"
        result = DBSearch.get_user_info(username)
        expected = [(1, 'Anna', 'MyPassword123')]
        self.assertEqual(expected, result)

    def test_get_user_info_non_existing_user(self):
        username = "Annaaa"
        result = DBSearch.get_user_info(username)
        expected = []
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()

