print("--------- Try It Yourself! ---------")
# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain
# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien
alien_color = 'green'
print('\n----- Test 1 -----')
if alien_color == 'green':
    print('You just earned 5 points for shooting the alien!')

print('\n----- Test 2 -----')
# If the alien’s color isn’t green, print a statement that the player just earned 10 points
alien_color = input("What color was the alien? ")
if alien_color != 'green':
    print("You just earned 10 points!")

print('\n----- Test 3 -----')
# Write one version of this program that runs the if block and another that runs the else block
alien_color = input("What color was the alien? ")
alien_color.lower()
if alien_color == 'green':
    print('You just earned 5 points for shooting the alien!')
else:
    print("You just earned 10 points!")