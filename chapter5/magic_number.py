print("--------- Numerical Comparisons ---------")
age = 18
print(age == 18) 

print('------------------------------------')
answer = 17
print("Did you get 42?")
if answer != 42:
    print("\tThat is not the correct answer. Please try again!")
print('------------------------------------')
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
print("--------- Numerical Comparisons: Multiple Conditions AND ---------")
age_0 = 22
age_1 = 18
print("Both 21 and over?")
print(age_0 >= 21 and age_1>= 21)

age_1 = 22
print("Redux: Both 21 and over?")
print(age_0 >= 21 and age_1>= 21)
print('------------------------------------')
print('Parenthesis print version attemtpt')
print((age_0 >= 21) and (age_1>= 21))

print("--------- Numerical Comparisons: Multiple Conditions OR ---------")
age_0 = 22
age_1 = 18
print("ANY 21 and over?")
print(age_0 >= 21 or age_1>= 21)

age_0 = 18
print("Redux: ANY 21 and over?")
print(age_0 >= 21 or age_1>= 21)
