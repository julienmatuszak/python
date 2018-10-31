# [x] Use the math module to display an accurate value for pi
import math
print(math.pi)

# [x] Write a program to:
# 1) find all the numbers in a list that are divisible by 3
# 2) display the square root of these numbers
# 3) use a rounding function to display the square roots while ignoring the decimal fraction
import math
lst = [23, 45, 65, 2345, 42, 76, 37, 87, 647, 35, 37 ,39, 898, 92, 18]
divisible_by_3 = []
sqr_list = []
neat_sqr_list = []
for a in lst:
    if a%3 == 0:
        divisible_by_3.append(a)
    sqr_list.append(math.sqrt(a))
    neat_sqr_list.append(round(math.sqrt(a),0))
print("The list of numbers divisible by 3 is :",divisible_by_3)
print("The list of square roots of these numbers (in the same order) is:",sqr_list)
print("A more brushed-up list of these square roots",neat_sqr_list)

# [x] Complete the function `quarters_count` so it calculates and prints the number of quarters in `input_cents`
# The function input `input_cents` should be in cents 
# The function should print the number of calculated quarters in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 25, why?) -> because if it's more, we can divide by a divisor with one more increment
# HINT: You might want to use % and // operators
import math
def quarters_count(input_cents):
    print("There are",str(int(math.floor(input_cents/25))),"quarters in total", end = " ")
    return "and there are "+str(int(input_cents%25))+" remaining cents."
              
# test with $2
# Output should be: 8 quarter\s
dollars = 2
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)
print(remaining_cents)

# test with $5.30
# Output should be: 21.0 quarter\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)
print(remaining_cents)
# test with $9.49
# Output should be: 37.0 quarter\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)
print(remaining_cents)

# [x] Complete the function `dimes_count` so it calculates and prints the number of dimes in `input_cents`
# The function input `input_cents` should be in cents 
# The function should print the number of calculated dimes in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 10, why?)
# HINT: You might want to use % and // operators

def dimes_count(input_cents):
    print("There are",str(int(math.floor(input_cents/10))),"dimes in total", end = " ")
    return "and there are "+str(int(input_cents%10))+" remaining cents."
         
# test with $2
# Output should be: 20 dime\s
dollars = 2
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)
print(remaining_cents)
# test with $5.30
# Output should be: 53.0 dime\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)
print(remaining_cents)
# test with $9.49
# Output should be: 94.0 dime\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)
print(remaining_cents)

# [x] Complete the function `nickels_count` so it calculates and prints the number of nickels in `input_cents`
# The function input `input_cents` should be in cents 
# The function should print the number of calculated nickels in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 5, why?)
# HINT: You might want to use % and // operators
def nickels_count(input_cents):
    print("There are",str(int(math.floor(input_cents/5))),"nickels in total", end = " ")
    return "and there are "+str(int(input_cents%5))+" remaining cents."       
# test with $2
# Output should be: 40 nickel\s
dollars = 2
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)
print(remaining_cents)
# test with $5.30
# Output should be: 106.0 nickel\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)
print(remaining_cents)
# test with $9.49
# Output should be: 189.0 nickel\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)
print(remaining_cents)

# [x] Complete the function `coins_due` to calculate and print the change due to a customer in coins
#
# The function `coins_due` has 2 inputs:
#      - `amount_paid`: Amount paid by a customer (in cents)
#      - `item_price`: Purchase price of an item
#
# The function should print:
#      - The number of quarters due
#      - The number of dimes due
#      - The number of nickels due
#      - The number of cents due
#      
# The function does not need to return anything
#
# HINT: Use the functions you developed before `quarters_count`, `dimes_count`, `nickels_count`
import math
def quarters_count(input_cents):
    return(float(math.floor((input_cents)/25)))
def dimes_count(input_cents):
    return(float(math.floor((input_cents)/10)))
def nickels_count(input_cents):
    return(float(math.floor((input_cents)/5))) 
def coins_due(amount_paid, item_price):
    q = quarters_count(amount_paid - item_price)
    d = dimes_count(q%25)
    n = nickels_count(d%10)
    c = amount_paid - item_price - 25*q - 10*d - 5*n
    print("Change due:\n"+str(q)+" quarter\s\n"+str(d)+" dime\s\n"+str(n)+" nickel\s\n"+str(c)+" cent\s")
# Test case:
# amount paid = $10, item price = $5.37
# Output should be: 
#    Change due:
#    18.0 quarter\s
#    1.0 dime\s
#    0.0 nickel\s
#    3.0 cent\s
amount_paid = 10 * 100 # in cents
item_price = 5.37 * 100 # in cents
coins_due(amount_paid, item_price)

