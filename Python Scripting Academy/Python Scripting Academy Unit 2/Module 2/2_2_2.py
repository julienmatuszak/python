# Currency Values
# [x] create a list of 3 or more currency denomination values, cur_values
# cur_values, contains values of coins and paper bills (.01, .05, etc.)
cur_values = [.01, .05, .10]

# [x] print the list
print(cur_values)

# [x] append an item to the list and print the list
cur_values.append(0.20)
print(cur_values)

# Currency Names
# [x] create a list of 3 or more currency denomination NAMES, cur_names
# cur_names contains the NAMES of coins and paper bills (penny, etc.)
cur_names = ["penny", "fiver", "dime"]
# [x] print the list
print(cur_names)

# [x] append an item to the list and print the list
cur_names.append("twenty cents")
print(cur_names)

# [x] append additional values to the Currency Names list using input()
cur_names.append(input("Give me the name of the next currency unit"))
# [x] print the appe

# [x] complete the Birthday Survey task above
bday_survey = []
bday = input("What is the day of the month of your birth? (1-31 or 'q' to quit) ")
while bday.lower().startswith("q")is False:
    bday_survey.append(bday)
    bday = input("What is the day of the month of your birth? (1-31 or 'q' to quit) ")
    
print(bday_survey)

# [x] Fix the Error
three_numbers = [1, 1, 2]
print("an item in the list is: ", three_numbers[2])

