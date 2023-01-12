print("--------- Try It Yourself! ---------")
# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after they log in to a website Loop through the list, and print a greeting to each user:
    # • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
    # • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
# BONUS: Append input for your name and your own special message.

usernames = ['heavenly','amber','warshawski','favi','admin']

for username in usernames:
    if username == 'admin':
        print("Hello " + username.title() + ", would you like to see a status report?")
    else:
        print("Hello " + username.title() + ", thank you for logging in again!")


print('\n----- Bonus Test -----')
your_name = input("What is your name? ")
your_name = your_name.lower()
usernames.append(your_name)

for username in usernames:
    if username == 'admin':
        print("Hello " + username.title() + ", would you like to see a status report?")
    elif username == 'tre':
        print("Greetings " + username.title() + ",you currently have no dev tasks in queue!")
    else:
        print("Hello " + username.title() + ", thank you for logging in again!")