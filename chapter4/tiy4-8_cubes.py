print("--------- Try It Yourself! ---------")
#   4-8. Cubes: A number raised to the third power is called a cube For example, the cube of 2 is written as 2**3 in Python.
#   Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
for cubes in cubes:
    print(cubes)

test = 1**3
print('Test: ' + str(test))