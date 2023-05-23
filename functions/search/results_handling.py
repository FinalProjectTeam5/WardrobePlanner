from WardrobePlanner.classes.dashboard_class import Dashboard
from WardrobePlanner.classes.db_utils import DBSearch

results_handling = Dashboard("What do you want to do with these results?", ["Choose an item",
                                                  "Search again"])

def display_results(results, user):
    users_with_id = DBSearch.get_all_users_and_ids()
    counter = 0
    # print(results)
    options = []
    whose = ""
    for result in results:
        if user.user_id == result[2]:
            whose = "me"
        else:
            for person in users_with_id:
                if person[0] == result[2]:
                    whose = person[1]
                    break
        counter += 1
        options.append(counter)
        print("{}. {}, item belongs to {}".format(counter, result[0], whose))
    return options


def what_user_wants_to_do_with_the_results(results, counter, user):
    options_count = results_handling.generate_menu()
    what_next = results_handling.get_users_choice(options_count)
    if what_next == 1:
        while True:
            choose_item = input("Type the number of the item you want to wear: ")
            if choose_item.isdigit() and 0 < int(choose_item) <= len(counter):
                chosen_item_index = counter.index(int(choose_item))
                print(chosen_item_index)
                chosen_item = results[chosen_item_index]
                return chosen_item
            else:
                print("You didn't choose a number from the list. Try again!")
    else:
        return