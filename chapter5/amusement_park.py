print("------ If-Elif-Else Chain ------")
# Admission for anyone under age 4 is free
# Admission for anyone between the ages of 4 and 18 is $5
# Admission for anyone age 18 or older is $10

age = 12
print('Current Age: ' + str(age))
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5")
else:
    print('Your admission cost is $10')

print("\n------ If-Elif-Else Chain: Realistic View ------")
# Shows a more practical method of how this would work
age = 12
print('Current Age: ' + str(age))
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + '.')


print("\n------ Using Multiple Elif Blocks ------")
age = 12
print('Current Age: ' + str(age))
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + '.')


print("\n------ Omitting the ELSE Block ------")
# ELSE block is not required at the end of the if-elif chain. You can use some form of 'catch all' in your conditions

age = 65
print('Current Age: ' + str(age))
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + '.')