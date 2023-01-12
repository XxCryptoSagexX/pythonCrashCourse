print("--------- Try It Yourself! ---------")
# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'
alien_color = 'green'

print('\n----- Test 1 -----')
# Write an if statement to test whether the alien’s color is green
# If it is, printa message that the player just earned 5 points
if alien_color == 'green':
    print("You just earned 5 points!")

print('\n----- Test 2 -----')
# Write one version of this program that passes the if test and another that fails (The version that fails will have no output )
alien_color = 'Red'
if alien_color == 'green':
    print("You just earned 5 points!")
print('Test was done... And Failed... ')

alien_color = 'red'
if alien_color == 'red':
    print("You just earned 5 points! Thanks for choosing RED!")