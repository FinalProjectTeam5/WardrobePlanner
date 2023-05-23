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

 def test_show_all_user_clothes_existing_user(self):
        user_id = 1
        result = DBSearch.show_all_user_clothes(user_id)
        expected = [(1, 'green denim trousers', 'available'), (2, 'blue green trousers', 'available'), (3, 'pink denim trousers', 'available'), (4, 'grey suit pants', 'available'), (5, 'black suit pants', 'available'), (6, 'red suit pants', 'available'), (7, 'green suit pants', 'available'), (8, 'orange midi skirt', 'available'), (9, 'black midi skirt', 'available'), (10, 'black long skirt', 'dirty'), (11, 'green long skirt', 'dirty'), (12, 'yellow mini skirt', 'available'), (13, 'orange mini skirt', 'available'), (14, 'red mini skirt', 'available'), (15, 'pink mini skirt', 'available'), (16, 'flower midi skirt', 'available'), (17, 'Printed T-shirt', 'available'), (18, 'Black T-shirt', 'available'), (19, 'Turquoise blouse', 'available'), (20, 'Red blouse', 'available'), (21, 'White T-shirt', 'available'), (22, 'Grey hoodie', 'available'), (23, 'Blue hoodie', 'available'), (24, 'Grey wool cardigan', 'available'), (25, 'Yellow wool cardigan', 'available'), (26, 'Duck down jacket', 'available'), (27, 'Blue duck down jacket', 'available'), (28, 'Black wool coat', 'available'), (29, 'Black wool coat', 'available'), (30, 'Dark grey hoodie', 'dirty'), (31, 'Dark grey hoodie', 'available'), (32, 'yoga pants', 'available'), (33, 'yoga pants', 'available'), (34, 'brown wool dress', 'available'), (35, 'green cotton dress', 'available'), (36, 'green cotton dress', 'available'), (37, 'blue poliester dress', 'available'), (38, 'red silk dress', 'available'), (39, 'silver sequin dress', 'available'), (40, 'navy blue jumpsuit', 'available')]
        self.assertEqual(expected, result)

    def test_show_all_user_clothes_non_existing_user(self):
        user_id = 500
        result = DBSearch.show_all_user_clothes(user_id)
        expected = []
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
if __name__ == '__main__':
    main()

