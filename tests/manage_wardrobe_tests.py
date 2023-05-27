
from unittest import TestCase, main, mock
from unittest.mock import patch
from WardrobePlanner.functions.manage_wardrobe import add_item, delete_item


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



