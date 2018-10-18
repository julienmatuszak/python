# create and call make_doctor() with full_name argument from user input - then print the return value
def make_doctor(name):
    print("Doctor", name)
    
full_name = input("What is your full name ? : ")

make_doctor(full_name)

# [x] add a 3rd period parameter to make_schedule
def make_schedule(period1, period2, period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title())
    return schedule

student_schedule = make_schedule("mathematics", "history", "sport")
print("SCHEDULE:", student_schedule)

# [x] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)
#this will be easier after we see the tables and the loops:
#Here we can put only one variable inside the function)
def print_schedule(period1, period2, period3, period4, period5, period6):
    print("SCHEDULE:", ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title() 
                        + ", [4th] " + period4.title()  + ", [5th] " + period5.title() + ", [6th] " + period6.title())
    )

#And here a loop to define the different variables of the table
period1 = input("What's your subject nr. 1? : ")
period2 = input("What's your subject nr. 2? : ")
period3 = input("What's your subject nr. 3? : ")
period4 = input("What's your subject nr. 4? : ")
period5 = input("What's your subject nr. 5? : ")
period6 = input("What's your subject nr. 6? : ")

print_schedule(period1, period2, period3, period4, period5, period6)
