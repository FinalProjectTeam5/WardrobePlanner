from WardrobePlanner.classes.dashboard_class import Dashboard
from WardrobePlanner.classes.db_utils import DBSearch
from WardrobePlanner.functions.search.results_handling import display_results, what_user_wants_to_do_with_the_results
from WardrobePlanner.functions.search.tag_prompts import prompt_user, formatting_tags
from WardrobePlanner.functions.search.pre_search_notifications import generate_no_search_possible_notification

searchDashboard = Dashboard("in Search", ["Search all available",
                                          "Search through tags",
                                          "Back to main dashboard"])


def do_search(user, tags):
    search_results = DBSearch.search_clothes(tags, user.user_id)
    if len(search_results) == 0:
        print("No clothes match your search criteria. Try a different search.")
        return
    number_of_results = display_results(search_results, user)
    decision = what_user_wants_to_do_with_the_results(search_results, number_of_results, user)  # none or chosen item
    # print(decision)
    if decision is None:
        return
    else:
        print("You've selected item '{}' that belongs to {}".format(decision[0][0], decision[1]))
        DBSearch.change_to_dirty(decision[0][1])
        return


def search_dashboard(user):
    if len(generate_no_search_possible_notification(user)) > 0:
        print(generate_no_search_possible_notification(user))
        return
    options_count = searchDashboard.generate_menu()
    user_choice = searchDashboard.get_users_choice(options_count)
    if user_choice == 1:
        tags = ""
        do_search(user, tags)
        return search_dashboard(user)
    elif user_choice == 2:
        user_tags = prompt_user(user)
        tags = formatting_tags(user_tags)
        do_search(user, tags)
        return search_dashboard(user)
    else:
        return

