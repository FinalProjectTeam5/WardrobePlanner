from unittest import TestCase, main, mock
from unittest.mock import patch
from WardrobePlanner.classes.db_utils import DBSearch, connect_to_db


class Test_DBUtils(TestCase):
    def test_username_check_if_returns_all_users(self):
        """This function is always returning a list of all created users, regardless of existing / non-existing username
        - so only 1 test has been created"""
        username = "Anna"
        result = DBSearch.username_check()
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
        expected = [(1, 'Anna'), (2, 'Maria'), (3, 'Jenny'), (4, 'Lucy')]
        self.assertEqual(expected, result)

    def test_get_location_valid_input(self):
        user_id = 1
        result = DBSearch.get_location(user_id)
        expected = [('Warsaw', 52.23, 21.01)]
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
                           [item_id, item_type, item_description, weather_tag, occasion_tag, mood_tag])

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



if __name__ == '__main__':
    main()



