from WardrobePlanner.classes.db_utils import DBSearch


def show_item_id(item_description):
    item_id = DBSearch.get_item_id(item_description)
    return item_id


def get_item_availability():
    item_description = input("What is the item you would like to borrow?")
    item_id = DBSearch.get_item_id(item_description)
    DBSearch.check_availability(item_id)


# print("These are all items that are matching your search criteria:")
#             for item in result:
#                 item_description = item[0]
#                 item_id = item[1]
#                 owner_id = item[2]
#                 output = "'{}' - item number {} belonging to user {}".format(item_description, item_id, owner_id)
#                 print(output)