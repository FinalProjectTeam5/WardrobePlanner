import unittest
from unittest import TestCase, mock
from WardrobePlanner.functions.tag_prompts import users_choices, whether_weather


class Test_WhetherWeather(TestCase):
    def test_whether_weather_valid_input_y(self):
        with mock.patch('builtins.input', return_value='y'):
            self.assertTrue(whether_weather())

    def test_whether_weather_valid_input_n(self):
        with mock.patch('builtins.input', return_value='n'):
            self.assertFalse(whether_weather())


    def test_whether_weather_invalid_input(self):
        with mock.patch('builtins.input', side_effect=['a', '123', 'Y', 'N']):
            with self.assertRaises(ValueError):
                whether_weather()


if __name__ == '__main__':
    unittest.main()
