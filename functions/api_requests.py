import requests
from WardrobePlanner.classes.db_utils import DBSearch
from WardrobePlanner.functions.date_and_geolocation import getting_future_date

def formatting_today_request_link(location):
    return "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=apparent_temperature_max&forecast_days=1&timezone=auto".format(location[0], location[1])


def formatting_future_request_link(location, date):
    return "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=apparent_temperature_max" \
           "&forecast_days=1&start_date={}&end_date={}&timezone=auto".format(location[0], location[1], date, date)


def getting_temperature_today():
    hometown = DBSearch.get_hometown()
    response = requests.get(formatting_today_request_link(hometown[1]))
    temp_raw_data = response.json()
    apparent_temp = temp_raw_data["daily"]['apparent_temperature_max'][0]
    return apparent_temp

def getting_temperature_future_date():
    hometown = DBSearch.get_hometown()
    future_date = getting_future_date()
    response = requests.get(formatting_future_request_link(hometown[1], future_date))
    temp_raw_data = response.json()
    apparent_temp = temp_raw_data["daily"]['apparent_temperature_max'][0]
    return apparent_temp

