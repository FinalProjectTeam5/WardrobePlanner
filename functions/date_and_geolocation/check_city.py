from geopy.geocoders import Nominatim


def check_city(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city, exactly_one=False)
    return location


def hometown_input_check(user_input):
    raw_results = check_city(user_input)
    if raw_results is None:
        print("1. No results were found for the city you provided. Let me try again.")
        print("2. No results were found for the city you provided. Let me proceed without a hometown.")
        while True:
            user_choice = input("_")
            if user_choice == "1":
                return True
            elif user_choice == "2":
                return False
            else:
                print("Try again.")
    else:
        return True

