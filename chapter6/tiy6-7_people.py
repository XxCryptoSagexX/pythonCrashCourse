print("--------- Try It Yourself! ---------")
# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102) Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people Loop through your list of people As you loop through the list, print everything you know about each person
# BONUS APPEND: Create a total of 4 dictionaries

person_0 = {
    'first_name': 'amber',
    'last_name': 'williams',
    'age': 26,
    'city': 'west monroe'
    }
person_1 = {
    'first_name': 'heavenly',
    'last_name': 'williams',
    'age': 7,
    'city': 'west monroe'
    }

person_2 = {
    'first_name': 'faviana',
    'last_name': 'torres',
    'age': 22,
    'city': 'west monroe'
    }

person_3 = {
    'first_name': 'warshawski',
    'last_name': 'caston',
    'age': 24,
    'city': 'swartz'
    } 

people = [person_0,person_1,person_2,person_3]

for person in people:
    print(person)