import unittest
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from WardrobePlanner.classes.user import User
from WardrobePlanner.functions.search.search_dashboard import search_dashboard
from WardrobePlanner.functions.search.pre_search_notifications import generate_no_search_possible_notification, \
    generate_no_hometown_notification, is_hometown_set, does_user_have_clothes, does_user_have_friends
from WardrobePlanner.functions.search.tag_prompts import formatting_tags
from WardrobePlanner.functions.search.results_handling import display_results, establishing_ownership
from WardrobePlanner.functions.search.api_requests import formatting_today_request_link, getting_temperature_today



class TestSearchDashboard(TestCase):
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


class TestTagPrpompts(TestCase):
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


class TestHandlingResults(TestCase):
    def test_display_results_1_item_found(self):
        user = User(1, "Anna", "MyPassword123", 'Warszawa, województwo mazowieckie, Polska', 52.23, 21.01)
        search_results = [('black T-shirt', 85, 3)]
        result = display_results(search_results, user)
        expected = [1]
        self.assertEqual(result, expected)

    def test_display_results_no_item_found(self):
        user = User(1, "Anna", "MyPassword123", 'Warszawa, województwo mazowieckie, Polska', 52.23, 21.01)
        search_results = []
        result = display_results(search_results, user)
        expected = []
        self.assertEqual(result, expected)

    def test_establishing_ownership_item_belongs_to_user(self):
        user = User(1, "Anna", "MyPassword123", 'Warszawa, województwo mazowieckie, Polska', 52.23, 21.01)
        chosen_item = ('green suit pants', 7, 1)
        result = establishing_ownership(user, chosen_item)
        expected = "you"
        self.assertEqual(result, expected)

    def test_establishing_ownership_item_belongs_to_friend(self):
        user = User(1, "Anna", "MyPassword123", 'Warszawa, województwo mazowieckie, Polska', 52.23, 21.01)
        chosen_item = ('black dress', 121, 3)
        result = establishing_ownership(user, chosen_item)
        expected = "Jenny"
        self.assertEqual(result, expected)


class TestApiRequests(TestCase):
    def test_formatting_today_request_link(self):
        expected = "https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&daily" \
                   "=apparent_temperature_max&forecast_days=1&timezone=auto"
        result = formatting_today_request_link(52.23, 21.01)
        self.assertEqual(result, expected)

    def setUp(self):
        self.user = MagicMock()
        self.user.latitude = 52.23
        self.user.longitude = 21.01

    @patch('requests.get')
    def test_getting_temperature_today(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "daily": {
                "apparent_temperature_max": [25]
            }
        }
        mock_requests_get.return_value = mock_response

        result = getting_temperature_today(self.user)

        mock_requests_get.assert_called_once_with(formatting_today_request_link(self.user.latitude, self.user.longitude))
        self.assertEqual(result, 25)


if __name__ == '__main__':
    unittest.main()