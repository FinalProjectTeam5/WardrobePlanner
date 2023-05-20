import itertools


def rounding_up_lat_long(coordinates):
    rounded_coordinates = []
    for coordinate_pair in coordinates:
        rounded_pair = (round(coordinate_pair[0], 2), round(coordinate_pair[1], 2))
        rounded_coordinates.append(rounded_pair)
    return rounded_coordinates


def eliminating_duplicates(array):
    duplicate_finder = []
    for item in array:
        item = item.split(", ")
        if len(item) > 1:
            duplicate_finder.append(item[1])
    return duplicate_finder


def creating_true_false_list(array2):
    true_false_list = [False for item in range(len(array2))]
    non_unique_list = eliminating_duplicates(array2)
    for item in non_unique_list:
        index = non_unique_list.index(item)
        true_false_list[index] = True
    return true_false_list


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

