print("--------- Try It Yourself! ---------")
# 6-1. Person: Use a dictionary to store information about a person you know Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city Print each piece of information stored in your dictionary
# BONUS APPEND: Create a second Dictionary.  

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

print('------------------------------------')

print(person_0)
print(person_1)

print('------------------------------------')

print("Person 1:")
print("\tFirst Name: " + person_0['first_name'].title())
print("\tLast Name: " + person_0['last_name'].title())
print("\tAge: " + str(person_0['age']))
print("\tCity: " + person_0['city'].title() + '\n')


print("Person 2:")
print("\tFirst Name: " + person_1['first_name'].title())
print("\tLast Name: " + person_1['last_name'].title())
print("\tAge: " + str(person_1['age']))
print("\tCity: " + person_1['city'].title())
