print('\n----- Simple Dictonary -----')

# Notice that dictionaries use the {} 
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print('\n------------------------------------\n')
# Note that the dictionary value is converted to variable then used 
new_points = alien_0['points']
print("Green Alien was defeated!")
print("You just earned " + str(new_points) + 'points.')

print('\n----- Variable Test: Dictionary -----')
# Note that this did work but their is probably a reason for why you would not do this. 
print("You just earned " + str(alien_0['points']) + ' points.')


print('\n----- Dictonaries: Adding New Key-Value Pairs  -----')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('\n----- Dictonaries: Starting with an Empty Dictionary  -----')
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print('\n----- Dictonaries: Modifying Values in a Dictionary  -----')
alien_0 = {'color': 'green'}
print('The alien is ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print('The alien is ' + alien_0['color'] + '.')

print('\n------------------------------------\n')
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# alien_0['speed'] = 'fast'

# Move the alien to the right
# Determine how far to move the alien based on its current position
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

print('\n----- Dictonaries: Removing Key-Value Pairs  -----')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


print('\n----- Dictonaries: Nesting -----')
print('----- A List of Dictonaries -----')
print("--- Append: Using Nesting'---")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n--- Append: Using Nesting'---")
# make an empty list for storing aliens
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Modifying green aliens to yellow via slicing. 
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have benn created.
print("total number of aliens: " + str(len(aliens)))

