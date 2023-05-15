class User():
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id

    def get_user_details(self):
        return self.username, self.user_id


user1 = User(username="Test", user_id=5)


