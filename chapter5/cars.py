print("--------- If Statements: Example 1 'Cars' ---------")

cars = ['audi', 'bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("--------- Conditional test: Equality ---------")

car = 'bmw'
print(car == 'bmw')
# returns True

print('------------------------------------')

car = 'audi'
print(car == 'bmw')
# returns False

print("--------- Conditional test: Equality ---------")
car = "Audi"
print(car.lower() == 'audi')
# returns True due to lower() function making a change

print('------------------------------------')
car = "Audi"
print(car.lower() == 'audi')
print(car)
# Note that using the lower() function does not make a permenant change to the variable.



