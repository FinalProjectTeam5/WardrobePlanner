import requests
from WardrobePlanner.functions.date_and_geolocation import getting_future_date

def formatting_today_request_link(lat, long):
    return "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=apparent_temperature_max&forecast_days=1&timezone=auto".format(lat, long)


def formatting_future_request_link(lat, long, date):
    return "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=apparent_temperature_max" \
           "&forecast_days=1&start_date={}&end_date={}&timezone=auto".format(lat, long, date, date)


def getting_temperature_today(user):
    latitude = user.latitude
    longitude = user.longitude
    response = requests.get(formatting_today_request_link(latitude, longitude))
    temp_raw_data = response.json()
    apparent_temp = temp_raw_data["daily"]['apparent_temperature_max'][0]
    return apparent_temp


def getting_temperature_future_date(user):
    future_date = getting_future_date()
    latitude = user.latitude
    longitude = user.longitude
    response = requests.get(formatting_future_request_link(latitude, longitude, future_date))
    temp_raw_data = response.json()
    apparent_temp = temp_raw_data["daily"]['apparent_temperature_max'][0]
    return apparent_temp

