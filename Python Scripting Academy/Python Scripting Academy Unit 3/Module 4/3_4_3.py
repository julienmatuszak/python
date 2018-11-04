# [x] The following function generates a single die roll
# Document the function using a one-line docstring
from random import randint
def die_roller ():
    """Returns a random number within the range from 1 to 6"""
    return (randint(1, 6))
print(die_roller.__doc__)
help(die_roller)

# [x] The following function computes the area of a circle
# Document the function using a one-line docstring
from math import pi
def circle_area(r):
    """Returns the area of a circle"""
    return pi * (r ** 2)
print(circle_area.__doc__)
help(circle_area)

# [x] The following program counts the number of times the value in `a` appears in `lst`
# Document the function using a multi-line docstring
def count_occurrences(a, lst): 
    """
    Counts the occurrences of an element in a list
    
    args:
        a: element to look for in the list
        list: the list itself
    
    returns:
        count: the number of occurrences
    """
    count = 0
    for element in lst:
        if a == element:
            count = count + 1  
    return count
print(count_occurrences.__doc__)
help(count_occurrences)

# [x] The following program prints out the date `d` number of days after today
# Document the function using a multi-line docstring
from datetime import date, timedelta
def future_date(d):
    """
    Gives the date a certain number of days from today   
    args:
        d: number of days from today (int)  
    returns:
        td: the future date
    """
    today = date.today()
    td = timedelta(days = d)
    future = today + td
    print("Date {:d} from today is: {:s}".format(d, future.strftime("%a %h %d, %Y")))   
# Date 10 days from today
future_date(10)
print(future_date.__doc__)
help(future_date)
