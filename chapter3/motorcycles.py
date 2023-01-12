motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

print("--------------------------------------------")
#Appending - Adding to the current list
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

#Appending - Starting with BLANK list then adding each item individually
motorcycles = []
motorcycles.append('kawasaki')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')

print("--------------------------------------------")

#inserting - Effectively adds element into list @ x postition shifting things to the right.
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

print("--------------------------------------------")
#Removing(Deleting) - This will effectively remove element from list but is specifically based on index positioning.
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#Deletes index 1 or "honda" from list
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)


print("\t---------- Removal via pop() Method ---------")
#pop() Method - Effectively removing the last element from list BUT is still stored as a value to be used later.
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print("The last motorcycle I purchased was a " + popped_motorcycles.title() + ".")

print("--------------------------------------------")

#pop() Method: "Popping elements from any position in list."
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print(first_owned)
print('The first motercycle i owned was a ' + first_owned.title() + ".")


print("\t---------- Removal via Value ---------")
#Removing - effectively telling python to remove element where element is found.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print("--------------------------------------------")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#Using a removed value similar to popping the value.
too_expensive = "ducati"
motorcycles.remove('ducati')
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")