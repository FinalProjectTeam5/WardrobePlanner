from WardrobePlanner.classes.db_utils import DBSearch

def add_item():
    item_type = input("What is the type of clothing? Bottom, top, full body, outerwear ")
    item_description = input("What is the description of the item?")
    weather_tag = input("What weather would you normally where this item? Freezing, cold, mild, warm, hot")
    occasion_tag = input("When would you usually wear this item? Cleaning, sport, home, work, party, date")
    mood_tag = input("In what mood would you wear this item? Cheerful, serious, romantic, sad, neutral")
    DBSearch.add_item_to_wardrobe(item_type, item_description, weather_tag, occasion_tag, mood_tag)
    return "{} has been added to your wardrobe".format(item_description)


def delete_item():
    item_to_delete = input("")
    DBSearch.delete_item_from_wardrobe(item_to_delete)
    return "{} has been deleted from your wardrobe".format(item_to_delete)