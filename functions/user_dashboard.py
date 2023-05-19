def user_dashboard_choice():
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
            print("Please, enter a number between 1 and 5. Try again.")
            return user_dashboard_choice()
    except ValueError:
        print("Sorry that's not a number, try again!")
        return user_dashboard_choice()


# sub_dashboards?

def sub_dashboard_option_3():
    print("1. Add Items To Your Wardrobe \n"
          "2. Delete Items From Your Wardrobe \n"
          "3. Do Laundry")
    try:
        user_choice = int(input("What would you like to do? "))
        if user_choice in [1, 2, 3]:
            return user_choice
        else:
            print("Please, enter a number between 1 and 3. Try again.")
            return user_dashboard_choice()
    except ValueError:
        print("Sorry that's not a number, try again!")
        return user_dashboard_choice()


def sub_dashboard_option_4():
    print("1. Add Friends \n"
          "2. Delete Friends \n"
          "3. Show Friends")
    try:
        user_choice = int(input("What would you like to do? "))
        if user_choice in [1, 2, 3]:
            return user_choice
        else:
            print("Please, enter a number between 1 and 3. Try again.")
            return user_dashboard_choice()
    except ValueError:
        print("Sorry that's not a number, try again!")
        return user_dashboard_choice()
