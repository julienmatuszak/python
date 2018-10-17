#executing this file in a terminal will not output the types and will need a quoted input for strings

# [x] get input for the variable student_name
student_name = input()
# [x] determine the type of student_name
type(student_name)

# [x] run cell several times entering a name a int number and a float number after adding code below
print("enter a name or number")
test_input = input()
# [x] insert code below to check the type of test_input
type(test_input)

student_name = input("enter the student name: ")  
print("Hi " + student_name)

# [x] get user input for a city name in the variable named city
city = input()
# [x] print the city name
print(city)

# [x]create variables to store input: name, age, get_mail with prompts
# for name, age and yes/no to being on an email list
print("What is your name ?")
name = input()
print("And what is your age ?")
age = input()
print("Last thing, do you want emails ? (yes/no)")
get_mail = input()

# [x] print a description + variable value for each variable
print("name = " + name + "\n" + "age = " + age + "\n" + "wants email = " + get_mail + "\n")
