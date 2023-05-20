from geopy.geocoders import Nominatim


def check_city(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city, exactly_one=False)
    return location

