from WardrobePlanner.classes.dashboard_class import Dashboard
from WardrobePlanner.functions.manage_wardrobe import add_item, delete_item, laundry, add_item_id, notification_laundry


manageWardrobeDashboard = Dashboard("in Manage Wardrobe", ["Add Items To Your Wardrobe",
                                                           "Delete Items From Your Wardrobe",
                                                           "Do Laundry",
                                                           "Back to main dashboard"])


def manage_wardrobe_dashboard(user):
    options_count = manageWardrobeDashboard.generate_menu()
    sub_dashboard_3_choice = manageWardrobeDashboard.get_users_choice(options_count)
    if sub_dashboard_3_choice == 1:
        item_id = add_item_id(user.user_id)[0][0]
        item_added = add_item(item_id)
        print(item_added)
        return manage_wardrobe_dashboard(user)
    # Add items to wardrobe

    elif sub_dashboard_3_choice == 2:
        item_deleted = delete_item()
        print(item_deleted)
        return manage_wardrobe_dashboard(user)
    # Delete items

    elif sub_dashboard_3_choice == 3:
        print(notification_laundry(user.user_id))
        if notification_laundry(user.user_id) == "You have no dirty clothes":
            return manage_wardrobe_dashboard(user)
        else:
            laundry_decision = laundry(user.user_id)
            print(laundry_decision)
            return manage_wardrobe_dashboard(user)
    # Do laundry
    else:
        return

