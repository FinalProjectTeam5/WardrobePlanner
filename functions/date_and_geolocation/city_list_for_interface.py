def city_list_for_interface(clean_search_results):
    counter = 1
    potential_cities = []
    for city in clean_search_results:
        potential_cities.append("{}. {}".format(counter, city[0]))
        counter += 1
    potential_cities.append("{}. My hometown isn't on this list. I want to try again.".format(counter))
    potential_cities.append("{}. My hometown isn't on this list. I want to proceed without a hometown.".format(counter + 1))
    return potential_cities