# [x] Complete the following program to display the probability of a certain die roll
from random import randint
def die_roller ():
    return(randint(1, 6))
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
x = randint(10000,20000)
print("We are doing",x,"throws")
for a in range(0,x):
    a = die_roller()
    if a == 1:
        p1 +=1/x
    elif a == 2:
        p2 +=1/x
    elif a == 3:
        p3 +=1/x
    elif a == 4:
        p4 +=1/x
    elif a == 5:
        p5 +=1/x
    else:
        p6 +=1/x
print("Probability to obtain 1 :",str(round(float(p1),3)*100)+"%")
print("Probability to obtain 2 :",str(round(float(p2),3)*100)+"%")
print("Probability to obtain 3 :",str(round(float(p3),3)*100)+"%")
print("Probability to obtain 4 :",str(round(float(p4),3)*100)+"%")
print("Probability to obtain 5 :",str(round(float(p5),3)*100)+"%")
print("Probability to obtain 6 :",str(round(float(p6),3)*100)+"%")

# [x] Complete the following program so you can count the number of times needed to get a roll sum of 11
from random import randint
def die_roller():
    return(randint(1, 6))
def roll_sum():
    return die_roller() + die_roller()
count = 0
while roll_sum() != 11:
    count+=1
    roll_sum()
print("The number of times needed to get a roll sum of 11 for this game is "+str(count))

# [x] Complete the function `pick_candy` so it returns a candy from box at random
from random import choice
def pick_candy():
    box = ["Taffy", "Brownie", "Cookie", "Candy bar", "Chocolate", "Lollipop", "Gingerbread", "Marshmallow"]
    return(choice(box))
print(pick_candy())

# [x] Write a program to shuffle the following sorted list
from random import shuffle
lst = [3, 5, 9, 29, 35, 59, 62, 69, 102, 394, 594, 1993]
shuffle(lst)
print(lst)

# [x] Write a program that displays the current time as (HH:MM AM/PM) (example 02:28 PM)
from datetime import datetime
def show_time():
    return(datetime.today().strftime("%I:%M %p"))
print(show_time())

# [x] Write a program that displays the current time as (HH:MM:SS) (example 14:28:10)
from datetime import time
def show_time():
    return(datetime.today().strftime("%H:%M:%S"))
print(show_time())

# [x] Complete the functions `american_format(d)` and `european_format(d)` to display the datetime object d in the proper format

from datetime import datetime
def american_format(d):
    return d.strftime("%m/%d/%y")
def european_format(d):
    return d.strftime("%d/%m/%y")
# test
d = datetime(month = 2, year = 2012, day = 13)
print("American format:", american_format(d))
print("European format:", european_format(d))

# [x] Write a program to display a list of all your birthdays from the day you were born till 2025.
# You should also show the weekdays so you can see which of them was (or will be) on a weekend
from datetime import datetime
t = datetime(year=1979,month=5,day=15)
for a in range(1979,2026):
    if a < datetime.today().year:
        print("Your birthday on",str(a),"was a",datetime(year=a,month=5,day=15).strftime("%A"))
    elif a > datetime.today().year:
        print("Your birthday on",str(a),"will be a",datetime(year=a,month=5,day=15).strftime("%A"))     
    else:
        print("Your birthday on",str(a),"is a",datetime(year=a,month=5,day=15).strftime("%A"))  

# Write a program to find out how many minutes are in a 4-week period
# Hint: Use a timedelta object and the total_seconds() method
from datetime import timedelta
t = timedelta(weeks=4)
print(t)
print(int(t.total_seconds()))

# [x] Write a program to compute the number of days remaining in the current year
from datetime import timedelta
t=datetime(year=2018,month=12,day=31)
print("There is",str((t-datetime.today()).days),"days left until the end of the year!")

# [x] Complete the program below to find out if July 4th is within 10 days of today's date,
# if it is, find out if has passed or not

from datetime import datetime
import math

# get today's date
todays_date = datetime.today()

# 4th of July of current year
july_4th = datetime(month = 7, day = 4, year = todays_date.year)
days_difference = todays_date - july_4th
if abs(days_difference.days) > 10:
    print("July 4th is not within 10 days of today's date.")
else:
    if days_difference.days < 0:
        print("July the 4th is gone, don't worry, there will be one more next year!")
    elif days_difference.days > 0:
        print("July the 4th is within 10 days, get ready!")
    else:
        print("July the 4th is today, rejoice!")

# [x ] Complete the following program to:
# 1) navigate to `parent_dir` directory (if not already in it)
# 2) create a new directory called `practice_1`
# 3) change the working directory to `practice_1`
# 4) display the current working directory to verify you are in the correct location
# 5) create a new directory called `practice_2`
# 6) verify that `practice_2` was created by listing the content of the current directory
# 7) rename `practice_2` as `sub_practice_2`
# 8) verify the name was successful changed by listing the content of the current directory
# 9) remove `sub_practice_2`
# 10) change working directory to the parent directory using `..`
# 11) remove `practice_1`
# 12) verify your current working directory and display its content
import os, os.path
# 1) navigate to `parent_dir` directory (if not already in it)
if('/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1' not in os.getcwd()):
    # Changing the current working directory to parent dir
    print("Changing working dir to parent_dir")
    os.chdir('/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1')
    print("Current working directory:", os.getcwd())
