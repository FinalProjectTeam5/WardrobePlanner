import itertools
import creating_true_false_list
import rounding_up_lat_long


def cleaning_up_results(raw_list):
    if len(raw_list) == 1:
        unique_cities_with_coordinates = [raw_list[0], (round(raw_list[1][0], 2), round(raw_list[1][1], 2))]
    else:
        new_list = [list(item) for item in raw_list]
        lat_long_list = [item[1] for item in new_list]
        lat_long_list = rounding_up_lat_long(lat_long_list)
        new_list = [item[0] for item in new_list]
        compressor = creating_true_false_list(new_list)
        city_list = list(itertools.compress(new_list, compressor))
        lat_long_list = list(itertools.compress(lat_long_list, compressor))
        unique_cities_with_coordinates = list(zip(city_list, lat_long_list))
    return unique_cities_with_coordinates

