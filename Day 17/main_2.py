class User:
    def __init__(self, id, name, lastname): #initialize attributes in a special method that Python understands to initialize the attributes
        print("New user being created ...")
        self.id = id
        self.name = name
        self.lastname = lastname
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


def create_username(user):
    user_name = user.name + user.lastname + user.id
    return user_name

def buy_followers(user, amount_new_followers):
    user.followers = amount_new_followers
    return user.followers

user_1 = User("001","John","Doe")
print(create_username(user_1))
print(buy_followers(user_1, 10))

user_2 = User("002","Jane","Eyre" )
print(create_username(user_2))
print("Before following user. 1 No. Followers : " , user_2.followers)
print("After following user 1: ")
user_2.follow(user_1)
print(f"Follows: {user_2.followers}")
print(f"Following: {user_2.following}")

print("U1 Before following user. 1 No. Followers : " , user_2.followers)
print("U1 After following user 1: ")
user_1.follow(user_2)
print(f"U1 Follows: {user_2.followers}")
print(f"U1 Following: {user_2.following}")