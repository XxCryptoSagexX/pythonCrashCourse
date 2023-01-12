print("--------------------------------------------")
#Sorting - using the sort() method permanentely changed the order (alphabetical order)
cars = ['bmw', 'audi','toyota','subaru']
cars.sort()
print(cars)
print("--------------------------------------------")
#Sorting - using the sort() method permanentely changed the order (reverse alphabetical order)
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
print("--------------------------------------------")
print("--------------------------------------------")
#Temp Sorting - using the sorted() Method to show sorted but not permanently sorting
cars = ['bmw', 'audi','toyota','subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
print("--------------------------------------------")
print("--------------------------------------------")
print("--------------------------------------------")
#Reverse Sorting - reversing the order of the list chronologically (this is input not alphabetically )
cars = ['bmw', 'audi','toyota','subaru']
cars.reverse()
print(cars)
print("--------------------------------------------")
#List Length - Using the len() function
cars = ['bmw', 'audi','toyota','subaru']
cars_len = len(cars)
print("Amount of cars available: " + str(cars_len))
