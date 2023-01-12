print("--------- Try It Yourself! ---------")
# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary However, to avoid confusion, let’s call it a glossary
    # • Think of five programming words you’ve learned about in the previous chapters Use these words as the keys in your glossary, and store their
    # meanings as values
    # • Print each word and its meaning as neatly formatted output You might print the word followed by a colon and then its meaning, or print the word
    # on one line and then print its meaning indented on a second line Use the newline character (\n) to insert a blank line between each word-meaning
    # pair in your output

glossary = {
    'variable': "a name that refers to a place in a computer’s memory where data is stored. More loosely, it can also be used to refer to that data.",
    'string': 'text data, which can be stored in a variable.',
    'loop': 'a piece of code that keeps repeating until a certain condition is met.',
    'comparative operator': ' sometimes called logic operators, they allow us to compare data in a program.',
    'mathematical operator': ' an operator that performs some mathematical function on some numbers.'
}

print('\n---- Python Glossary Words ---')
print('Variable: ' + glossary['variable'] + '.')
print('String: ' + glossary['string'] + '.')
print('Loop:' + glossary['loop'] + '.')
print('Comparative Operator: ' + glossary['comparative operator'] + '.')
print('Mathematical Operator: ' + glossary['mathematical operator'] + '.\n')