from WardrobePlanner.classes.db_utils import DBSearch


def does_user_have_clothes(user):
    clothes = DBSearch.show_all_user_clothes(user.user_id)
    if len(clothes) > 0:
        return True
    else:
        return False


def does_user_have_friends(user):
    friends = DBSearch.get_friends_list(user.user_id)
    if len(friends) > 0:
        return True
    else:
        return False


def is_hometown_set(user):
    if user.home_town is None:
        return False
    else:
        return True


def generate_no_search_possible_notification(user):
    if does_user_have_clothes(user) or does_user_have_friends(user):
        return ""
    else:
        return "You don't have any clothes in your wardrobe and your friends list is empty.\n" \
               "No search can be performed.\n" \
               "Add clothes and/or friends to use the search function."


def generate_no_hometown_notification(user):
    if is_hometown_set(user):
        return ""
    else:
        return "You don't have a hometown set so weather conditions won't be included in your search."

