from WardrobePlanner.functions.search.api_requests import getting_temperature_today
from WardrobePlanner.functions.search.pre_search_notifications import generate_no_hometown_notification


tags_dict = {"weather_tag": ["freezing", "cold", "mild", "warm", "hot"],
             "occasion_tag": ["cleaning", "sport", "home", "work", "party", "date"],
             "mood_tag": ["cheerful", "serious", "romantic", "sad", "neutral"],
             "item_type": ["bottom", "top", "outer wear", "full body"]
             }


def user_choices_input(tag_list_name, counter):
    while True:
        try:
            user_choice = int(input("\n_"))
            if int(user_choice) == counter:
                return ""
            elif 0 < int(user_choice) <= counter - 1:
                return tags_dict[tag_list_name][int(user_choice) - 1]
            else:
                print("Please choose an option from the list. Try again.")
        except ValueError:
            print("Sorry that's not a number from the requested range, try again!")


def users_choices(tag_list_name):
    counter = 1
    for option in tags_dict[tag_list_name]:
        print("{}. {}".format(counter, option))
        counter += 1
    print("{}. n/a".format(counter))
    return user_choices_input(tag_list_name, counter)


def whether_weather(user):
    if len(generate_no_hometown_notification(user)) > 0:
        print(generate_no_hometown_notification(user))
        return False
    while True:
        try:
            user_choice = input("Do you want to factor in the weather? (y/n)\n_")
            if user_choice.lower() == "y":
                return True
            elif user_choice.lower() == "n":
                return False
            else:
                raise ValueError("Please type y/n. Try again.")
        except ValueError:
            print("Please type y/n. Try again.")


def prompt_user(user):
    input_list = []
    print("What's the occasion?")
    occasion = users_choices("occasion_tag")
    input_list.append(occasion)
    print("What are you feeling like today?")
    mood = users_choices("mood_tag")
    input_list.append(mood)
    if whether_weather(user):
        temperature = getting_temperature_today(user)
        if temperature < 0:
            weather = tags_dict["weather_tag"][0]
        elif 0 <= temperature < 10:
            weather = tags_dict["weather_tag"][1]
        elif 10 <= temperature < 15:
            weather = tags_dict["weather_tag"][2]
        elif 15 <= temperature < 25:
            weather = tags_dict["weather_tag"][3]
        else:
            weather = tags_dict["weather_tag"][4]
        input_list.append(weather)
    else:
        input_list.append("")
    return input_list


def formatting_tags(tag_list):
    if tag_list[0] == "":
        occasion_tag = ""
    else:
        occasion_tag = " AND c.occasion_tag = '{}' ".format(tag_list[0])
    if tag_list[1] == "":
        mood_tag = ""
    else:
        mood_tag = " AND c.mood_tag = '{}' ".format(tag_list[1])
    if tag_list[2] == "":
        weather_tag = ""
    else:
        weather_tag = " AND c.weather_tag = '{}' ".format(tag_list[2])
    return occasion_tag + mood_tag + weather_tag

