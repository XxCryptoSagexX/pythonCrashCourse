print("--------- Try It Yourself! ---------")
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60)
# Make a copy of the list of pizzas, and call it friend_pizzas
favorite_pizzas = ["meat lover's pizza", 'sausage pizza', 'buffalo pizza']
friend_pizzas = favorite_pizzas[:]

# Add a new pizza to the original list
favorite_pizzas.append('pepperoni pizza')

# Add a different pizza to the list friend_pizzas
friend_pizzas.append('pineapple & ham pizza')


# Prove that you have two separate lists
# Print the message, My favorite pizzas are:, and then use a for loop to print the first list.
# Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list
print('My favorite pizzas are:')
for pizza in favorite_pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
