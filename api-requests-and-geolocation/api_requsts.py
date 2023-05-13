import requests
from geopy.geocoders import Nominatim


def city_to_long_lat(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city)
    lat = round(location.latitude, 2)
    long = round(location.longitude, 2)
    return [lat, long]


def formatting_today_request_link(location):
    return "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=apparent_temperature_max&forecast_days=1&timezone=auto".format(location[0], location[1])


def formatting_future_request_link(location, date):
    return "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=apparent_temperature_max" \
           "&forecast_days=1&start_date={}&end_date={}&timezone=auto".format(location[0], location[1], date, date)


#variables to be replaced with user's choices
hometown = "Zurich"
future_date = "2023-05-20"

#today
response = requests.get(formatting_today_request_link(city_to_long_lat(hometown)))
temp_raw_data = response.json()
apparent_temp = temp_raw_data["daily"]['apparent_temperature_max'][0]
#print(apparent_temp)

#future
response = requests.get(formatting_future_request_link(city_to_long_lat(hometown), future_date))
temp_raw_data = response.json()
apparent_temp = temp_raw_data["daily"]['apparent_temperature_max'][0]
#print(apparent_temp)