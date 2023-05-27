from unittest import TestCase, main, mock
import unittest
from WardrobePlanner.functions.manage_wardrobe import add_item, delete_item, laundry


class ManageWardrobeTesting(TestCase):
    def test_add_item_valid(self):
        with mock.patch('builtins.input', side_effect=[1, 1, 1, 1, 1]), mock.patch(
                'WardrobePlanner.classes.db_utils.DBSearch.add_item_to_wardrobe'):
            self.assertTrue(add_item(300))

    def test_delete_item_valid(self):
        mock.item_to_delete_id = 2
        with mock.patch('builtins.input', side_effect=[1]), mock.patch(
                'WardrobePlanner.classes.db_utils.DBSearch.delete_item_from_wardrobe'), mock.patch(
                'WardrobePlanner.classes.db_utils.DBSearch.get_item_id'):
            self.assertTrue(delete_item())


class TestLaundry(TestCase):
    def test_laundry_clean_clothes(self):
        with mock.patch('builtins.input', side_effect=['y']), mock.patch(
                'WardrobePlanner.classes.db_utils.DBSearch.do_laundry', return_value=["Done"]):
            self.assertEqual("All of your clothes are clean now!", laundry(1))

    def test_laundry_skip_cleaning(self):
        with mock.patch('builtins.input', side_effect=['n']), mock.patch(
                'WardrobePlanner.classes.db_utils.DBSearch.do_laundry', return_value=["Done"]):
            self.assertEqual("Ok, maybe later.", laundry(1))


if __name__ == '__main__':
    unittest.main()
