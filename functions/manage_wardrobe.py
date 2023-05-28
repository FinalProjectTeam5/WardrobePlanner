from WardrobePlanner.classes.db_utils import DBSearch
from WardrobePlanner.functions.search.tag_prompts import users_choices


def add_item_id(user_id):
    return DBSearch.add_item_ID(user_id)


def add_item(item_id):
    print("What type of item are you adding?")
    item_type = users_choices("item_type")
    item_description = input("How would you succinctly describe it? \n")
    print("When would you wear this item?")
    print("Weather options:")
    weather_tag = users_choices("weather_tag")
    print("Occasion options:")
    occasion_tag = users_choices("occasion_tag")
    print("Mood options:")
    mood_tag = users_choices("mood_tag")
    DBSearch.add_item_to_wardrobe(item_id, item_type, item_description, weather_tag, occasion_tag, mood_tag)
    return "{} has been added to your wardrobe".format(item_description)


def delete_item():
    item_to_delete = input("Please enter the description of an item you'd like to remove: ")
    item_to_delete_id = DBSearch.get_item_id(item_to_delete)[0][0]
    DBSearch.delete_item_from_wardrobe(item_to_delete_id)
    return "{} has been deleted from your wardrobe".format(item_to_delete)


def laundry(user_id):
    wanna_do_laundry = input("Do you want to clean all your clothes? y/n \n")
    if wanna_do_laundry == "y":
        DBSearch.do_laundry(user_id)
        return "All of your clothes are clean now!"
    else:
        return "Ok, maybe later."


def notification_laundry(user_id):
    notif = "You have {} available clothes, and {} dirty clothes. "\
        .format(DBSearch.show_count_of_clothes_available(user_id)[0][0],
                DBSearch.show_count_of_clothes_dirty(user_id)[0][0])
    if DBSearch.show_count_of_clothes_dirty(user_id)[0][0] == 0:
        notif = "You have no dirty clothes"
    return notif
