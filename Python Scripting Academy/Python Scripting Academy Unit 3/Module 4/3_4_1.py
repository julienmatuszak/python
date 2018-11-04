%%writefile main_2.py
# [x] The following program asks the user for a circle radius then display the area and circumference
# Modify the program so it only displays the information when executed directly
# The program should not display anything if it is imported as a module 
from math import pi
def circle_area(r):
    return pi * (r ** 2)

def circle_circumference(r):
    return 2 * pi * r
radius = float(input("Enter radius: "))
print("Area =", circle_area(radius))
print("Circumference =", circle_circumference(radius))

%%writefile day_finder.py
# [x] Write a program that reads a date (month, day, year) as command-line arguments in order
# then prints the day of the week for that date.
# If an optional flag (-c or --complete) is specified, the program should print the full date (not only the day of the week).
# The help message should look like:
'''
usage: day_finder.py [-h] [-c] month day year
positional arguments:
  month           Month as a number (1, 12)
  day             Day as a number (1, 31) depending on the month
  year            Year as a 4 digits number (2018)
optional arguments:
  -h, --help      show this help message and exit
  -c, --complete  Show complete formatted date
'''
# HINT: Use a date object with strftime
import argparse
from datetime import datetime
# Define an argument parser object
parser = argparse.ArgumentParser()
# Add positional arguments
parser.add_argument('month', action = 'store', type = int, help = 'Month as a number (1, 12)')
parser.add_argument('day', action = 'store', type = int, help = 'Day as a number (1, 31) depending on the month')
parser.add_argument('year', action = 'store', type = int, help = 'Year as a 4 digit number (2018)')
# Add optional arguments
parser.add_argument('-c', '--complete', action = 'store_true', help = 'Show complete formatted date')
# Parse command-line arguments
args = parser.parse_args()
# Program
t = datetime(month = args.month, day = args.day, year = args.year)
print(t.strftime("%A"), end = " ")
# If args.complete is used, print the date with the complete format
if args.complete:
    print(t.strftime("%B, %d, %Y"))

%%bash
python3 day_finder.py 12 31 2017 -c -h

%%bash
python3 day_finder.py 12 31 2017

%%writefile sort_numbers.py
# [x] Write a program that reads an unspecified number of integers from the command line,
# then prints out the numbers in an ascending order
# The program should have an optional argument to save the sorted numbers as a file named `sorted_numbers.txt`
# The help message should look like:
'''
usage: sort_numbers.py [-h] [-s] [numbers [numbers ...]]
positional arguments:
  numbers     int to be sorted
optional arguments:
  -h, --help  show this help message and exit
  -s, --save  save the sorted numbers on a file (sorted_numbers.txt)
'''
#HINT: use nargs = '*' in an add_argument method
import argparse
# Define an argument parser object
parser = argparse.ArgumentParser()
# Add positional arguments
parser.add_argument('numbers', action = 'store', nargs = '*', type = int, help = 'int to be sorted')
# Add optional arguments
parser.add_argument('-s', '--save', action = 'store', help = 'save the sorted numbers on a file (sorted_numbers.txt)')
# Parse command-line arguments
args = parser.parse_args()
# Program
arranged = sorted(args.numbers)
print(*arranged)
if args.save:
    with open("sorted_numbers.txt", 'w+') as f:
        for a in arranged:
            f.write(str(a)+" ")
%%bash
python3 sort_numbers.py 23 49 5 300 43 582 58 29 62 69 320 60 -s SAVE -h

