# [x] Get user input for first_name
# [x] iterate through letters in first_name 
#    - print each letter on a new line
letter = ""
first_name = input("Tell me your first name please : ")
for letter in first_name:
    print(letter)

# [x] Create capitalize-io
first_name = input("Gimme your first name : ")
new_name = ""
for xyz in first_name:
    if xyz == "i":
        new_name += xyz.upper()
    elif xyz == "o":
        new_name += xyz.upper()
    else:
    	new_name += xyz
print (new_name)

# [x] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
other_word = ""
for a in long_word[0::2]:
    other_word += a
print (other_word)

# Mirror Color
# [x] get user input, fav_color
# [x] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"
fav_color = input("What's your favourite color ? ")
roloccolor = ""
for a in fav_color[::-1]:
    roloccolor += a
print(roloccolor+fav_color)
