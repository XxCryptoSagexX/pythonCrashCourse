print("--------- Tuples: Standard Printing ---------") 
# Think of it as the "list" that is permanent and cannot be changed/altered.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print('------------------------------------')
# trying to change dimensions but failes here
# dimensions[0] = 250
print('\nYou cannot change the value of tuples. I tried and failed.\n')
print("--------- Tuples: For Looping Print ---------") 
for dimension in dimensions:
    print(dimension)
print("--------- Tuples: Writing Over Tuples ---------") 
# You will need to create/redifine the variable to change the value like below. 
print('Original Dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('\nModified Dimensions:')
for dimension in dimensions:
    print(dimension)




