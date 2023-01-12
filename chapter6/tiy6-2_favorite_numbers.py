print("--------- Try It Yourself! ---------")
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers Think of five names, and use them as keys in your dictionary
# Think of a favorite number for each person, and store each as a value in your dictionary
# Print each person’s name and their favorite number For even more fun, poll a few friends and get some actual data for your program

favorite_numbers = {
    'warshawski': 5,
    'amber': 7, 
    'favi': 14, 
    'tavin': 15, #Made it up. 
    'tre': 69 # For balance of the Yin and the Yang.... 
    }

print("Tre's favorite number is " + str(favorite_numbers['tre']) + ".")
print("Warshawski's favorite number is " + str(favorite_numbers['warshawski']) + ".")
print("Amber's favorite number is " + str(favorite_numbers['amber']) + ".")
print("Favi's favorite number is " + str(favorite_numbers['favi']) + ".")
print("Tavin's favorite number is " + str(favorite_numbers['tavin']) + ".")

if favorite_numbers['tre'] == 69:
    print("\nTRE!!!! You have some explaining to do mister...\n")