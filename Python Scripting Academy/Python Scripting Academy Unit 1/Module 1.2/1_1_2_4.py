# [x] get input for a variable, fav_food, that describes a favorite food
print("Dude, what's your favorite food ?")
fav_food = input()
# [x] display fav_food as ALL CAPS, used in a sentence
print("I WANT MY BLOODY",fav_food.upper(),"!")
# [x] display fav_food as all lower case, used in a sentence
print("Could I have a ",fav_food.lower(),"please?")
# [x] display fav_food with swapped case, used in a sentence
print("I think I will go to the hospital, I just had a ",fav_food.swapcase())
# [x] display fav_food with capitalization, used in a sentence
print("He ordered something.",fav_food.capitalize(),".")

fav_color = "Forest Green"
# [x] display the fav_color variable as upper, lower, swapcase, and capitalize formatting in a single print() statement
print(fav_color.upper(),fav_color.lower(),fav_color.swapcase(),fav_color.capitalize())

# [x] input variable fav_color as upper
fav_color = input("What's your favourite color? ").upper()
# [x] print fav_color
print(fav_color)

# [x] print 3 tests, with description text, testing the menu variable for 'pizza', 'soup' and 'dessert'
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print("'pizza' in menu = ", 'pizza' in menu)
print("'soup' in menu = ", 'soup' in menu)
print("'dessert' in menu = ", 'dessert' in menu)

# Create a program where the user supplies input to search the menu
search = input("Try to guess what is in the menu ! : ")
print("Your guess is:", search in menu)

# add to menu
print(menu)
add_item = input("What would you like to add to the menu ? ")
new_menu = menu + ', ' + add_item
print(new_menu)

# Testing Add to Menu - create user input to search for an item on the new menu
print("'pizza' in menu = ", 'salad' in menu)
print("'" + add_item + "'" + " in menu = ", 'salad' in menu)

# [x] fix the error
paint_colors = "red, blue, green, black, orange, pink"
print('Red in paint colors = ', 'red' in paint_colors)
