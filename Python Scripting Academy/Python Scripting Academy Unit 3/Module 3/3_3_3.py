# [x] Create a tuple that consists of the following variables
x = 5
l = [4.4, 5.3]
s = "something"
t = (9, 0)
T = (5,[4.4,5.3],"something",(9,0))

# [x] Change the third element of T to [59, 20.4]
T = ([43.6, 34], [49, 59], [50, 34.6], [39, 49])
print(T)
T[2][0] = 59
T[2][1] = 20.4
print(T)

# [x] Write a program to merge the content of T1 and T2 into one tuple T
# Correct output should be T = (5, 4, 3, 9, 2, 12)
# T = ((5, 4, 3), (9, 2, 12)) is an incorrect output
# Hint: Use list to/from tuple conversion
T1 = (5, 4, 3)
T2 = (9, 2, 12)
T=(T1,T2)
print(T)

# [x] Write a program to split the content of T into T1 and T2
# T1 = (5, 4, 3)
# T2 = (9, 2, 12)
# Split a full name into the first and last names
def split_tuple(t):
    t1 = (t[0],t[1],t[2])
    t2 = (t[3],t[4],t[5])
    # pack the variables into a tuple, then return the tuple
    return ("T1 = "+str(t1)+"\n"+"T2 = "+str(t2))
# Unpacked variables can be used separately
#print("First name: {:s}".format(first))
#print("Last name: {:s}".format(last))
T = (5, 4, 3, 9, 2, 12)
print(split_tuple(T))

# [x] Complete the function `current_date` to return today's month, day, and year
# Hint: Use an appropriate function from the datetime module
from datetime import datetime
def current_date():
    t = datetime.today()
    m = t.month
    d = t.day
    y = t.year
    return(m, d, y)   
m, d, y = current_date()
print("Today's date is: {:2d}/{:2d}/{:4d}".format(m, d, y))

# [x] Write a program to merge the content of T1 and T2 into one tuple T
# Correct output should be T = (5, 4, 3, 9, 2, 12), 
# T = ((5, 4, 3), (9, 2, 12)) is an incorrect output
# You should NOT use lists in your solution
T1 = (5, 4, 3)
T2 = (9, 2, 12)
T = T1 + T2
print(T)

# [x] Write a program to prompt the user for a number, then test if the number is contained in T
T = (23, 45, 93, 59, 35, 58, 19, 3)
num = int(input("Guess the number : "))
for a in range(len(T)):
    if num == T[a]:
        print("You guessed the number !")
        break

# Write a function to return the largest element in a tuple T
T = (70, 45, 93, 59, 35, 58, 19, 3)
m = 0
for a in T:
    for b in range(len(T)):
        if T[b] > m:
            m = a
print(m)

# [x] Write a program to compute the average of the elements in T
T = (23, 45, 93, 59, 35, 58, 19, 3)
b = 0
for a in range(len(T)):
    b += T[a]
print("The average of the elements in T is",str(round(float(b/len(T)),2)))
