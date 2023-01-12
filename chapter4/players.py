print('--------- Splicing A List ---------')
# This is you basically using only specific 'range' of a list.
# Remebmer that it is similar to range so you go past the index you want. Meaning if there are 5 and you want 4 you must put 5
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print('\tYou selected the following players(1-3): ' + str(players[0:3]))
print('------------------------------------')
print(players[1:4])
print('\tYou selected the following players(2-4): ' + str(players[0:3]))
print('------------------------------------')
# Without a starting in dex python will automatically start from beginning.
print(players[:4])
print('\tYou selected the following players(1-4): ' + str(players[0:3]))
print('------------------------------------')
# without an ending index pythong will automatically end with remaining elements.
print(players[2:])
print('\tYou selected the following players(3-5): ' + str(players[0:3]))
#Negative inverse exist here too. 
players = ['charles','martina','michael','florence','eli']
print(players[-3:])

print('------------------------------------')
print('------------------------------------')

print('--------- Looping Through a Slice ---------')
players = ['charles','martina','michael','florence','eli']
print('Here are the first three players of my team:')
for player in players[:3]:
    print(player.title())