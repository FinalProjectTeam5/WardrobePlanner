from db_utils import DBSearch


def show_item_id(item_description):
    item_id = DBSearch.get_item_id(item_description)
    return item_id
