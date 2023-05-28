from geopy.geocoders import Nominatim
from WardrobePlanner.classes.dashboard_class import Menu

no_results_menu = Menu("No results were found for the city you provided.\n"
                       "WARNING - in the current version of the app this is the only moment when you can set the hometowm.\n"
                       "Without the hometown set your searches automatically won't include weather tags.\n",
                       ["Search again.", "Proceed without a hometown."])


def check_city(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city, exactly_one=False)
    return location


def no_results_found():
    options_count = no_results_menu.generate_menu()
    what_next = no_results_menu.get_users_choice(options_count)
    if what_next == 1:
        return "again"
    else:
        return "no_hometown"


def hometown_input_check(user_input):
    raw_results = check_city(user_input)
    if raw_results is None:
        no_results_what_to_do = no_results_found()
        return no_results_what_to_do
    else:
        return "generate_list"

