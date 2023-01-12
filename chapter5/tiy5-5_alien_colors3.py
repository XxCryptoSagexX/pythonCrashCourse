print("--------- Try It Yourself! ---------")

username = input("What is your name? ")

print('\n\n----- Test 1 -----')
# If the alien is green, print a message that the player earned 5 point
alien_color = 'green'
print("You have chosen the color " + alien_color + '.')   
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print('You just earned 10 points!')
elif alien_color == 'red':
    print("You just earned 15 points!")

print('\n----- Test 2 -----')

# If the alien is yellow, print a message that the player earned 10 point
alien_color = 'yellow'    
print("You have chosen the color " + alien_color + '.')   
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print('You just earned 10 points!')
elif alien_color == 'red':
    print("You just earned 15 points!")

print('\n----- Test 3 -----')
# If the alien is red, print a message that the player earned 55 point
alien_color = 'red'    
print("You have chosen the color " + alien_color + '.')   
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print('You just earned 10 points!')
elif alien_color == 'red':
    print("You just earned 15 points!")

print('\n----- Test 4 -----')
print('You were told to make 3 separate programs... Do you have 3?')
answer = input("\nDo you have three programs? ")
answer = answer.lower()

if answer == 'yes':
    print('\nJob well done, ' + username.title() + "!")
    print('\nJolly good show!')
else:
    print('\n' + username.title() + ", you need more practice!\n")
    