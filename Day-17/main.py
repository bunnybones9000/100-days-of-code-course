class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user1 = User("001", "angela")
user2 = User("002", "daniel")

user1.follow(user2)

