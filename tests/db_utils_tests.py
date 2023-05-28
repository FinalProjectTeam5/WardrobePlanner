from unittest import TestCase, main, mock
from unittest.mock import patch
from WardrobePlanner.classes.db_utils import DBSearch, connect_to_db


class Test_DBUtils(TestCase):
    def test_username_check_if_returns_all_users(self):
        """This function is always returning a list of all created users, regardless of existing / non-existing username
        - so only 1 test has been created"""
        username = "Anna"
        result = DBSearch.username_check()
        expected = [('Anna',), ('Maria',), ('Jenny',), ('Lucy',), ('Kim',), ('Olga',)]
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
        expected = [(1, 'green denim trousers', 'available'), (2, 'blue green trousers', 'available'),
                    (3, 'pink denim trousers', 'available'), (4, 'grey suit pants', 'available'),
                    (5, 'black suit pants', 'available'), (6, 'red suit pants', 'available'),
                    (7, 'green suit pants', 'available'), (8, 'orange midi skirt', 'available'),
                    (9, 'black midi skirt', 'available'), (10, 'black long skirt', 'dirty'),
                    (11, 'green long skirt', 'dirty'), (12, 'yellow mini skirt', 'available'),
                    (13, 'orange mini skirt', 'available'), (14, 'red mini skirt', 'available'),
                    (15, 'pink mini skirt', 'available'), (16, 'flower midi skirt', 'available'),
                    (17, 'Printed T-shirt', 'available'), (18, 'Black T-shirt', 'available'),
                    (19, 'Turquoise blouse', 'available'), (20, 'Red blouse', 'available'),
                    (21, 'White T-shirt', 'available'), (22, 'Grey hoodie', 'available'),
                    (23, 'Blue hoodie', 'available'), (24, 'Grey wool cardigan', 'available'),
                    (25, 'Yellow wool cardigan', 'available'), (26, 'Duck down jacket', 'available'),
                    (27, 'Blue duck down jacket', 'available'), (28, 'Black wool coat', 'available'),
                    (29, 'Black wool coat', 'available'), (30, 'Dark grey hoodie', 'dirty'),
                    (31, 'Dark grey hoodie', 'available'), (32, 'yoga pants', 'available'),
                    (33, 'yoga pants', 'available'), (34, 'brown wool dress', 'available'),
                    (35, 'green cotton dress', 'available'), (36, 'green cotton dress', 'available'),
                    (37, 'blue poliester dress', 'available'), (38, 'red silk dress', 'available'),
                    (39, 'silver sequin dress', 'available'), (40, 'navy blue jumpsuit', 'available')]
        self.assertEqual(expected, result)

    def test_show_all_user_clothes_non_existing_user(self):
        user_id = 500
        result = DBSearch.show_all_user_clothes(user_id)
        expected = []
        self.assertEqual(expected, result)

    def test_get_friend_user_id_valid_input(self):
        username = "Maria"
        result = DBSearch.get_friend_user_id(username)
        expected = [(2,)]
        self.assertEqual(expected, result)

    def test_get_friend_user_id_invalid_input(self):
        username = "XYZ"
        result = DBSearch.get_friend_user_id(username)
        expected = []
        self.assertEqual(expected, result)

    def test_get_friends_list_valid_input(self):
        user_id = 1
        result = DBSearch.get_friends_list(user_id)
        expected = [(2, 'Maria'), (3, 'Jenny'), (4, 'Lucy')]
        self.assertEqual(expected, result)

    def test_get_friends_list_invalid_input(self):
        user_id = "p"
        result = DBSearch.get_friends_list(user_id)
        expected = []
        self.assertEqual(expected, result)

    def test_show_count_of_clothes_available_valid_input(self):
        user_id = 1
        result = DBSearch.show_count_of_clothes_available(user_id)
        expected = [(37,)]
        self.assertEqual(expected, result)

    def test_show_count_of_clothes_available_invalid_input(self):
        user_id = 100
        result = DBSearch.show_count_of_clothes_available(user_id)
        expected = [(0,)]
        self.assertEqual(expected, result)

    def test_show_count_of_clothes_dirty_valid_input(self):
        user_id = 1
        result = DBSearch.show_count_of_clothes_dirty(user_id)
        expected = [(3,)]
        self.assertEqual(expected, result)

    def test_show_count_of_clothes_dirty_invalid_input(self):
        user_id = 100
        result = DBSearch.show_count_of_clothes_dirty(user_id)
        expected = [(0,)]
        self.assertEqual(expected, result)

    def test_get_all_users_and_ids_if_returns_all(self):
        """This function is always returning a list of all created users and their ids, regardless of existing / non-existing username
        - so only 1 test has been created"""
        result = DBSearch.get_all_users_and_ids()
        expected = [(1, 'Anna'), (2, 'Maria'), (3, 'Jenny'), (4, 'Lucy'), (5, 'Kim'), (6, 'Olga')]
        self.assertEqual(expected, result)

    def test_get_location_valid_input(self):
        user_id = 1
        result = DBSearch.get_location(user_id)
        expected = [('Warszawa, województwo mazowieckie, Polska', 52.23, 21.01)]
        self.assertEqual(expected, result)

    def test_get_location_invalid_input(self):
        user_id = 100
        result = DBSearch.get_location(user_id)
        expected = []
        self.assertEqual(expected, result)

    @patch('WardrobePlanner.classes.db_utils.connect_to_db')
    def test_create_new_user(self, mock_connect_to_db):
        # Mock the return value of connect_to_db
        mock_db_connection = mock_connect_to_db.return_value
        mock_cursor = mock_db_connection.cursor.return_value

        # Call the function with test data
        username = 'Tina'
        password = 'Strong'
        DBSearch.create_new_user(username, password)

        # Assert that the expected methods are called
        mock_connect_to_db.assert_called_once()
        mock_db_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            """INSERT INTO users (user_name, user_password) VALUES (%s, %s);""",
            [username, password]
        )
        mock_db_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('WardrobePlanner.classes.db_utils.connect_to_db')
    def test_set_hometown(self, mock_connect_to_db):
        # Mock the return value of connect_to_db
        mock_db_connection = mock_connect_to_db.return_value
        mock_cursor = mock_db_connection.cursor.return_value

        # Call the function with test data
        user_id = 2
        hometown = "Warsaw"
        lat = 52.23
        long = 21.01
        DBSearch.set_hometown(user_id, hometown, lat, long)

        # Assert that the expected methods are called
        mock_connect_to_db.assert_called_once()
        mock_db_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            """INSERT INTO user_location (user_id, home_town, latitude, longitude) VALUES (%s, %s, %s, %s);""",
            [user_id, hometown, lat, long])

        mock_db_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('WardrobePlanner.classes.db_utils.connect_to_db')
    def test_add_to_friend_list(self, mock_connect_to_db):
        # Mock the return value of connect_to_db
        mock_db_connection = mock_connect_to_db.return_value
        mock_cursor = mock_db_connection.cursor.return_value

        # Call the function with test data
        user_id = 1
        friend_id = 4

        DBSearch.add_to_friend_list(user_id, friend_id)

        # Assert that the expected methods are called
        mock_connect_to_db.assert_called_once()
        mock_db_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            """INSERT INTO friends (user_id, friend_id) VALUES (%s, %s)""", [user_id, friend_id])

        mock_db_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('WardrobePlanner.classes.db_utils.connect_to_db')
    def test_delete_from_friend_list(self, mock_connect_to_db):
        # Mock the return value of connect_to_db
        mock_db_connection = mock_connect_to_db.return_value
        mock_cursor = mock_db_connection.cursor.return_value

        # Call the function with test data
        user_id = 1
        friend_id = 4

        DBSearch.delete_from_friend_list(friend_id, user_id)

        # Assert that the expected methods are called
        mock_connect_to_db.assert_called_once()
        mock_db_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            """DELETE FROM friends AS f WHERE f.friend_id = %s AND f.user_id = %s""",
            [friend_id, user_id])

        mock_db_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('WardrobePlanner.classes.db_utils.connect_to_db')
    def test_do_laundry(self, mock_connect_to_db):
        # Mock the return value of connect_to_db
        mock_db_connection = mock_connect_to_db.return_value
        mock_cursor = mock_db_connection.cursor.return_value

        # Call the function with test data
        user_id = 1

        DBSearch.do_laundry(user_id)

        # Assert that the expected methods are called
        mock_connect_to_db.assert_called_once()
        mock_db_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("""UPDATE availability_status AS a
                                    INNER JOIN ownership AS o ON a.item_id = o.item_id
                                    SET item_status = 'available'
                                    WHERE a.item_status = 'dirty'
                                    AND o.owner_id = %s;""", [user_id])

        mock_db_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('WardrobePlanner.classes.db_utils.connect_to_db')
    def test_add_item_to_wardrobe(self, mock_connect_to_db):
        # Mock the return value of connect_to_db
        mock_db_connection = mock_connect_to_db.return_value
        mock_cursor = mock_db_connection.cursor.return_value

        # Call the function with test data
        item_id = 200
        item_type = "bottom"
        item_description = "orange flower skirt"
        weather_tag = "mild"
        occasion_tag = "work"
        mood_tag = "cheerful"

        DBSearch.add_item_to_wardrobe(item_id, item_type, item_description, weather_tag, occasion_tag, mood_tag)

        # Assert that the expected methods are called
        mock_connect_to_db.assert_called_once()
        mock_db_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("""INSERT INTO clothes 
                                (item_ID, item_type, item_description, weather_tag, occasion_tag, mood_tag) 
                                VALUES (%s,%s,%s,%s,%s,%s);""",
                                                    [item_id, item_type, item_description, weather_tag, occasion_tag,
                                                     mood_tag])

        mock_db_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('WardrobePlanner.classes.db_utils.connect_to_db')
    def test_delete_item_from_wardrobe(self, mock_connect_to_db):
        # Mock the return value of connect_to_db
        mock_db_connection = mock_connect_to_db.return_value
        mock_cursor = mock_db_connection.cursor.return_value

        # Call the function with test data
        item_id = 6

        DBSearch.delete_item_from_wardrobe(item_id)

        # Assert that the expected methods are called
        mock_connect_to_db.assert_called_once()
        mock_db_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_any_call("""DELETE FROM availability_status AS a WHERE a.item_id = %s;""",
                                            [item_id])
        mock_cursor.execute.assert_any_call("""DELETE FROM clothes AS c WHERE c.item_id = %s;""",
                                            [item_id])

        mock_db_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    def test_search_clothes_no_tags(self):
        tags = ""
        user_id = 1
        result = DBSearch.search_clothes(tags, user_id)
        expected = [('green denim trousers', 1, 1),
                    ('blue green trousers', 2, 1),
                    ('pink denim trousers', 3, 1),
                    ('grey suit pants', 4, 1),
                    ('black suit pants', 5, 1),
                    ('red suit pants', 6, 1),
                    ('green suit pants', 7, 1),
                    ('orange midi skirt', 8, 1),
                    ('black midi skirt', 9, 1),
                    ('yellow mini skirt', 12, 1),
                    ('orange mini skirt', 13, 1),
                    ('red mini skirt', 14, 1),
                    ('pink mini skirt', 15, 1),
                    ('flower midi skirt', 16, 1),
                    ('Printed T-shirt', 17, 1),
                    ('Black T-shirt', 18, 1),
                    ('Turquoise blouse', 19, 1),
                    ('Red blouse', 20, 1),
                    ('White T-shirt', 21, 1),
                    ('Grey hoodie', 22, 1),
                    ('Blue hoodie', 23, 1),
                    ('Grey wool cardigan', 24, 1),
                    ('Yellow wool cardigan', 25, 1),
                    ('Duck down jacket', 26, 1),
                    ('Blue duck down jacket', 27, 1),
                    ('Black wool coat', 28, 1),
                    ('Black wool coat', 29, 1),
                    ('Dark grey hoodie', 31, 1),
                    ('yoga pants', 32, 1),
                    ('yoga pants', 33, 1),
                    ('brown wool dress', 34, 1),
                    ('green cotton dress', 35, 1),
                    ('green cotton dress', 36, 1),
                    ('blue poliester dress', 37, 1),
                    ('red silk dress', 38, 1),
                    ('silver sequin dress', 39, 1),
                    ('navy blue jumpsuit', 40, 1),
                    ('Blue denim jacket', 41, 2),
                    ('blue trousers', 43, 2),
                    ('pink cotton trousers', 44, 2),
                    ('greyish suit pants', 45, 2),
                    ('dark grey suit pants', 46, 2),
                    ('orange suit pants', 47, 2),
                    ('darnk green suit pants', 48, 2),
                    ('red long skirt', 49, 2),
                    ('woolen midi skirt', 50, 2),
                    ('brown long skirt', 51, 2),
                    ('blue long skirt', 52, 2),
                    ('yellow skirt', 53, 2),
                    ('orange skirt', 54, 2),
                    ('red mini skirt', 55, 2),
                    ('pink mini skirt', 56, 2),
                    ('printed midi skirt', 57, 2),
                    ('Animal print T-shirt', 58, 2),
                    ('White T-shirt', 59, 2),
                    ('Purple blouse', 60, 2),
                    ('Red blouse', 61, 2),
                    ('Golden T-shirt', 62, 2),
                    ('White hoodie', 63, 2),
                    ('Black hoodie', 64, 2),
                    ('Beige cardigan', 65, 2),
                    ('White wool cardigan', 66, 2),
                    ('Red jacket', 67, 2),
                    ('Duck down jacket', 68, 2),
                    ('Black coat', 69, 2),
                    ('Dark grey hoodie', 71, 2),
                    ('Light blue hoodie', 72, 2),
                    ('yellow yoga pants', 73, 2),
                    ('yoga pants', 74, 2),
                    ('brown cotton dress', 75, 2),
                    ('green dress', 76, 2),
                    ('cotton dress', 77, 2),
                    ('poliester dress', 78, 2),
                    ('silk dress', 79, 2),
                    ('sequin dress', 80, 2),
                    ('golden jumpsuit', 81, 2),
                    ('Grey denim jacket', 82, 2),
                    ('blue denim trousers', 83, 3),
                    ('black denim trousers', 84, 3),
                    ('black T-shirt', 85, 3),
                    ('beige suit pants', 86, 3),
                    ('black suit pants', 87, 3),
                    ('black long sleeve shirt', 88, 3),
                    ('white long sleeve shirt', 89, 3),
                    ('navy denim trousers', 91, 3),
                    ('navy denim shorts', 92, 3),
                    ('black denim shorts', 93, 3),
                    ('blue mini skirt', 94, 3),
                    ('black mini skirt', 95, 3),
                    ('grey long leggins', 96, 3),
                    ('black long leggins', 97, 3),
                    ('black long skirt', 98, 3),
                    ('Printed T-shirt', 99, 3),
                    ('Black T-shirt', 100, 3),
                    ('white blouse', 102, 3),
                    ('White T-shirt', 103, 3),
                    ('black hoodie', 104, 3),
                    ('blue hoodie', 105, 3),
                    ('grey wool cardigan', 107, 3),
                    ('black jacket', 108, 3),
                    ('blue denim jacket', 109, 3),
                    ('black wool coat', 110, 3),
                    ('beige wool coat', 111, 3),
                    ('dark grey hoodie', 112, 3),
                    ('grey hoodie', 113, 3),
                    ('black yoga pants', 114, 3),
                    ('blue cotton dress', 116, 3),
                    ('white cotton dress', 117, 3),
                    ('red cotton dress', 118, 3),
                    ('multicolor dress', 119, 3),
                    ('multicolor cotton dress', 120, 3),
                    ('black dress', 121, 3),
                    ('navy dress', 122, 3),
                    ('white T-shirt', 123, 3)]
        self.assertEqual(expected, result)

    def test_search_clothes_all_tags(self):
        tags = "AND c.occasion_tag = 'home' AND c.mood_tag = 'neutral' AND c.weather_tag = 'freezing'"
        user_id = 1
        result = DBSearch.search_clothes(tags, user_id)
        expected = [('green denim trousers', 1, 1), ('grey wool cardigan', 107, 3)]
        self.assertEqual(expected, result)

    @patch('WardrobePlanner.classes.db_utils.connect_to_db')
    def test_change_to_dirty(self, mock_connect_to_db):
        # Mock the return value of connect_to_db
        mock_db_connection = mock_connect_to_db.return_value
        mock_cursor = mock_db_connection.cursor.return_value

        # Call the function with test data
        item_id = 1

        DBSearch.change_to_dirty(item_id)

        # Assert that the expected methods are called
        mock_connect_to_db.assert_called_once()
        mock_db_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            """UPDATE availability_status SET item_status = 'dirty' WHERE item_ID = %s ;""", [item_id])

        mock_db_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()


if __name__ == '__main__':
    main()
