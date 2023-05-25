import unittest
from unittest import mock
from friends import add_friend, delete_friend, show_friends_list
from WardrobePlanner.classes.user import User




class FriendsTestCase(unittest.TestCase):
    # def test_add_friend_valid(self):
    #     user = User(1, "Anna", "MyPassword123", 'Warsaw', 52.23, 21.01)
    #     with mock.patch('builtins.input', side_effect=["Luna"]):
    #         self.assertEqual(add_friend(user), "Luna has been added to your friend list")  # add assertion here

    def test_add_friend_valid_already_friends(self):
        user = User(1, "Anna", "MyPassword123", 'Warsaw', 52.23, 21.01)
        with mock.patch('builtins.input', side_effect=["Maria"]):
            self.assertEqual(add_friend(user), "You are already friends with Maria")

    def test_add_friend_invalid(self):
        user = User(1, "Anna", "MyPassword123", 'Warsaw', 52.23, 21.01)
        with mock.patch('builtins.input', side_effect=[2]):
            self.assertEqual(add_friend(user), "Sorry, that user doesn't exist")  # add assertion here

    def test_show_friends_list_valid(self):
        user = User(1, "Anna", "MyPassword123", 'Warsaw', 52.23, 21.01)
        self.assertEqual("Here is a list of your friends: Maria, Jenny", show_friends_list(user))


if __name__ == '__main__':
    unittest.main()
