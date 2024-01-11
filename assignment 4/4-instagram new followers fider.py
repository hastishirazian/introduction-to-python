import instaloader
import getpass

old_followers = []
new_followers = []
follow = []

f = open("old_followers.txt" , "r")
for line in f:
    old_followers.append(line)
f.close()

username = input("Username:")
password = getpass.getpass("Password:")

account = instaloader.Instaloader() #Log in instagram
account.login(username,password)

profile = instaloader.profile.from_usernme(L.cotext , "hastishiraziann") #connecting to profie

for follower in profile.get_followers():
    new_followers.append(follower)

for follower in new_followers:
    if follower not in old_followers:
            follow.append(follower)

f = open("new_followers.txt" , "w")
for follower in new_followers:
    f.write(follower + "\n")
f.close()

print("Your new followers are:")
print(follow)