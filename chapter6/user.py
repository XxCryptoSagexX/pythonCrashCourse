print('\n----- Dictonaries: Looping through a Dictionary  -----')

print('\n----- Looping Through ALL Key-Value Pairs -----')
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }
# Note that we are storing the value of what the items are in each dictionary.
# Possible catigorization is used with items() function. 
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

