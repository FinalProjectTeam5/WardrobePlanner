import unittest
from geopy import Nominatim
from unittest import TestCase
from unittest.mock import patch
from WardrobePlanner.functions.date_and_geolocation.check_city import check_city, hometown_input_check
from WardrobePlanner.functions.date_and_geolocation.cleaning_up_results import cleaning_up_results, \
    creating_true_false_list, eliminating_duplicates, rounding_up_lat_long
from WardrobePlanner.functions.date_and_geolocation.city_list_for_interface import city_list_for_interface
from WardrobePlanner.classes.dashboard_class import Menu


class TestCheckCity(TestCase):
    def test_hometown_input_check_valid_input(self):
        expected = "generate_list"
        result = hometown_input_check("Rome")
        self.assertEqual(expected, result)

    @patch.object(Menu, 'get_users_choice')
    def test_get_users_choice_search_again(self, fake_get_users_choice):
        fake_get_users_choice.return_value = True
        no_results_menu = Menu("", ["Search again.", "Proceed without a hometown."])
        result = no_results_menu.get_users_choice()
        expected = True
        self.assertEqual(result, expected)

    @patch.object(Menu, 'get_users_choice')
    def test_get_users_choice_proceed_without_hometown(self, fake_get_users_choice):
        fake_get_users_choice.return_value = False
        no_results_menu = Menu("", ["Search again.", "Proceed without a hometown."])
        result = no_results_menu.get_users_choice()
        expected = False
        self.assertEqual(result, expected)

    def test_check_city_existing_city(self):
        list_of_geopy_objects = check_city("Falenica")
        result = [list(item) for item in
                  list_of_geopy_objects]  # this line is needed because raw geopy results can't be truned into a variable just by pasting them, only like this I could create an 'expected' variable
        expected = [['Falenica, Wawer, Warszawa, województwo mazowieckie, Polska', (52.1608783, 21.211679)],
                    ['Falenica, Jaźwiny, gmina Borowie, powiat garwoliński, województwo mazowieckie, 08-412, Polska',
                     (51.9612839, 21.7782269)],
                    ['Falenica, Bysławska, Falenica, Wawer, Warszawa, województwo mazowieckie, 04-970, Polska',
                     (52.1594362, 21.2045542)]]
        self.assertEqual(result, expected)

    def test_check_city_city_not_exist(self):
        result = check_city(
            "kjlEFjkgjk")  # this keymash doesn't return results, shockingly many keymashes I tried before this returned legitimate results, it's a very robust module
        expected = None
        self.assertEqual(result, expected)


class Test_LocationResultsHandling(TestCase):

    def test_cleaning_up_results_non_empty_list_passed(self):
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode("Falenica", exactly_one=False)
        result = cleaning_up_results(location)
        expected = [('Falenica, Wawer, Warszawa, województwo mazowieckie, Polska', (52.16, 21.21)), (
            'Falenica, Jaźwiny, gmina Borowie, powiat garwoliński, województwo mazowieckie, 08-412, Polska',
            (51.96, 21.78)), ('Falenica, Bysławska, Falenica, Wawer, Warszawa, województwo mazowieckie, 04-970, Polska',
                              (52.16, 21.2))]
        self.assertEqual(result, expected)

    def test_cleaning_up_results_empty_list_passed(self):
        result = cleaning_up_results([])
        expected = []
        self.assertEqual(result, expected)

    def test_creating_true_false_list_non_empty_list_passed(self):
        result = creating_true_false_list(['Falenica, Wawer, Warszawa, województwo mazowieckie, Polska',
                                           'Falenica, Jaźwiny, gmina Borowie, powiat garwoliński, województwo mazowieckie, 08-412, Polska',
                                           'Falenica, Bysławska, Falenica, Wawer, Warszawa, województwo mazowieckie, 04-970, Polska'])
        expected = [True, True, True]
        self.assertEqual(result, expected)

    def test_creating_true_false_list_empty_list_passed(self):
        result = creating_true_false_list([])
        expected = []
        self.assertEqual(result, expected)

    def test_eliminating_duplicates_non_empty_list_passed(self):
        result = eliminating_duplicates(['Falenica, Wawer, Warszawa, województwo mazowieckie, Polska',
                                         'Falenica, Jaźwiny, gmina Borowie, powiat garwoliński, województwo mazowieckie, 08-412, Polska',
                                         'Falenica, Bysławska, Falenica, Wawer, Warszawa, województwo mazowieckie, 04-970, Polska'])
        expected = ['Wawer', 'Jaźwiny', 'Bysławska']
        self.assertEqual(result, expected)

    def test_eliminating_duplicates_empty_list_passed(self):
        result = eliminating_duplicates([])
        expected = []
        self.assertEqual(result, expected)

    def test_rounding_up_lat_long_non_empty_list_passed(self):
        result = rounding_up_lat_long([(52.1608783, 21.211679), (51.9612839, 21.7782269), (52.1594362, 21.2045542)])
        expected = [(52.16, 21.21), (51.96, 21.78), (52.16, 21.2)]
        self.assertEqual(result, expected)

    def test_rounding_up_lat_long_empty_list_passed(self):
        result = rounding_up_lat_long([])
        expected = []
        self.assertEqual(result, expected)

    def test_city_list_for_interface_non_empty_list_passed(self):
        result = city_list_for_interface(
            [('Falenica, Wawer, Warszawa, województwo mazowieckie, Polska', (52.16, 21.21)), (
                'Falenica, Jaźwiny, gmina Borowie, powiat garwoliński, województwo mazowieckie, 08-412, Polska',
                (51.96, 21.78)), (
                 'Falenica, Bysławska, Falenica, Wawer, Warszawa, województwo mazowieckie, 04-970, Polska',
                 (52.16, 21.2))])
        expected = ['1. Falenica, Wawer, Warszawa, województwo mazowieckie, Polska',
                    '2. Falenica, Jaźwiny, gmina Borowie, powiat garwoliński, województwo mazowieckie, 08-412, Polska',
                    '3. Falenica, Bysławska, Falenica, Wawer, Warszawa, województwo mazowieckie, 04-970, Polska',
                    "4. My hometown isn't on this list. I want to try again.",
                    "5. My hometown isn't on this list. I want to proceed without a hometown."]
        self.assertEqual(result, expected)

    def test_city_list_for_interface_empty_list_passed(self):
        result = city_list_for_interface([])
        expected = ["1. My hometown isn't on this list. I want to try again.",
                    "2. My hometown isn't on this list. I want to proceed without a hometown."]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
