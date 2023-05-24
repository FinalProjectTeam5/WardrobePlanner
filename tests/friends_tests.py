import unittest
from unittest import mock
from friends import add_friend, delete_friend, show_friends_list

#Unsure how to pass user as argument at the moment

# class FriendsTestCase(unittest.TestCase):
#     def test_add_friend_valid(self):
#         with mock.patch('builtins.input', side_effect=["Luna"]):
#             self.assertEqual(add_friend(), "Luna has been added to your friend list")  # add assertion here
#
#     def test_add_friend_valid_already_friends(self):
#         with mock.patch('builtins.input', side_effect=["Maria"]):
#             self.assertEqual(add_friend(), "You are already friends with Maria")
#
#     def test_add_friend_invalid(self):
#         with mock.patch('builtins.input', side_effect=[2]):
#             self.assertEqual(add_friend(), "Sorry, that user doesn't exist")  # add assertion here
#
#     def test_show_friends_list_valid(self):
#         self.assertEqual("Here is a list of your friends: Maria, Jenny", show_friends_list())


if __name__ == '__main__':
    unittest.main()
