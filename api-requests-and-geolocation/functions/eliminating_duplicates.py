def eliminating_duplicates(array):
    duplicate_finder = []
    #print(array)
    for item in array:
        item = item.split(", ")  # turns the location information into a list
        if len(item) > 1:
            duplicate_finder.append(item[1])
    return duplicate_finder

