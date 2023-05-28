import unittest
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from WardrobePlanner.classes.user import User
from WardrobePlanner.functions.search.search_dashboard import search_dashboard
from WardrobePlanner.functions.search.pre_search_notifications import generate_no_search_possible_notification, \
    generate_no_hometown_notification, is_hometown_set, does_user_have_clothes, does_user_have_friends
from WardrobePlanner.functions.search.tag_prompts import formatting_tags
from WardrobePlanner.classes.dashboard_class import Dashboard


class Test_SearchDashboard(TestCase):
    def test_search_dashboard_user_has_no_clothes_and_no_friends(self):
        user = User(6,	"Olga",	"W0rdPass", "Львів, Львівська міська громада, Львівський район, Львівська область, Україна", 49.84, 24.03)
        result = search_dashboard(user)
        expected = None
        self.assertEqual(result, expected)

    def test_generate_no_search_possible_notification_user_has_no_clothes_and_no_friends(self):
        user = User(6,	"Olga",	"W0rdPass", "Львів, Львівська міська громада, Львівський район, Львівська область, Україна", 49.84, 24.03)
        result = generate_no_search_possible_notification(user)
        expected = "You don't have any clothes in your wardrobe and your friends list is empty.\n" \
               "No search can be performed.\n" \
               "Add clothes and/or friends to use the search function."
        self.assertEqual(result, expected)

    def test_generate_no_search_possible_notification_user_has_clothes_but_no_friends(self):
        user = User(5, "Kim", "kimkim",
                    None, None, None)
        result = generate_no_search_possible_notification(user)
        expected = ""
        self.assertEqual(result, expected)

    def test_generate_no_hometown_notification_user_has_no_hometown(self):
        user = User(5, "Kim", "kimkim", None, None, None)
        result = generate_no_hometown_notification(user)
        expected = "You don't have a hometown set so weather conditions won't be included in your search."
        self.assertEqual(result, expected)

    def test_generate_no_hometown_notification_user_has_hometown(self):
        user = User(1, "Anna", "MyPassword123", 'Warszawa, województwo mazowieckie, Polska', 52.23, 21.01)
        result = generate_no_hometown_notification(user)
        expected = ""
        self.assertEqual(result, expected)

    def test_is_hometown_set_yes(self):
        user = User(1, "Anna", "MyPassword123", 'Warszawa, województwo mazowieckie, Polska', 52.23, 21.01)
        self.assertTrue(is_hometown_set(user))

    def test_is_hometown_set_no(self):
        user = User(5, "Kim", "kimkim", None, None, None)
        self.assertFalse(is_hometown_set(user))

    def test_does_user_have_clothes_yes(self):
        user = User(1, "Anna", "MyPassword123", 'Warszawa, województwo mazowieckie, Polska', 52.23, 21.01)
        self.assertTrue(does_user_have_clothes(user))

    def test_does_user_have_clothes_no(self):
        user = User(6,	"Olga",	"W0rdPass", "Львів, Львівська міська громада, Львівський район, Львівська область, Україна", 49.84, 24.03)
        self.assertFalse(does_user_have_clothes(user))

    def test_does_user_have_friends_yes(self):
        user = User(1, "Anna", "MyPassword123", 'Warszawa, województwo mazowieckie, Polska', 52.23, 21.01)
        self.assertTrue(does_user_have_friends(user))

    def test_does_user_have_friends_no(self):
        user = User(6,	"Olga",	"W0rdPass", "Львів, Львівська міська громада, Львівський район, Львівська область, Україна", 49.84, 24.03)
        self.assertFalse(does_user_have_friends(user))


class Test_TagPrpompts(TestCase):
    def test_formatting_tags_3_tags_specified_list(self):
        result = formatting_tags(["sport", "serious", "freezing"])
        expected = " AND c.occasion_tag = 'sport'  AND c.mood_tag = 'serious'  AND c.weather_tag = 'freezing' "
        self.assertEqual(result, expected)

    def test_formatting_tags_2_tags_specified_list(self):
        result = formatting_tags(["sport", "serious", ""])
        expected = " AND c.occasion_tag = 'sport'  AND c.mood_tag = 'serious' "
        self.assertEqual(result, expected)

    def test_formatting_tags_1_tag_specified_list(self):
        result = formatting_tags(["", "serious", ""])
        expected = " AND c.mood_tag = 'serious' "
        self.assertEqual(result, expected)

    def test_formatting_tags_no_tags_specified_list(self):
        result = formatting_tags(["", "", ""])
        expected = ""
        self.assertEqual(result, expected)

    def test_formatting_tags_too_short_list(self):
        with self.assertRaises(IndexError):
            formatting_tags(["sport", "freezing"])




if __name__ == '__main__':
    unittest.main()