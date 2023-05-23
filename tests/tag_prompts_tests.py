from unittest import TestCase, mock
from WardrobePlanner.functions.tag_prompts import users_choices, whether_weather

class Test_TagPrompts(TestCase):
    def test_whether_weather_valid_input_y(self):
        with mock.patch('builtins.input', return_value='y'):
            self.assertTrue(whether_weather())

    def test_whether_weather_valid_input_n(self):
        with mock.patch('builtins.input', return_value='n'):
            self.assertFalse(whether_weather())


            
            
            
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