# 2) create a new directory called `practice_1`
os.mkdir("practice_1")
# 3) change the working directory to `practice_1`
os.chdir("practice_1")
# 4) display the current working directory to verify you are in the correct location
os.getcwd()
# 5) create a new directory called `practice_2`
os.mkdir("practice_2")
# 6) verify that `practice_2` was created by listing the content of the current directory
print(os.listdir())
# 7) rename `practice_2` as `sub_practice_2`
os.rename("practice_2","sub_practice_2")
# 8) verify the name was successful changed by listing the content of the current directory
print(os.listdir())
# 9) remove `sub_practice_2`
os.rmdir("sub_practice_2")
# 10) change working directory to the parent directory using `..`
os.chdir("..")
# 11) remove `practice_1`
os.rmdir("practice_1")
# 12) verify your current working directory and display its content
print(os.listdir())

# [x] Write a program that prompts the user for a file or directory name
# if it exists in the current working directory, it prints whether it is a file or directory
import os, os.path
print(os.getcwd())
file_or_dir = input("Which file or directory are you looking for ? ")
if os.path.isfile(file_or_dir):
    print("There is something and it is a file !")
elif os.path.isdir(file_or_dir):
    print("There is something and it is a directory !")
else:
    print("There is nothing !")

# [x] The following program is designed to generate a number of directories.
# The directory names follow the pattern (MM_DD_YY_randnum), where:
#     - MM_DD_YY: is today's date as month/day/year
#     - randnum: is a random integer between 10000 and 50000
# For example, if today is May 12th, 2016, then the following would be valid names: 05_12_16_11050 or 05_12_16_15001
#
# For this task, you should complete the functions:
# 1) `directory_count()`
# 2) `name_generator()`
# 3) `directory_creator(name)`
# 4) `create()`
#
# HINT: You should import all necessary modules
import os
from random import randint
import math
from datetime import datetime
def directory_count():
    """
    Calculate the number of directories to be generated.   
    I) Get the current minute using appropriate functionality from `datetime`
    II) Take the square root of ..the current minute + 15
    III) Round the square root to an integer
    VI) return the rounded number as the number of directories to be created   
    args: 
          NONE   
    returns: 
         `dir_count`: number of directories to be created 
    """
    current_minute = 0
    dir_count = 0
    current_minute = datetime.today().minute
    dir_count = int(math.sqrt(current_minute+15))
    return(dir_count)
def name_generator():
    """
    Generate a single directory name using the pattern (MM_DD_YY_randnum).   
    args:
         NONE    
    returns:
         `dir_name`: string containing a valid directory name
    """
    dir_name = ""
    randnum = 0
    randnum = randint(10000,50000)
    dir_name = datetime.today().strftime("%m_%d_%Y_")+str(randnum)
    return(dir_name)
def directory_creator(name):
    """
    Create a single directory called `name` in the current working directory.   
    args:
         name: directory to be created   
    returns:
         NONE
    """
    os.mkdir(name)
def create():
    """
    Generate the necessary directories.    
    Use `directory_count` to calculate the number of directories, then use `directory_creator` and `name_generator`.
    args:
         NONE    
    returns:
         NONE
    """
    for a in range(0,directory_count()):
        directory_creator(name_generator())        
# Change working directory to `parent_dir` or `create`
if("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/parent_dir" not in os.getcwd()):
    if os.path.exists("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/parent_dir"):
        print("Changing working dir to /Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/parent_dir")
        os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/parent_dir")
    else:
        os.mkdir(os.getcwd() + "/parent_dir")
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
else:
    # so the code can run multiple times 
    # while directory not ending with 'parent_dir' move up the path ..\
    while "parent_dir" not in os.getcwd()[-11:]:
        # move up in dir to find 'parent_dir'
        os.chdir("..")
        print("moved up", os.getcwd())       
# print the current working directory (should be "parent_dir")
print("The current working directory is:", os.getcwd())
# check for randoms_directory if not present, create new
if os.path.exists(os.getcwd() + "/randoms_directory") != True:
    os.mkdir("randoms_directory")
# change the current working directory to randoms_directory
print("Changing working dir to randoms_directory")
os.chdir("randoms_directory")
# print the current working directory (should be "randoms_dir")
print("The current working directory is:", os.getcwd())
# create directories inside "randoms_directory"
create()   
# list the content of the current directory
print("Current directory content:", os.listdir())
