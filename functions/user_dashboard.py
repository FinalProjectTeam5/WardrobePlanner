def user_dashboard_choice():
    print("Welcome!")
    print("1. Show User Info \n"
          "2. Search Wardrobe \n"
          "3. Manage Wardrobe \n"
          "4. Manage Friends \n"
          "5. Log Out / Exit")
    try:
        user_choice = int(input("What would you like to do? "))
        if user_choice in [1, 2, 3, 4, 5]:
            return user_choice
        else:
            print("Please choose an option from the list. Try again.")
            return user_dashboard_choice()
    except ValueError:
        print("Sorry that's not a number, try again!")
        return user_dashboard_choice()


def sub_dashboard_user_info():
    pass

def sub_dashboard_search():
    print("You're in Search")
    print("1. Search all available \n"
          "2. Search through tags \n"
          "3. Back to main dashboard")
    while True:
        try:
            user_choice = int(input("What would you like to do? "))
            if user_choice in [1, 2]:
                return user_choice
            elif user_choice == 3:
                return user_dashboard_choice()
            else:
                print("Please choose an option from the list. Try again.")
        except ValueError:
            print("Sorry that's not a number, try again!")




def sub_dashboard_manage_wardrobe():
    print("You're in Wardrobe Management")
    print("1. Add Items To Your Wardrobe \n"
          "2. Delete Items From Your Wardrobe \n"
          "3. Do Laundry\n"
          "4. Back to main dashboard")
    try:
        user_choice = int(input("What would you like to do? "))
        if user_choice in [1, 2, 3]:
            return user_choice
        else:
            print("Please choose an option from the list. Try again.")
            return user_dashboard_choice()
    except ValueError:
        print("Sorry that's not a number, try again!")
        return user_dashboard_choice()


def sub_dashboard_manage_friends():
    print("You're in Friends Management")
    print("1. Add Friends \n"
          "2. Delete Friends \n"
          "3. Show Friends\n"
          "4. Back to main dashboard")
    try:
        user_choice = int(input("What would you like to do? "))
        if user_choice in [1, 2, 3]:
            return user_choice
        else:
            print("Please choose an option from the list. Try again.")
            return user_dashboard_choice()
    except ValueError:
        print("Sorry that's not a number, try again!")
        return user_dashboard_choice()
