class Dashboard:

    def __init__(self, location, options):
        self.location = location
        self.options = options

    def generate_menu(self):
        print("You are {}".format(self.location))
        counter = 0
        for option in self.options:
            counter += 1
            print("{}. {}".format(counter, option))
        return counter

    def get_users_choice(self, options_count):
        while True:
            try:
                user_choice = int(input("What would you like to do? "))
                if user_choice <= options_count:
                    return user_choice
                else:
                    print("Please choose an option from the list. Try again.")
            except ValueError:
                print("Sorry that's not a number, try again!")






