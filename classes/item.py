from WardrobePlanner.functions import search_clothes as search


class Item:
    def __init__(self, user_id):
        self.owner_id = user_id
        self.item_id = None
        self.item_type = None
        self.item_description = None
        self.weather_tag = None
        self.occasion_tag = None
        self.mood_tag = None

    def manage_item(self, item_type, item_description, weather_tag, occasion_tag, mood_tag):
        self.item_id = search.show_item_id(item_description)
        self.item_type = item_type
        self.item_description = item_description
        self.weather_tag = weather_tag
        self.occasion_tag = occasion_tag
        self.mood_tag = mood_tag

    def delete_item(self):
        self.owner_id = None
        self.item_id = None
        self.item_type = None
        self.item_description = None
        self.weather_tag = None
        self.occasion_tag = None
        self.mood_tag = None
