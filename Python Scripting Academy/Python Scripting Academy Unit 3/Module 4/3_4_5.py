%%writefile sentence_counter.py
# [x] The following program contains a few functions to count the number of: vowels, consonants, and digits in a sentence.
# Modify the program so it only run the test case when the program is executed directly. 
# In other words, when the program is imported as a module for another program, it shouldn't display the test cases.
def count_vowels(sentence):
    """Count the number of vowels in sentence."""
    vowels = 0
    for c in sentence:
        if c.lower() in "aeiouy":
            vowels = vowels + 1
    return vowels
def count_consonants(sentence):
    """Count the number of consonants in sentence."""
    consonants = 0
    for c in sentence:
        if c.isalpha():
            if c.lower() not in "aeiouy":
                consonants = consonants + 1
    return consonants
def count_digits(sentence):
    """Count the number of digits in sentence."""
    digits = 0
    for c in sentence:
        if c.isdigit():
            digits = digits + 1
    return digits
test_sentence = "Plan 2 is not working!"
print("Number of vowels = {:d}".format(count_vowels(test_sentence)))
print("Number of consonants = {:d}".format(count_consonants(test_sentence)))
print("Number of digits = {:d}".format(count_digits(test_sentence)))

%%writefile stairs.py
# [x] The following program generates a staircase character art
# The `size` variable controls the number of steps
# The `base_shape` defines the characters used to generate the art
# Modify the program so the `size` is set as a positional command line argument, and base_shape as an optional 
# command line argument with a default value of `[]`
import argparse
def gen_stairs(steps, base_shape):
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print(base_shape, end = "")
        print()
# Define an argument parser object
parser = argparse.ArgumentParser()
# Add positional arguments
parser.add_argument('size', action = 'store', type = int, help = 'Controls the numbers of steps')
# Add optional arguments
parser.add_argument('-b', '--base_shape', metavar = 'shape', action = 'store', type = str, default = "[]", help = 'Defines the characters used to generate the art')
# Parse command-line arguments
args = parser.parse_args()
# Program
# Generate a staircase with steps using '[]` as default a base shape 
gen_stairs(args.size, args.base_shape)

%%writefile day_counter.py
# [x] Write a program that reads a date from the command line as numbers (month  then day then year),
# if the date entered is in the past, a message saying "The date has passed" should be printed
# if the date is in the future the program should display the number of days remaining from today till that date,
# there should be an optional command line flag that displays the results in total number of seconds instead of days
import argparse
from datetime import datetime, timedelta
# help message should look like:
'''
usage: day_counter.py [-h] [-s] month day year
positional arguments:
  month                Month as a number (1, 12)
  day                  Day as a number (1, 31) depending on the month
  year                 Year as a 4 digits number (2018)

optional arguments:
  -h, --help           show this help message and exit
  -s, --total_seconds  Show the time difference in total number of seconds
'''
# Define an argument parser object
parser = argparse.ArgumentParser()
# Add positional arguments
parser.add_argument('month', action = 'store', type = int, help = 'Month as a number (1, 12)')
parser.add_argument('day', action = 'store', type = int, help = 'Day as a number (1, 31) depending on the month')
parser.add_argument('year', action = 'store', type = int, help = 'Year as a 4 digit number (2018)')
# Add optional arguments
parser.add_argument('-s', '--total_seconds', action = 'store_true', help = 'Show the time difference in total number of seconds')
# Parse command-line arguments
args = parser.parse_args()
# Program
t = datetime(month = args.month, day = args.day, year = args.year)
td = abs(t - datetime.today())
if t < datetime.today():
    print("The date has passed")   
else:
    print("There is",td.days,"days left until this date")
# If args.total_seconds is used, print the date with the complete format
if args.total_seconds:
        print("There is",int(td.total_seconds()),"seconds difference between this date and today")

%%bash
python3 day_counter.py 3 2 2018 -s

