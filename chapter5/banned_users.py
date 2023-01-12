print("---------Checking if value IS in a LIST ---------")
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

print("---------Checking if value ISNOT in a LIST ---------")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")