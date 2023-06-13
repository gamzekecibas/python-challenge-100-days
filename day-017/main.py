## Day 17 - Intermediate | Benefits of OOP
## 13.06.2023

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  ## default value
        self.following = 0
        print("new user being created...")

    def follow(self, user):
        user.followers += 1
        self.following += 1

##  pass   ## decoration


user_1 = User("001", "angela")
#user_1.id = "001"
#user_1.username = 'angela'

print(user_1.username)

user_2 = User('002', 'jack')
#user_2.id = '002'
#user_2.name = 'jack'   ## it is open such errors! So, initialize object in class!!
print(user_2.followers)

print('When follow method is added: ')
user_1.follow(user_2)       ## user_1 follows user_2 now!
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
