from functions import check_city, city_list_for_interface, cleaning_up_results, hometown_input_check

hometown = None

user_typed_hometown = input("If you want to use the weather tags in your wardrobe searches please provide your hometown.\n"
                    "  - type the the town name in your native tongue or in a Latin transcription\n"
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
    hometown = None

while True:
    hometown = input("\n_")
    if hometown.isdigit() and hometown in range(1, len(city_list)):
        break
    else:
        print("Please choose an option from the list")

if hometown == len(city_list):
    hometown = None



# raw_results = check_city("Warsaw")
# pprint(raw_results)
# pprint(cleaning_up_results(raw_results))
# raw_results = check_city("Tagong")
# pprint(raw_results)
# raw_results = check_city("塔公镇")
# pprint(raw_results)
# raw_results = check_city("Kolymbari")
# pprint(raw_results)
# raw_results = check_city("Κολυμβάρι")
# pprint(raw_results)
# raw_results = check_city("Mi'ilya")
# pprint(raw_results)
# raw_results = check_city("معليا")
# pprint(raw_results)
# raw_results = check_city("מִעִלְיָא")
# pprint(raw_results)
# pprint(cleaning_up_results(raw_results))
