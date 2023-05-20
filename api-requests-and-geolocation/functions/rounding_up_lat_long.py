def rounding_up_lat_long(coordinates):
    rounded_coordinates = []
    for coordinate_pair in coordinates:
        rounded_pair = (round(coordinate_pair[0], 2), round(coordinate_pair[1], 2))
        rounded_coordinates.append(rounded_pair)
    return rounded_coordinates

