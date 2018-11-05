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

%%writefile weather.py
# [x] In this project, you will read a CSV file containing about 25K lines of weather information 
# and store the information in a Python dictionary. You will then use the dictionary to find out
# the hottest, coldest, rainiest years and so on...
# You will see that the dictionary's search optimization algorithms will allow you to explore 
# this large dataset without any noticeable delays.
# The logic of the program is in the `main` function, read it before writing any code.
# Use the description and examples under each of the following functions to implement them:
# 1) convert_file(file_path)
# 2) add_rainy(weather)
# 3) consolidate(weather)
# 4) year_info(year, yearly_weather)
# 5) hottest(yearly_weather)
# 6) coldest(yearly_weather)
# 7) rainiest_days(yearly_weather)
# 8) highest_prcp(yearly_weather)
from datetime import date, datetime
import os
def convert_file(file_path):
    """
    Convert CSV file to a Python dictionary.
    
    The CSV file contains daily weather information arranged in rows,
    the rows contain  (date, precipitation (inches), maximum temperature (F), minimum temperature (F)) in order.
    First line in CSV file is a header (DATE, PRCP, TMAX, TMIN), the rest contain the weather data.   
    The function should read the data in the file and generate a dictionary where:
        1) keys are date objects (from the datetime module), using the daily date info in the file
        2) values are lists containing [TMAX, TMIN, PRCP] in order      
    args:
        file_path: path to the CSV file    
    returns:
        weather: the generated dictionary using date objects as keys and lists of weather info as values        
    examples:
    Input CSV file:
    DATE,PRCP,TMAX,TMIN
    12/10/2017,0,49,34
    12/11/2017,0,49,29
    12/12/2017,0,46,32
    12/13/2017,0,48,34
    12/14/2017,0,50,36
    12/15/2017,0.06,43,37
    12/16/2017,0.14,45,37
    12/17/2017,0.03,50,42
    12/18/2017,0.7,49,41
    12/19/2017,1,50,40
    12/20/2017,0.13,49,32
    12/21/2017,0.01,41,29
    12/22/2017,0.09,40,35
    12/23/2017,0,38,29
    12/24/2017,0.12,38,28
    Output dictionary (weather):
    {datetime.date(2017, 12, 10): [49, 34, 0.0],
     datetime.date(2017, 12, 11): [49, 29, 0.0],
     datetime.date(2017, 12, 12): [46, 32, 0.0],
     datetime.date(2017, 12, 13): [48, 34, 0.0],
     datetime.date(2017, 12, 14): [50, 36, 0.0],
     datetime.date(2017, 12, 15): [43, 37, 0.06],
     datetime.date(2017, 12, 16): [45, 37, 0.14],
     datetime.date(2017, 12, 17): [50, 42, 0.03],
     datetime.date(2017, 12, 18): [49, 41, 0.7],
     datetime.date(2017, 12, 19): [50, 40, 1.0],
     datetime.date(2017, 12, 20): [49, 32, 0.13],
     datetime.date(2017, 12, 21): [41, 29, 0.01],
     datetime.date(2017, 12, 22): [40, 35, 0.09],
     datetime.date(2017, 12, 23): [38, 29, 0.0],
     datetime.date(2017, 12, 24): [38, 28, 0.12]}
    """
    os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/")
    if (file_path not in os.listdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/")):
        print("STOP!!!! Run the environment setup code!")
        return None
    else:
        weather = {}
        with open(file_path, 'r') as f:
            skip = f.readline()
            for a in range(0,25561):
                u = f.readline()
                u = u.rstrip()
                u = u.split(",")
                c = date_creater(u[0])
                if u[1] == "":
                    u[1] = 0
                if u[2] == "":
                    u[2] = 0
                if u[3] == "":
                    u[3] = 0
                weather[c] = [int(u[2]),int(u[3]),float(u[1])]
        return weather   
    #[x] open the file for reading (HINT: use `with` statement)
    #[x] ignore the first header line (DATE, PRCP, TMAX, TMIN)
    #[x] remove newline characters from end of each line (HINT: use str.rstrip())
    #[x] split line into a list (HINT: use str.split(','))
    #[x] create the date object from the first list element 
    # HINT: use the date_creater(date_string) function provided below
    #[x] read the weather related variables
    # precipitation
    # maximum temperature
    # minimum temperature   
    #[x] create dictionary key:value pair
def add_rainy(weather):
    """
    Emphasize rainy days using Boolean values.    
    Modify the weather dictionary by adding another Boolean element to the values' lists. 
    If precipitation is observed on a day (more than 0"), the associated list is appended by True.
    If precipitation is not observed (0"), the associated list is appended by False.   
    args:
        weather: dictionary, keys are date objects and values are lists [TMAX, TMIN, PRCP]        
    returns:
        None: the weather dictionary is modified directly, keys are date objects and values are lists [TMAX, TMIN, PRCP, RAINY_DAY]        
    examples:
    Input weather dictionary:
    {datetime.date(2017, 12, 10): [49, 34, 0.0],
     datetime.date(2017, 12, 11): [49, 29, 0.0],
     datetime.date(2017, 12, 12): [46, 32, 0.0],
     datetime.date(2017, 12, 13): [48, 34, 0.0],
     datetime.date(2017, 12, 14): [50, 36, 0.0],
     datetime.date(2017, 12, 15): [43, 37, 0.06],
     datetime.date(2017, 12, 16): [45, 37, 0.14],
     datetime.date(2017, 12, 17): [50, 42, 0.03],
     datetime.date(2017, 12, 18): [49, 41, 0.7],
     datetime.date(2017, 12, 19): [50, 40, 1.0],
     datetime.date(2017, 12, 20): [49, 32, 0.13],
     datetime.date(2017, 12, 21): [41, 29, 0.01],
     datetime.date(2017, 12, 22): [40, 35, 0.09],
     datetime.date(2017, 12, 23): [38, 29, 0.0],
     datetime.date(2017, 12, 24): [38, 28, 0.12]}    
    Updated weather dictionary with Boolean values
    {datetime.date(2017, 12, 10): [49, 34, 0.0, False],
     datetime.date(2017, 12, 11): [49, 29, 0.0, False],
     datetime.date(2017, 12, 12): [46, 32, 0.0, False],
     datetime.date(2017, 12, 13): [48, 34, 0.0, False],
     datetime.date(2017, 12, 14): [50, 36, 0.0, False],
     datetime.date(2017, 12, 15): [43, 37, 0.06, True],
     datetime.date(2017, 12, 16): [45, 37, 0.14, True],
     datetime.date(2017, 12, 17): [50, 42, 0.03, True],
     datetime.date(2017, 12, 18): [49, 41, 0.7, True],
     datetime.date(2017, 12, 19): [50, 40, 1.0, True],
     datetime.date(2017, 12, 20): [49, 32, 0.13, True],
     datetime.date(2017, 12, 21): [41, 29, 0.01, True],
     datetime.date(2017, 12, 22): [40, 35, 0.09, True],
     datetime.date(2017, 12, 23): [38, 29, 0.0, False],
     datetime.date(2017, 12, 24): [38, 28, 0.12, True]}
    """
    for a in weather.keys():
        if weather[a][2] > 0:
            weather[a].append(True)
        else:
            weather[a].append(False)
def consolidate(weather):
    """
    Consolidate the daily weather information by year.    
    Use the weather dictionary to generate a new consolidated dictionary (yearly_weather). 
    The new dictionary uses years as keys, and the associated values are lists containing (in order):
        1) The average of the highest recorded temperatures in the year (AVG_TMAX)
        2) The average of the lowest recorded temperatures in the year (AVG_TMIN)
        3) The total recorded precipitation in the year (TOTAL_PRCP)
        4) The total number of rainy days in the year (TOTAL_RAINY_DAYS)
        5) The number of recorded days (TOTAL_DAYS). 
           This element is necessary to account for days where the station breaks (missing recordings),
           or if the year hasn't finished yet.         
    args: 
        weather: dictionary, keys are date objects and values are lists [TMAX, TMIN, PRCP, RAINY_DAY]   
    returns:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]                       
    examples:
    Input weather dictionary:
    {datetime.date(2017, 12, 10): [49, 34, 0.0, False],
     datetime.date(2017, 12, 11): [49, 29, 0.0, False],
     datetime.date(2017, 12, 12): [46, 32, 0.0, False],
     datetime.date(2017, 12, 13): [48, 34, 0.0, False],
     datetime.date(2017, 12, 14): [50, 36, 0.0, False],
     datetime.date(2017, 12, 15): [43, 37, 0.06, True],
     datetime.date(2017, 12, 16): [45, 37, 0.14, True],
     datetime.date(2017, 12, 17): [50, 42, 0.03, True],
     datetime.date(2017, 12, 18): [49, 41, 0.7, True],
     datetime.date(2017, 12, 19): [50, 40, 1.0, True],
     datetime.date(2017, 12, 20): [49, 32, 0.13, True],
     datetime.date(2017, 12, 21): [41, 29, 0.01, True],
     datetime.date(2017, 12, 22): [40, 35, 0.09, True],
     datetime.date(2017, 12, 23): [38, 29, 0.0, False],
     datetime.date(2017, 12, 24): [38, 28, 0.12, True]}     
     Output yearly_weather dictionary:
     {2017: [45.666666666666664, 34.333333333333336, 2.28, 9, 15]}
    """    
    yearly_weather = {}
    for a in range(1948,2018):
        total_days = 0
        rainy_days = 0
        total_prec = 0
        total_max = 0
        total_min = 0
        for b in weather.keys():
            if b.year == a:
                total_days += 1
                total_prec += weather[b][2]
                total_max += weather[b][0]
                total_min += weather[b][1]
                if weather[b][3] == True:
                    rainy_days += 1
        yearly_weather.update({a:[total_max/total_days, total_min/total_days, total_prec, rainy_days, total_days]})
    return yearly_weather
def year_info(year, yearly_weather):
    """
    Convert the year's weather information to a formatted string.   
    Look for the weather information of `year` in the `yearly_weather` dictionary.
    If it exists, convert the information list into a formatted string:
            YEAR | AVG_TMAX | AVG_TMIN | TOTAL_PRCP | TOTAL_RAINY_DAYS | TOTAL_DAYS
    If it does not exist, the formatted string should be:
            N/A  |    N/A   |    N/A   |     N/A    |        N/A       |    N/A       
    args:
        year: int value to look for in the yearly_weather dictionary       
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]    
    returns:
        formatted_string: containing the year's weather information                        
    examples:
    Input yearly weather dictionary:
    {2017: [45.666666666666664, 34.333333333333336, 2.28, 9, 15]}  
    Output formatted string:
    == year_info(2017, yearly_weather) == (contained in the dictionary)
    ' 2017 |         45.67 |        34.33 |   2.28" |            9 |             15 '
    
    == year_info(2055, yearly_weather) == (not contained in the dictionary)
    ' N/A  |      N/A      |     N/A      |   N/A   |     N/A      |      N/A       '
    """
    if year in yearly_weather.keys():
        return "{:>10s} | {:s} | {:s} | {:s} | {:s} | {:s}".format("YEAR","AVG_TMAX","AVG_TMIN","TOTAL_PRCP","TOTAL_RAINY_DAYS","TOTAL_DAYS")+"\n"+"{:>10d} | {:^8.5f} | {:^8.5f} | {:^10.2f} | {:^16d} | {:^10d}".format(year,yearly_weather[year][0],yearly_weather[year][1],yearly_weather[year][2],yearly_weather[year][3],yearly_weather[year][4])+"\n"          
    if year not in yearly_weather.keys():
        return "{:>10s} | {:s} | {:s} | {:s} | {:s} | {:s}".format("YEAR","AVG_TMAX","AVG_TMIN","TOTAL_PRCP","TOTAL_RAINY_DAYS","TOTAL_DAYS")+"\n"+"{:>10s} | {:^8s} | {:^8s} | {:^10s} | {:^16s} | {:^10s}".format("N/A","N/A","N/A","N/A","N/A","N/A")+"\n"
def hottest(yearly_weather):
    """
    Find the hottest year in yearly_weather.    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the highest average maximum temperature (highest AVG_TMAX)
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]     
    returns:
        hottest_year: the year with the highest maximum temperature average (AVG_TMAX)
    """
    return(max(yearly_weather))       
def coldest(yearly_weather):
    """
    Find the coldest year in yearly_weather.   
    Look through all the years in the yearly_weather dictionary and return the year with 
    the lowest average minimum temperature (lowest AVG_TMIN)
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] 
    
    returns:
        coldest_year: the year with the lowest minimum temperature average (AVG_TMIN)
    """
    return(min(yearly_weather))
def rainiest_days(yearly_weather):
    """
    Find the year with the largest number of rainy days in yearly_weather.
    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the largest TOTAL_RAINY_DAYS    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]     
    returns:
        rainiest_year: the year with the largest number of rainy days
    """
    total_rainy_max = 0
    for a in yearly_weather.keys():
        if yearly_weather[a][3] >= total_rainy_max:
            total_rainy_max = yearly_weather[a][3]
            year = a
    return(year)
def highest_prcp(yearly_weather):
    """
    Find the year with the highest total precipitation in yearly_weather.
    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the largest TOTAL_PRCP
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] 
    
    returns:
        rainiest_year: the year with the highest total precipitation
    """
    total_prec_max = 0
    for a in yearly_weather.keys():
        if yearly_weather[a][2] >= total_prec_max:
            total_prec_max = yearly_weather[a][2]
            year = a
    return(year)
def date_creater(date_string):
    """Convert the date_string (formatted as m/d/yyyy) to a date object."""
    date_string = date_string.split("/")
    if len(date_string[0]) == 1:
        a = "0"+date_string[0]
        date_string[0] = a
    if len(date_string[1]) == 1:
        b = "0"+date_string[1]
        date_string[1] = b
    if int(date_string[2]) >= 48 and int(date_string[2]) <= 99:
        c = "19"+date_string[2]
    if int(date_string[2]) >0 and int(date_string[2]) < 18:
        c = "20"+date_string[2]
    if date_string[2] == "00":
        c = "2000"
    date_string[2] = c
    date_string = "/".join(date_string)
    d = datetime.strptime(date_string, "%m/%d/%Y")
    return d.date()
def dashes(count):
    """Print a fancy line of `count` dashes"""
    print("o" + count *'-' + "o")
def page_header(title):
    """Print a page header with a title surrounded by dashes"""
    dashes(78)
    print("|{:^78s}|".format(title))
    dashes(78)
def table_header():
    """Print the first row in a table  (header row)"""
    print()
    print(' {0:^4s} | {1:^13s} | {2:^12s} | {3:^7s} | {4:^12s} | {5:^14s} '.format("Year", "Avg High Temp", "Avg Low Temp", "Precip", "# Rainy days", "# Recorded days"))
    dashes(78)    
def display(title, years, yearly_weather):
    """Print a page with a header, title, and the weather information of all years as found in yearly_weather"""
    page_header(title)
    table_header()   
    # if years contain a single int, convert to a single item list
    if type(years) is not list: years = [years]    
    # print weather information for all years
    for year in years:
        print(year_info(year, yearly_weather))         
    # display this page till you go back to the main menu
    while True:
        m = input("Return to main menu [y/n]?")
        if m in 'yesYesYES':
            break     
def main():
    # convert the data in the (csv) file into a Python dictionary
    weather = convert_file("seattle_weather.csv")   
    # highlight rainy days by adding a Boolean entry to the dictionary's values
    add_rainy(weather)   
    # consolidate the weather data by year then store the result in a new dictionary
    yearly_weather = consolidate(weather)
    # earliest and latest years on record
    min_year = min(yearly_weather)
    max_year = max(yearly_weather)
    # menus functionality
    while True:
        # display header
        page_header("Weather Records")
        # display main menu
        print()
        print("Main Menu (choose an option to display):\n")
        print("1. Summary of a certain year")
        print("2. All years summary table")
        print("3. Hottest year on record")
        print("4. Coldest year on record")
        print("5. Year with most rainy days")
        print("6. Year with the highest precipitation")
        print("7. Quit")
        print()
        # display footer with user input message
        dashes(78)
        while True:
            try:
                option = input("Select an option (1, 7): ")
                option = int(option)
                if 1 <= option <= 7:
                    break # break the user input loop only, main loop does NOT break
            except ValueError:
                print("Cannot convert {:} to int".format(type(option)))       
        # execute relevant function
        # 1. Summary of a certain year
        if option == 1:
            # ask the user for a valid year
            while True:
                try:
                    year = input("Enter a year ({} - {})".format(min_year, max_year))
                    year = int(year)
                    if min_year <= year <= max_year:
                        break
                except ValueError:
                    print("Cannot convert {:} to int".format(type(option)))
            display("Year Summary", year, yearly_weather)
        # 2. All years summary table 
        elif option == 2:
            years = list(sorted(yearly_weather))
            display("Tabular Summary", years, yearly_weather)      
        # 3. Hottest year on record
        elif option == 3:
            year = hottest(yearly_weather)
            display("Hottest year on record", year, yearly_weather)            
        # 4. Coldest year on record   
        elif option == 4:
            year = coldest(yearly_weather)
            display("Coldest year on record", year, yearly_weather)           
        # 5. Year with most rainy days    
        elif option == 5:
            year = rainiest_days(yearly_weather)
            display("Year with most rainy days", year, yearly_weather)      
        # 6. Year with the highest precipitation
        elif option == 6:
            year = highest_prcp(yearly_weather)
            display("Year with the highest precipitation", year, yearly_weather)          
        # 7. Quit    
        elif option == 7:
            break
# Run the program  
main()

%%bash
pydoc weather

%%writefile cipher.py
import argparse
import os
def parse_command_line():
    """
    Parse the command line arguments and return the parse_args object.   
    There should be 1 positional argument and 6 optional arguments.
    The help message generated by the parser should look like:    
    usage: cipher.py [-h] [-o outfile_path] [-k KEY] [-d] [-a] [-v] infile
    positional arguments:
      infile                input file to be encrypted or decrypted
    optional arguments:
      -h, --help            show this help message and exit
      -o outfile_path, --outfile outfile_path
                            output file
      -k KEY, --key KEY     encryption/decryption key (must be positive) (default
                            = 1)
      -d, --decrypt         decrypt the input file
      -a, --all             decrypt using all keys [1, 25], save outputs in
                            different files. (useful in case the key is lost or
                            unknown)
      -v, --verbose         verbose mode
    args:
        None        
    returns:
        args: generated argparse object with all the passed command line arguments      
    """
    parser = argparse.ArgumentParser()    
    # Add positional arguments
    parser.add_argument('infile', action = 'store', type = str, help = 'input file to be encrypted or decrypted')
    # Add optional arguments
    parser.add_argument('-o', '--outfile', metavar = 'outfile_path', action = 'store', type = str, help = 'output file')
    parser.add_argument('-k', '--key', metavar = 'KEY', action = 'store', default = 1, help = 'encryption/decryption key (must be positive) (default = 1)')
    parser.add_argument('-d', '--decrypt', action = 'store_true', help = 'decrypt the input file')
    parser.add_argument('-a', '--all', action = 'store_true', help = 'decrypt using all keys [1, 25], save outputs in different files. (useful in case the key is lost or unknown)')
    parser.add_argument('-v', '--verbose', action = 'store_true', help = 'verbose mode')
    args = parser.parse_args()
    #HINTS: Review Jupyter Notebook 3-4.1
    return(args)
def read_file(file_path):
    """
    Read file_path and return the content as string.  
    The file must be opened and closed and the function should handle exceptions when they are raised.    
    args:
        file_path: path to file
    returns:
        message: content of file in file_path as a string
    """
    os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 4/")
    if (file_path not in os.listdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 4/")):
        print("STOP!!!! Run the environment setup code!")
        return None
    else:
        with open(file_path,'r') as f:
            try:
                t = f.read()
            except FileOpenError as exception:
                print(exception)
            else:
                return t           
def write_file(message, file_path):
    """
    Write the message in file_path.    
    The file must be opened and closed and the function should handle exceptions when they are raised.    
    args:
        message: string to write in file
        file_path: path to file        
    returns:
        None
    """
    os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 4/")
    with open(file_path,'w') as f:
        try:
            f.write(message)
        except FileOpenError as exception:
            print(exception)
        else:
            return None
def transform(message, key, decrypt):
    """
    Encrypt or decrypt a message using Caesar cipher.   
    Encryption and decryption is determined by the Boolean value in decrypt. Key determines the number of 
    places a character is shifted. When encrypting, use the positive value of key to shift the characters forward; 
    when decrypting, use the negative key to shift the characters backward.     
    The function should maintain characters that are not letters without change; for example, spaces, punctuations, 
    and numbers should not be encrypted or decrypted. Additionally, the case of the letters should be preserved, 
    small letters are transformed to other small letters and capital letters are transformed to capital letters.
    Use the function `shift` (provided later) to shift each character in message by the number in key.   
    args:
        message: string to be encrypted or decrypted
        key: number of places to shift the characters (always positive)
        decrypt: Boolean; when False the message is encrypted,  when True the message is decrypted        
    returns:
        transformed_message: encrypted (or decrypted) message        
    examples:
        Encryption
        ==  transform("deal", 1, False) returns:
            "efbm"        
        ==  transform("deal", 2, False) returns:
            "fgcn"        
        ==  transform("deal", 30, False) is equivalent to transform(message, 4, False)
            "hiep"        
        Decryption
        ==  transform("efbm", 1, True) returns:
            "deal"
            
        ==  transform("fgcn", 2, True) returns:
            "deal"
            
        ==  transform("hiep", 30, True) returns:
            "deal"            
    """
    if decrypt:
        split_message = message.split(" ")   
        decrypted = ""
        for a in split_message:
            for b in a:
                if b == "\n":
                    decrypted += "\n"
                elif b == ".":
                    decrypted += "."
                elif b == "!":
                    decrypted += "!"
                elif b == "-":
                    decrypted += "-"
                elif b == "=":
                    decrypted += "="
                else:
                    c = shift(b,key)
                    decrypted += c
            decrypted += " "
        return decrypted
    else:
        split_message = message.split(" ")
        crypted = ""
        for a in split_message:
            for b in a:
                if b == "\n":
                    crypted += "\n"
                elif b == ".":
                    crypted += "."
                elif b == "-":
                    crypted += "-"
                else:
                    c = shift(b,key)
                    crypted += c
            crypted += " "
        return crypted 
def shift(char, key):    
    """
    Shift char by the value in key while maintaining the case (small/capital).    
    If char contains non-letters (i.e. digits, punctuations, and white spaces), it is ignored.   
    args:
        char: character to shift
        key: number of places to shift char        
    returns:
        shifted character       
    examples:
        shift('a', 1) ==> 'b'
        shift('z', -1) ==> 'y'
        shift('A', 5) ==> 'F'
        shift('H', 7) ==> 'O'
        shift('o', -10) ==> 'e'
        shift('a', 30) ==> 'e'
    """    
    # ordered lower case alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"    
    # will contain shifted lower case alphabet
    shifted_alphabet = ''
    for i in range(len(alphabet)):
        shifted_alphabet = shifted_alphabet + alphabet[(i + int(key)) % 26]
    if char.isalpha():
        char_index = alphabet.index(char.lower())
        shifted_char = shifted_alphabet[char_index]   
        # keep char's case (upper or lower)
        if char.isupper():
            return shifted_char.upper()
        else:
            return shifted_char
def main():
    # parse command line arguments
    args = parse_command_line()
    # read content of infile to a string
    instring = read_file(args.infile)    
    # verbose
    if args.verbose:
        print("Input file:")
        print("------------")
        print(instring)
        print()   
    # key is specified
    if not args.all:
        # encrypt/decrypt content of infile
        outstring = transform(instring, args.key, args.decrypt)
        # verbose
        if args.verbose:
            print("Output file:")
            print("------------")
            print(outstring)
        # write content of outstring to outfile
        write_file(outstring, args.outfile)
    # key is not specified, try all keys from 1 to 25 to decrypt infile
    else:
        for k in range(1, 26):
            # decrypt content of infile
            outstring = transform(instring, k, True)
            # verbose
            if args.verbose:
                print("Key =", k)
                print("------------")
                print(outstring)
                print()
            # write content of outstring to outfile
            write_file(outstring, "decrypted_by_" + str(k) + ".txt")  
if __name__ == '__main__':
    main()
    
%%bash
pydoc cipher
