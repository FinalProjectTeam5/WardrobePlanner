import unittest
from unittest import mock
from WardrobePlanner.functions.friends import add_friend, delete_friend, show_friends_list


class FriendsTestCase(unittest.TestCase):
    def test_add_friend_valid(self):
        with mock.patch('builtins.input', side_effect=['Izzy']), mock.patch(
                'WardrobePlanner.classes.db_utils.DBSearch.add_to_friend_list', return_value=["Added"]):
            self.assertEqual(add_friend(1), "Izzy has been added to your friend list.")

    def test_add_friend_valid_already_friends(self):
        with mock.patch('builtins.input', side_effect=["Jenny"]):
            self.assertEqual("You are already friends with Jenny.", add_friend(1))

    def test_add_friend_invalid(self):
        with mock.patch('builtins.input', side_effect=["Luna"]):
            self.assertEqual("Sorry, that isn't a valid user. Please try again.", add_friend(1))

    def test_add_friend_invalid_int(self):
        with mock.patch('builtins.input', side_effect=[7]):
            self.assertEqual("Sorry, that isn't a valid user. Please try again.", add_friend(1))

    def test_show_friends_list_valid(self):
        self.assertEqual("Here is a list of your friends: [(2, 'Maria'), (3, 'Jenny'), (4, 'Lucy'), (5, 'Nicole')]", show_friends_list(1))

    def test_delete_friend_valid(self):
        with mock.patch('builtins.input', side_effect=['Maria']), mock.patch(
                    'WardrobePlanner.classes.db_utils.DBSearch.delete_from_friend_list', return_value=["Deleted"]):
            self.assertEqual("Maria has been deleted from your friend list.", delete_friend(1))

    def test_delete_friend_invalid_not_user(self):
        with mock.patch('builtins.input', side_effect=["William"]):
            self.assertEqual("Sorry, that isn't a valid user. Please try again.", delete_friend(1))

    def test_delete_friend_invalid_int(self):
        with mock.patch('builtins.input', side_effect=[7]):
            self.assertEqual("Sorry, that isn't a valid user. Please try again.", delete_friend(1))


if __name__ == '__main__':
    unittest.main()
