from db_utils import DBSearch


def show_item_id(item_description):
    item_id = DBSearch.get_item_id(item_description)
    return item_id


def get_item_availability():
    item_description = input("What is the item you would like to borrow?")
    item_id = DBSearch.get_item_id(item_description)
    DBSearch.check_availability(item_id)
