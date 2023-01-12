print('\n----- Dictonaries: A Dictionary of Similar Objects  -----')
# You can create your lists/dictionaries in this format for readablility just makes sure spaces are correct. MOST IDEs do this for you. 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# This proves that you can also break your "Print Statements" ... Gonna be honest... dont like how this looks at all. 
print(favorite_languages)
print("Sarah's favoriate language is " +
    favorite_languages['sarah'].title() +
    ".")

print("Phil's favorite language is " + favorite_languages['phil'].title() + ".")


print('\n----- Dictonaries: Looping through a Dictionary  -----')
print('----- Looping Through ALL Key-Value Pairs -----')
print("--- Append: Using forLoop to loop through both 'KEY and VALUE'---")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print('----- Looping Through ALL Keys in a Dictionary -----')
# keys() method is used to pull what seems to be the "keys" used in the dictionary and stores them to a variable. 
# keys() method is some what option all 
for name in favorite_languages.keys():
    print(name.title())

print('\n----- Test: Looping Through ALL Keys in a Dictionary without keys() Method -----')
for poll_name in favorite_languages:
    print(poll_name.title())

print('\n------------------------------------\n')

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

print('\n------------------------------------\n')

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n----- Looping Through a Dictionary's Keys in Order -----")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking our poll.")

print("\n----- Looping Through All Values in a Dictionary -----")
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
# set = a list that requires each item to be unique (removes dups)
print("\nThe following languages have been mentioned(without duplicates): ")
for language in set(favorite_languages.values()):
    print(language.title())


print('\n----- Dictonaries: Nesting -----')
print('----- A List in a  Dictionary -----')
print("--- Append: Using Nesting'---")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python','haskell']
    }

for name , languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())