%%writefile adder.py
# [x] Write a program that reads an unspecified number of integers from the command line,
# then prints out the sum of all the numbers
# the program should also have an optional argument to show the product of the numbers (in addition to the sum)
# help message should look like:
'''
usage: adder.py [-h] [-p] [numbers [numbers ...]]
positional arguments:
  numbers        numbers to be added (or multiplied)
optional arguments:
  -h, --help     show this help message and exit
  -p, --product  show the product of the numbers (in addition to the displayed
                 sum)
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('numbers', action = 'store', nargs = '*', type = int, help = 'numbers to be added (or multiplied)')
parser.add_argument('-p', '--product', action = 'count', help = 'show the product of the numbers (in addition to the displayed sum)')
args = parser.parse_args()
print(sum(args.numbers))
if args.product:
    a = 1
    for b in args.numbers:
        a *= b
    print(a)

%%bash
python3 adder.py 2 3 5 10 -p

# The following program displays the double of a number
# Fix the error/s in the program so the correct answer is displayed
def double(num):
    answer = num * 2
    return answer
print(double(6))

# [x] The program below converts a length from Centimeters to Inches, Feet, Yards, and Miles
# Complete the functions cent2inches, cent2feet, cent2yards, cent2miles so they all return the expected result
def cent2inches(length):
    """
    Convert length from Centimeters to Inches.
    
    1 Centimeter = 0.393701 Inches   
    args:
        length: in Centimeter (float)        
    results:
        result: equivalent length in Inches (float)
    """
    result = 0.393791 * length  
    return result
def cent2feet(length):
    """
    Convert length from Centimeters to Feet.    
    1 Centimeter = 0.0328084 Feet    
    args:
        length: in Centimeter (float)        
    results:
        result: equivalent length in Feet (float)
    """
    result = 0.0328084 * length  
    return result
def cent2yards(length):
    """
    Convert length from Centimeters to Yards.   
    1 Centimeter = 0.0109361 Yards   
    args:
        length: in Centimeter (float)       
    results:
        result: equivalent length in Yards (float)
    """
    result = 0.0109361 * length  
    return result
def cent2miles(length):
    """
    Convert length from Centimeters to Miles.
    
    1 Centimeter = 6.2137e-6 Miles   
    args:
        length: in Centimeter (float)        
    results:
        result: equivalent length in Miles (float)
    """
    result = 6.2137e-6 * length  
    return result
def main():
    length = float(input("Enter length in Centimeters: "))    
    # In Inches
    inches = cent2inches(length)   
    # In Feet
    feet = cent2feet(length)   
    # In Yards
    yards = cent2yards(length)   
    # In Miles
    miles = cent2miles(length)    
    print('{:.2f} [cm] = {:.2f} [inches]", {:.2f} [feet], {:.2f} [yards], {:.2e} [miles]'.format(length, inches, feet, yards, miles))
if __name__ == '__main__':
    main()
    
# [x] The program below converts a length from Centimeters to Feet without using direct conversion
# Complete the functions cent2inches, inches2feet, and cent2feet so they return the expected result
# You should use cent2inches and inchest2feet in cent2feet
def cent2inches(length):
    """
    Convert length from Centimeters to Inches.
    
    1 Centimeter = 0.393701 Inches    
    args:
        length: in Centimeter (float)        
    results:
        result: equivalent length in Inches (float)
    """
    result = 0.393701 * length
    return result
def inches2feet(length):
    """
    Convert length from Inches to Feet.    
    1 Inch = 0.0833333 Feet    
    args:
        length: in Inches (float)        
    results:
        result: equivalent length in Feet (float)
    """
    result = 0.0833333 * length
    return result
def cent2feet(length):
    """
    Convert length from Centimeters to Yards.   
    The conversion rate is unknown, you have to use cent2inches and inches2feet   
    args:
        length: in Centimeter (float)       
    results:
        result: equivalent length in Yards (float)
    """
    result = inches2feet(cent2inches(length))
    return result
def main():
    length = float(input("Enter length in Centimeters: "))   
    # In Feet
    feet = cent2feet(length)   
    print('{:.2f} [cm] = {:.2f} [feet]'.format(length, feet))    
if __name__ == '__main__':
    main()    

# [x] Complete the function `formatted_phone()` so it displays the PHONE number as 777-248-3940
PHONE = "7895550153"
def formatted_phone():
    print("{:s}-{:s}-{:s}".format(PHONE[0:3],PHONE[3:6],PHONE[6:]))
formatted_phone()

# [x] In the following program, the function change_x should change the value stored in x from 5 to 7
# modify the function so the value of x is changed from within the function
x = 5
def change_x():
    global x
    x = 7  
print("Before change x =", x) # should be 5
change_x()
print("After change x =", x) # should be 7

# [x] The function upper_case should change the NAME to upper case
# correct the function so that NAME is changed permanently
# HINT: Use the string function str.upper()
NAME = "Skye Homsi"
def upper_case():
    global NAME
    NAME = NAME.upper()
    return NAME
print("Current name case:", NAME)
upper_case()
print("Updated name case:", NAME)

# [x] The function `average` computes the average of a list (or tuple) T
# Document the function using a one-line docstring
def average(T):
    '''computes the average of a list (or tuple)'''
    s = 0
    for num in T:
        s = s + num
    return s / len(T)   
print(average.__doc__)
help(average)

# [x] The following functions compute the area and circumference of a circle with radius r
# Document both function using a one-line docstring
from math import pi
def circle_area(r):
    '''computes the area of a circle with radius r'''
    return pi * r ** 2
def circle_circumference(r):
    '''computes the circumference of a circle with radius r'''
    return 2 * pi * r
print(circle_area.__doc__)
help(circle_area)
print(circle_circumference.__doc__)
help(circle_circumference)

# [x] As you saw before, the function gen_stairs generates a number of stairs using (base_shape)
# Document the function using a multi-line docstring
def gen_stairs(steps, base_shape):
    '''generates a number of stairs using a base shape'''
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print(base_shape, end = "")
        print()
# Generate a staircase with 6 steps using '[]` as a base shape               
gen_stairs(6, '[]')
print(gen_stairs.__doc__)
help(gen_stairs)

# [x] The following function returns the minimum and maximum of a tuple (or list) T
# # Document the function using a multi-line docstring
def min_max(T):
    '''
    finds the minimum and maximum within a list / tuple   
    args:
        table / tuple     
    returns:
        minimum and maximum within the list / tuple
    
    '''
    return (min(T), max(T))
print(min_max.__doc__)
help(min_max)
