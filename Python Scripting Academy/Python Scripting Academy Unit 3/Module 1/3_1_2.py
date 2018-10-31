from datetime import time
# [x] Create a `time` variable containing the time: 8:45 AM
t = time(hour = 8, minute = 45)
print (t)

# [x] Create a `time` variable containing the time: 8:45:01:000150 PM
from datetime import time
t = time(hour = 20, minute = 45, second = 1, microsecond = 150)
print(t)

# [x] Print the hour (only) contained in t3
from datetime import time
t3 = time(hour = 15, minute = 10, second = 0)
print(t3.hour)

# [x] Modify t3 to: 4:10 PM
from datetime import time
t3 = time(hour = 15, minute = 10, second =0)
t = t3.replace(hour = 16)
print(t)

# [x] Create a `date` variable containing: (March 28 2012)
from datetime import date
d = date(year=2012,month=3,day=28)
print(d)

# [x] Prompt the user to enter a month and a day, get the current year, then create a date object with the information collected
from datetime import date
month1=int(input("Enter a month : "))
day1=int(input("Enter a day : "))
date1=date.today()
date2=date(date1.year,month1,day1)
print(date2)

# [x] Create a `datetime` variable containing: (March 28 2012 @ 12:55:10:30 AM)
from datetime import datetime
dt = datetime(year=2012,month=3,day=28,hour=0,minute=55,second=10)
print(dt)

# [x] Write code that prints the current hour
from datetime import datetime
t = datetime.today()
print(t.hour)

# [x] Write a program that prints the current date on one line and the current time on another line
from datetime import datetime, date, time
t=datetime.today()
print("Current date is : "+str(t.year)+"-"+str(t.month)+"-"+str(t.day))
print("Current time is : "+str(t.hour)+":"+str(t.minute)+":"+str(t.second))

# [x] Write a program that:
# 1) prompts the user for a time (hours and minutes only)
# 2) gets the current date
# 3) combines the collected information into a `datetime` variable
from datetime import date
h = int(input("Enter a time (hours) : "))
m = int(input("Enter a time (minutes) : "))
t=date.today()
print(str(t.year)+"-"+str(t.month)+"-"+str(t.day),str(h)+":"+str(m))

# [x] Write a program that displays the time: (17:39:10) as:
# 1) 05:39:10 PM
# 2) 17:39:10
from datetime import time
t = time(hour = 17, minute = 39, second = 10)
ft = t.strftime("%I:%M:%S %p")
ft2 = t.strftime("%H:%M:%S")
print(ft)
print(ft2)

# [x] Write a program that displays the date: (October 23rd 2018) as:
# 1) Oct 23, 2018
# 2) 10/23/18
# 3) 23/October/2018
# 4) Tuesday October 23
from datetime import date
d = date(year = 2018, month = 10, day =23)
fd = d.strftime("%b %d, %Y")
fd2 = d.strftime("%m/%d/%y")
fd3 = d.strftime("%d/%B/%y")
fd4 = d.strftime("%A %B %d")
print(fd)
print(fd2)
print(fd3)
print(fd4)

# [x] Complete the function `weekday` to return the weekday name of `some_date`
# Use the function to find the weekday on which you were born
from datetime import date
def weekday(some_date):
    return "You were born on a "+some_date.strftime("%A")
# Modify to your birthdate
bd = date(day = 8, month = 3, year = 1974)
# Display the day on which you were born
day = weekday(bd)
print(day)