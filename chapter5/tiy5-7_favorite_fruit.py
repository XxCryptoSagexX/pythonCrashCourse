print("--------- Try It Yourself! ---------")
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list
    # • Make a list of your three favorite fruits and call it favorite_fruits
    # • Write five if statements Each should check whether a certain kind of fruit is in your list 
    # If the fruit is in your list, the if block should print a statement, such as You really like bananas!
    # BONUS: Append a fruit to the list to have an additional check

favorite_fruits = ['mango', 'papaya', 'guava']
if 'mango' in favorite_fruits:
    print("You really like mangos!")
if 'papaya' in favorite_fruits:
    print("You really like papayas!")
if 'guava' in favorite_fruits:
    print("You really like guavas!")
if 'apple' in favorite_fruits:
    print("You really like apples")
if 'banana' in favorite_fruits:
    print("You really like bananas!")


print('\n----- Bonus Test -----')
print("Current list of fruits: ")
print(favorite_fruits)

name = input('\nWhat is your name? ')
fruit = input(name.title() + ", input 'apple': ")
favorite_fruits.append(fruit)

print("\nCurrent list of fruits: ")
print(favorite_fruits)


if 'mango' in favorite_fruits:
    print("\nYou really like mangos!")
if 'papaya' in favorite_fruits:
    print("You really like papayas!")
if 'guava' in favorite_fruits:
    print("You really like guavas!")
if 'apple' in favorite_fruits:
    print("You really like apples")
if 'banana' in favorite_fruits:
    print("You really like bananas!")