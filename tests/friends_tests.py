import unittest
from unittest import mock
from friends import add_friend, delete_friend, show_friends_list


# class FriendsTestCase(unittest.TestCase):
#     def test_add_friend_valid(self):
#         with mock.patch('builtins.input', side_effect=["Sarah"]):
#             self.assertEqual("Sarah has been added to your friend list", add_friend(1))  # add assertion here
#
#     def test_add_friend_valid_already_friends(self):
#         with mock.patch('builtins.input', side_effect=["Maria"]):
#             self.assertEqual("You are already friends with Maria.", add_friend(1))
#
#     def test_add_friend_invalid(self):
#         with mock.patch('builtins.input', side_effect=["Luna"]):
#             self.assertEqual("Sorry, that isn't a valid user. Please try again.", add_friend(1))  # add assertion here
#
#     def test_show_friends_list_valid(self):
#         self.assertEqual("Here is a list of your friends: [(2, 'Maria'), (3, 'Jenny')]", show_friends_list(1))

#
# if __name__ == '__main__':
#     unittest.main()
