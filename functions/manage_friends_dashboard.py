from WardrobePlanner.classes.dashboard_class import Dashboard
from WardrobePlanner.functions.friends import add_friend, delete_friend, show_friends_list


manageFriendsDashboard = Dashboard("in Manage Friends", ["Show Friends",
                                                         "Add Friends",
                                                         "Delete Friends",
                                                         "Back to main dashboard"])


def manage_friends_dashboard(user):
    # Managing friends
    options_count = manageFriendsDashboard.generate_menu()
    sub_dashboard_4_choice = manageFriendsDashboard.get_users_choice(options_count)

    if sub_dashboard_4_choice == 1:
        friend_list = show_friends_list(user.user_id)
        print(friend_list)
        return manage_friends_dashboard(user)
    # Show friends

    elif sub_dashboard_4_choice == 2:
        friend_added = add_friend(user.user_id)
        print(friend_added)
        return manage_friends_dashboard(user)
    # Add friends

    elif sub_dashboard_4_choice == 3:
        friend_deleted = delete_friend(user.user_id)
        print(friend_deleted)
        return manage_friends_dashboard(user)
    # Delete friends
    else:
        return

