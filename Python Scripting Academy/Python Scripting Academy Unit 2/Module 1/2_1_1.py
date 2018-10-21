# [x] assign a string 5 or more letters long to the variable: street_name
# [x] print the 1st, 3rd and 5th characters
street_name = "Taikos"
print(street_name[0],street_name[2],street_name[4])

# [x] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [x] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else
team_name = input('Put the name of your team with "i", "o", "u" as 2nd character : ')
if team_name[1].lower() == "i":
    print('The 2nd character of the name of your team is "i"')
elif team_name[1].lower() == "o":
    print('The 2nd character of the name of your team is "o"')
elif team_name[1].lower() == "u":
    print('The 2nd character of the name of your team is "u"')
else:
    print("Ah, you might not have understood the directives or made a mistake. Try again!")# [x] assign a string 5 or more letters long to the variable: street_name

# [x] print the last 3 characters of street_name
street_name = "Taikos"
print(street_name[-3],street_name[-2],street_name[-1])

# [x] create and assign string variable: first_name
first_name = "Julien"
# [x] print the first and last letters of name
print(first_name[0],first_name[-1])

# [x] Review, Run, Fix the error using string index
shoe = "tennis"
# print the last letter
print(shoe[-1])
