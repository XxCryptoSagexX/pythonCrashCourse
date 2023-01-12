print("--------- Try It Yourself! ---------")
# 5-2. More Conditional Tests: You don’t have to limit the number of tests youcreate to 10
# If you want to try more comparisons, write more tests and add them to conditional_tests.py 

# Tests for equality and inequality with strings
car = 'cadilac'
print("Is car == 'cadilac'? I predict True")
print(car == 'cadilac')

print("\nIs car == 'cadilac'? I predict False")
print(car == 'ford') 

print("\nIs car != 'cadilac'? I predict False")
print(car != 'cadilac')

car = 'ford'
print("\nIs car != 'cadilac'? I predict True")
print(car != 'cadilac')

print('\n----- Test 2 -----')
# Tests using the lower() function
favorite_food = 'BUFFALO WINGS'
print("\nIs favoite_food == 'buffalo wings'? I predict False")
print(favorite_food == 'buffalo wings')

print("\nIs favoite_food == 'buffalo wings'? I predict True")
print(favorite_food.lower() == 'buffalo wings')

print('\n----- Test 3 -----')
#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
age = 29
print("\nIs age == 29? I predict True")
print(age == 29)

print("\nIs age != 29? I predict False")
print(age != 29)

print("\nIs age > 20? I predict True")
print(age > 20)

print("\nIs age > 50? I predict False")
print(age > 50)

print("\nIs age < 50? I predict True")
print(age < 50)

print("\nIs age < 20? I predict False")
print(age < 20)

print("\nIs age >= 20? I predict True")
print(age >= 20)

print("\nIs age >= 50? I predict False")
print(age >= 50)

print("\nIs age <= 50? I predict True")
print(age <= 50)

print("\nIs age <= 20? I predict False")
print(age <= 20)

print('\n----- Test 4 -----')
#Tests using the and keyword and the or keyword
print("\nIs age > 18 AND  age < 50 ? I predict True")
print( (age > 18) and (age < 50) )

print("\nIs age > 18 AND  age > 50 ? I predict False")
print( (age > 18) and (age > 50) )

print("\nIs age > 18 OR age > 21? I predict True")
print( (age > 18) or (age > 21) )

print("\nIs age > 50 or age > 65 ? I predict False")
print( (age > 50) or (age > 65) )

print('\n----- Test 5 -----')
#Test whether an item is in a list
favorite_beverages = ['sweet tea', 'coffee', 'sprite zero', 'coke zero', 'baja blast zero']
print("\nIs 'baja blast zero' in favorite_beverages? I predict True")
print('baja blast zero' in favorite_beverages)

print("\nIs 'pepsi zero' in favorite_beverages? I predict False")
print('pepsi zero' in favorite_beverages)


print('\n----- Test 5 -----')
#Test whether an item is not in a list
favorite_beverages = ['sweet tea', 'coffee', 'sprite zero', 'coke zero', 'baja blast zero']
print("\nIs 'pepsi zero' not in favorite_beverages? I predict True")
print('pepsi zero' not in favorite_beverages)

print("\nIs 'sweet tea' not in favorite_beverages? I predict False")
print('sweet tea' not in favorite_beverages)
