# [x] print 3 strings on the same line using commas inside the print() function 
print("I have a big", "task", "tomorrow")

# review and run code
number_errors = 0
print("An Integer of", 14, "combined with strings causes",number_errors,"TypeErrors in comma formatted print!")

# [x] use a print() function with comma separation to combine 2 numbers and 2 strings
print("Correction, I have",2,"tasks to do until", 4)

# [x] get user input for a street name in the variable, street
print("Btw, what's the name of your street ?")
street = input()
# [x] get user input for a street number in the variable, st_number
print("Hei, you forgot the street number !")
st_number = input()
# [x] display a message about the street and st_number
print("Ok, so you leave on",street,"gatve and your namas is", st_number)

# [x] define a variable with a string or numeric value
string = "2"
# [x] display a message combining the variable, 1 or more literal strings and a number
print("This number ->",string,"is actually a string but this one ->",2,"is not!")

# [x] get input for variables: owner, num_people, training_time  - use descriptive prompt text
owner = input("enter the name of the person to contact for the training group: ")
num_people = input("enter the total number of people attending the course: ")
training_time = input("enter the training time selected: ")
# [x] create a integer variable min_early and "hard code" the integer value (e.g. - 5, 10 or 15)
min_early = 5
# [x] print reminder text using all variables & add additional strings -  use comma separated print formatting
print("------------------------------")
print("Reminder: chicha smoking training is scheduled at",training_time,"for the",owner,"group of",num_people,"attendee(s)")
print("Please arrive",min_early,"minutes late for the first class")
