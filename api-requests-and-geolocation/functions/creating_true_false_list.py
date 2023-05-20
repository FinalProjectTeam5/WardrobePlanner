import eliminating_duplicates

def creating_true_false_list(array2):
    true_false_list = [False for item in range(len(array2))]
    non_unique_list = eliminating_duplicates(array2)
    for item in non_unique_list:
        index = non_unique_list.index(item)
        true_false_list[index] = True
    return true_false_list

