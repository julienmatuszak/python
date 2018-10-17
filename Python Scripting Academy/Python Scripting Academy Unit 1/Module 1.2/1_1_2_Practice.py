# [x] get user input for a variable named remind_me
remind_me = input()

# [x] print the value of the variable remind_me
print(remind_me)

# use string addition to print "remember: " before the remind_me input string
print("remember: " + remind_me)

# [x] get user input for 2 variables: meeting_subject and meeting_time
meeting_subject = input()
meeting_time = input()

# [x] use string addition to print meeting subject and time with labels
print(meeting_subject + " at " + meeting_time)

# [x] print the combined strings "Wednesday is" and "in the middle of the week" 
print("Wednesday is","in the middle of the week")

# [x] print combined string "Remember to" and the string variable remind_me from input above
print("Remember to", remind_me)

# [x] Combine 3 variables from above with multiple strings
print("Remember! You have",meeting_subject,"at",meeting_time)

# [x] print a string sentence that will display an Apostrophe (')
print("This is an apostrophe: '")

# [x] print a string sentence that will display a quote(") or quotes
print('This is a quote: "')

# [x] complete vehicle tests 
vehicle = input("What's your vehicle ? ")
print("All Alpha:",vehicle.isalpha())
print("All Alphanumeric:",vehicle.isalnum())
print("Capitalized ?",vehicle.istitle())
print("All lowercase ?",vehicle.islower())

# [x] print True or False if color starts with "b" 
color = input("What's the color of your " + vehicle + " ? ")
print("Your car is blue:",color.lower().startswith("b"))

# [x] print the string variable capitalize_this capitalizing only the first letter
capitalize_this = "the TIME is Noon."
print(capitalize_this)
print(capitalize_this.capitalize())

# print the string variable swap_this in swapped case
swap_this = "wHO writes LIKE tHIS?"
print(swap_this)
print(swap_this.swapcase())

# print the string variable whisper_this in all lowercase
whisper_this = "Can you hear me?"
print(whisper_this)
print(whisper_this.lower())

# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"
print(yell_this)
print(yell_this.upper())

#format input using .upper(), .lower(), .swapcase, .capitalize()
format_input = input('enter a string to reformat: ')
print(format_input.upper())
print(format_input.lower())
print(format_input.swapcase())
print(format_input.capitalize())

# [x] get user input for a variable named color
color = input("What's the color of a white horse ? ")
# [x] modify color to be all lowercase and print
print(color.lower())

# [x] get user input using variable remind_me and format to all **lowercase** and print
remind_me = input("What do I have to remember already ? ")
print("**"+remind_me.lower()+"**")
# [x] test using input with mixed upper and lower cases

# [x] get user input for the variable yell_this and format as a "YELL" to ALL CAPS
yell_this = input("WHAT ARE YOU SAYING ? ")
print(yell_this.upper())

# [x] get user input for the name of some animals in the variable animals_input
animals_input = 'bear, wolf, cat, octopus'

# [x] print true or false if 'cat' is in the string variable animals_input
print('Is cat in the list? :', 'cat' in animals_input)

# [x] get user input for color
color = input("Name your color : ")

# [x] print True or False if color starts with "b"
print('Does your color start with "b"? : ',color.startswith('b'))

# [x] print color variable value exactly as input 
#     test with input: "Blue", "BLUE", "bLUE"

# project: "guess what I'm reading"
# 1[x] get 1 word input for can_read variable
can_read = input("enter 1 word item that can be read: ")
# 2[x] get 3 things input for can_read_things variable
can_read_things = input("enter 3 items that can be read: ")
# 3[x] print True if can_read is in can_read_things
print(can_read in can_read_things)
# [x] challenge: format the output to read "item found = True" (or false)
print("item found = ", can_read in can_read_things)
# hint: look print formatting exercises


# Allergy check 

# 1[x] get input for test
input_test = input("enter some things eaten in the last 24 hours: ").lower()

# 2/3[x] print True if "dairy" is in the input or False if not
print("dairy" in input_test)

# 4[x] Check if "nuts" are in the input
print('nuts' in input_test)

# 4+[x] Challenge: Check if "seafood" is in the input
print("seafood is in the input:", 'seafood' in input_test)

# 4+[x] Challenge: Check if "chocolate" is in the input
print("chocolate is in the input:", 'chocolate' in input_test)

# 5[x] Challenge: make your code work for input regardless of case, e.g. - print True for "Nuts", "NuTs", "NUTS" or "nuts"


