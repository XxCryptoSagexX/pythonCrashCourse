print("--------- Try It Yourself! ---------")
# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values When you’re sure that your loop works, add five more Python terms to your
# glossary When you run your program again, these new words and meanings should automatically be included in the output
    # BONUS APPEND: Sort the list created and apply a special parameter to one of your terms. 

glossary = {
    'variable': "a name that refers to a place in a computer's memory where data is stored. More loosely, it can also be used to refer to that data.",
    'string': 'text data, which can be stored in a variable.',
    'loop': 'a piece of code that keeps repeating until a certain condition is met.',
    'comparative operator': 'sometimes called logic operators, they allow us to compare data in a program.',
    'mathematical operator': 'an operator that performs some mathematical function on some numbers.',

    'integer': "a number data-type that cannot have a decimal value and must be a whole number.",
    'syntax error': 'an error produced when a computer fails to run a program because it cannot recognise the format of the code supplied',
    'operator': 'a symbol that performs a simple function on some code such as multiplying two numbers or comparing them to see if they are equal.',
    'ide': 'stands for Integrated Development Environment.',
    'float': 'a number data-type that can have a decimal value.'
    }

print('\n---- Python Glossary Words ---')

for term, definition in sorted(glossary.items()):
    if term == 'ide':
        print(term.upper() + ": " + definition)
    else:
        print(term.title()+ ": " + definition)
