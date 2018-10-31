# [x] Create a `timedelta` object that contains: 2 hours, 3 minutes, and 1 week
from datetime import timedelta
date1 = timedelta(hours = 2, minutes = 3, weeks = 1)

# [x] Use a `timedelta` object to calculate the total number of seconds in: 1 hour and 15 minutes
from datetime import timedelta
date1 = timedelta(hours=1,minutes=15)
print("Total number of seconds : ",date1.seconds)

# Use a `timedelta` object to find out how many days are left until your upcoming birthday
from datetime import datetime, timedelta
date1 = datetime.today()
date2 = datetime(year = 2019, month = 5, day = 15)
delta = date2 - date1
print("There are",delta.days,"days left until your birthday.")

# [x] Write a program to compute the date 3 weeks before your birthday 
# to help you remember when to send the invitations
from datetime import datetime, timedelta
bday = datetime(year=2019,month=5,day=15)
bbday = bday - timedelta(days=21)
print("On",bbday.strftime("%b/%d/%Y"),"remember to send the invitations!")

# [x] Write a program that computes the number of days from the current date till the 3 weeks reminder
# 1) Create a `timedelta` object (td1) for the period between the current date and your upcoming birthday
# 2) Create a `timedelta` object (td2) containing 3 weeks
# 3) Use the `timedelta` objects (td) from 1 and 2 to compute the required number of days
from datetime import datetime, timedelta
today = datetime.today()
bday = datetime(year=2019,month=5,day=15)
td1 = bday - today
td2 = timedelta(days=21)
print("Number of days from the current date till the 3 weeks reminder : ",(td1-td2).days)

# [x] Write a program to find out if 4th of July of this year has passed or not
from datetime import datetime, timedelta
national_day = datetime(year=2018,month=7,day=14)
if datetime.today() > national_day:
    print("The National Day of",national_day.year,"has already passed!")
elif datetime.today() < national_day: 
    print("The National Day of",national_day.year,"is yet to come!")
else:
    print("The National Day is today!")

# [x] Complete the following program to find out if you are closer to the current year's June or December solstice
from datetime import datetime, timedelta
import math

# Define today's date
now = datetime.today()

# Define the December solstice
december_solstice = datetime(month = 12, day = 21, year = now.year)

# Define the June solstice
june_solstice = datetime(month = 6, day = 21, year = now.year)

# Find out which solstice is closer
if abs((now-december_solstice).days) > abs((now-june_solstice).days):
    print("Today is closer to the december solstice than to the summer solstice.")
elif abs((now-december_solstice).days) < abs((now-june_solstice).days):
    print("Today is closer to the december solstice than to the summer solstice.")
else:
    print("There are as many days from today to the winter solstice than to the summer solstice!")
