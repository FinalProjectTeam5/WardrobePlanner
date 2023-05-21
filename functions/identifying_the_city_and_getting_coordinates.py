from WardrobePlanner.functions.date_and_geolocation import check_city
from WardrobePlanner.functions.date_and_geolocation import city_list_for_interface
from WardrobePlanner.functions.date_and_geolocation import cleaning_up_results
from WardrobePlanner.functions.date_and_geolocation import hometown_input_check


def getting_hometown():
    while True:
        user_typed_hometown = input("If you want to use the weather tags in your wardrobe searches please provide your hometown.\n"
                            "  - type the town name in your native tongue or in a Latin transcription\n"
                            "  - if the api didn't find your hometown on first attempt, try the name of the nearest bigger town instead\n"
                            "\n"
                            "Your hometown: ")
        user_hometown_choice = hometown_input_check(user_typed_hometown)
        if user_hometown_choice:
            possible_cities = check_city(user_typed_hometown)
            list_prep = cleaning_up_results(possible_cities)
            city_list = city_list_for_interface(list_prep)
            print("Choose your hometown from the list:")
            for city in city_list:
                print(city)
        else:
            return
        while True:
            hometown = input("\n_")
            if hometown.isdigit() and int(hometown) <= len(city_list):
                break
            else:
                print("Please choose an option from the list. Try again.")
        if int(hometown) == len(city_list):
            return
        elif int(hometown) == len(city_list) - 1:
            pass
        else:
            hometown = list_prep[int(hometown) - 1]
            return hometown




