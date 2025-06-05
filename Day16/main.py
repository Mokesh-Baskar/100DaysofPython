class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username= username
        self.followers  = 0
    def updatefollowerscount(self,count):
        self.followers += count    

user_1 = User("001","mokesh")


print(user_1.id)
print(user_1.username)


count =int(input("Please enter the follower count to be updated : "))


user_1.updatefollowerscount(count)


print(user_1.followers)
