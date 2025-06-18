# class User:
#     pass


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Jane"
#
# print(user_1.username)
#
# user_2 = User()
# user_1.id = "002"
# user_1.username = "Joh

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Jane")
user_2 = User("002", "John")

user_1.follow(user_2)
print(f"User 1 followers {user_1.followers}")
print(f"User 1 followings {user_1.following}")
print(f"User 2 followers {user_2.followers}")
print(f"User 2 followings {user_2.following}")


