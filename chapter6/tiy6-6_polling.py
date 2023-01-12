print("--------- Try It Yourself! ---------")
# 6-6. Polling: Use the code in favorite_languages.py (page 104)
    # • Make a list of people who should take the favorite languages poll Include some names that are already in the dictionary and some that are not
    # • Loop through the list of people who should take the poll If they have already taken the poll, print a message thanking them for responding
    # If they have not yet taken the poll, print a message inviting them to take the poll.
    # BONUS APPEND: Sort the list 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

participants = ['henry','david', 'phil', 'edward','sarah']

for participant in participants:
        if participant in favorite_languages.keys():
            print("Thanks for your participation, " + participant.title() + ".")
        else:
            print(participant.title() + ", please consider taking the poll.")