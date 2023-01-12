print("--------- Try It Yourself! ---------")
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods Think of five simple foods, and store them in a tuple
buffet_foods = ('sushi','fried rice', 'chicken teriyaki','pan-fried potatoes','grilled salmon')

# Use a for loop to print each food the restaurant 
print("Buffet Menu:")
for buffet_food in buffet_foods:
    print(buffet_food.title())
print('------------------------------------')
# Try to modify one of the items, and make sure that Python rejects the change
print("\nI tried to change the menu from Chicken Teriyaki to General Tso's and was denied by python. I am sad...\n")
# buffet_foods[2] = 'general tso'

print('------------------------------------')
# The restaurant changes its menu, replacing two of the items with different foods
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu
buffet_foods = ('sushi','egg fried rice', 'general tso','pan-fried potatoes','grilled salmon')
print('New Buffet Menu:')
for buffet_food in buffet_foods:
    print(buffet_food.title())
