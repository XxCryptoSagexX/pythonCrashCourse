print("------ Original Toppings.py ------")
requested_toppings = ['anchovies', 'extra cheese']

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

print("\n------ Appended Toppings.py ------")
print("------ Testing Multiple Conditions ------")
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
#Adding ELIF Blocks here would not work due to it passing once and would end the program. 
#Here we are checking each IF Block which would be needed to complete the pizza
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished maing your pizza")


print("\n------ Appendedv2 Toppings.py ------")
print("------ Checking for Special Items ------")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Aadding " + requested_topping + ".")

print("\nFinished making your pizza!")

print('------------------------------------')

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

print("\n------ Checking That a List Is Not Empty ------")
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Aadding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("\n------ Using Multiple Lists ------")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print ("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

