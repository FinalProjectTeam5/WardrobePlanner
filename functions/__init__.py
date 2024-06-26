from WardrobePlanner.functions.search.api_requests import getting_temperature_today, getting_temperature_future_date
from .dashboard_function import dashboard
from .friends import add_friend, delete_friend, show_friends_list
from WardrobePlanner.functions.date_and_geolocation.identifying_the_city_and_getting_coordinates import getting_hometown
from .login import sign_up, login, get_new_password, get_new_username, show_user_id
from .manage_wardrobe import add_item, delete_item, laundry, add_item_id
from .manage_wardrobe_dashboard import manage_wardrobe_dashboard
from .manage_friends_dashboard import manage_friends_dashboard
