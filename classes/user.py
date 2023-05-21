class User:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.password = None
        self.home_town = None
        self.status = False

    def login(self, user_id, username, password, home_town):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.home_town = home_town
        self.status = True

    def logout(self):
        self.user_id = None
        self.username = None
        self.password = None
        self.home_town = None
        self.status = False

