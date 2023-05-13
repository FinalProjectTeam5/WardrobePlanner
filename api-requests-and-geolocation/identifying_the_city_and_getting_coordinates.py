import itertools
from pprint import pprint
from geopy.geocoders import Nominatim


#looks up the provided city, returns a geopy location object of matches or a None object
def check_city(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city, exactly_one=False)
    return location


def cleaning_up_results(raw_list):
    new_list = [list(item) for item in raw_list]  # converts the geopy object into a list
    lat_long_list = [item[1] for item in new_list]  # creates a list of latitude, longitude tuples
    new_list = [item[0] for item in new_list]  # removes the latitude, longitude tuples from the previous list
    duplicate_finder = []
    compressor = [False for item in range(len(new_list))]  # creates a starter second list for the compress method
    # turns the location information into a list
    for item in new_list:
        item = item.split(", ")
        if len(item) > 1:
            duplicate_finder.append(item[1])
    # prepares the proper 2nd list for the compress method
    for item in duplicate_finder:
        index = duplicate_finder.index(item)
        compressor[index] = True
    city_list = list(itertools.compress(new_list, compressor))
    print(city_list)
    lat_long_list = list(itertools.compress(lat_long_list, compressor))
    # combines back the city name and the coordinates but only for unique cities
    unique_cities_with_coordinates = list(zip(city_list, lat_long_list))
    return unique_cities_with_coordinates


def city_list_for_interface():
    pass


# hometown = input("What is your home town, or the closest town to where you live? ")
# print(type(check_city(hometown)))
# print(check_city(hometown))


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