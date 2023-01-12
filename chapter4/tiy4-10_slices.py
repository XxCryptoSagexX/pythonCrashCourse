print("--------- Try It Yourself! ---------")
# Print the message, The first three items in the list are: Then use a slice to print the first three items from that program’s list
magicians = ['alice','david','caroline','harry','ron','severus','dumbledore']
print('The first three magicians are:')
for magician in magicians[:3]:
    print(magician.title())
print('------------------------------------')
# Print the message, Three items from the middle of the list are: Use a slice to print three items from the middle of the list
print('Three magicians from the middle of the list are:')
for magician in magicians[2:5]:
    print(magician.title())
print('------------------------------------')
#Print the message, The last three items in the list are: Use a slice to print the last three items in the list
print('The last three magicians are:')
for magician in magicians[4:]:
    print(magician.title())
