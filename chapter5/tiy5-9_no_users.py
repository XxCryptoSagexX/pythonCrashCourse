print("--------- Try It Yourself! ---------")
# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty
    # • If the list is empty, print the message We need to find some users!
    # • Remove all of the usernames from your list, and make sure the correct message is printed

print("\n--------- Filled  List Variant---------")
usernames = ['heavenly','amber','warshawski','favi','admin']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello " + username.title() + ", would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in again!")
else:
    print("We need to find some users!")

print("\n--------- Empty List Variant---------")
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello " + username.title() + ", would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in again!")
else:
    print("We need to find some users!")


