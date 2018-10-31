# [x] Use relational and/or arithmetic operators with the variables x and y to write:
# 3 expressions that evaluate to True (i.e. x >= y)
# 3 expressions that evaluate to False (i.e. x <= y)
x = 84
y = 17
print(not x<=y)
print(x>=y or x<=y)
print(x>=y and not x<=y)
print(x>=y and x<=y)
print(not x>=y)
print(x<=y and not x>=y)

# [x] Use the basic Boolean operators with the variables x and y to write:
# 3 expressions that evaluate to True (i.e. not y)
# 3 expressions that evaluate to False (i.e. x and y)
x = True
y = False
print(not y)
print(y or x)
print(x and not y)
print(y and not x)
print(not x)
print(x and y)

# [x] Write an expression to test if x is an even number outside the range [-100, 100]
# Test your expression with:
#x = 104 #(True)
#x = 115 #(False)
#x = -106 #(True)
#x = -99 #(False)
(x%2 == 0) and (x>100 or x<-100)

# [x] Write an expression to test if a string s starts and ends with a capital letter
# HINT: You might find the function `str.isupper()` useful
# Test your expression with
s = "CapitaL" #(True)
#s = "Not Capital" #(False)
s[0].isupper() and s[-1].isupper()

# [x] Write an expression to test if a string s contains a numerical value
# then test if the value is greater than the value stored in x
# HINT: Use the functions `s.isnumeric()` and `float(s)`
# Test your expression with
#s = "39"
#x = 24
# Expression should yield True
#s = "a39"
#x = 24
# Expression should yield False
if s.isnumeric():
    print(float(s) > 24)
else:
   print(s.isnumeric())
# [x] Write an expression equivalent to the one below 
# to test if x is outside the range [10, 20] (seen in a previous example)
# (x < 10) or (x > 20)
# Test your expression with 
#x = 11 #(False)
#x = 50 #(True)
not(x>10 and x<20)

# [x] Write a second expression to test if x is an even number outside the range [-100, 100]
# Do NOT use the expression you wrote for a previous exercise
# Test your expression with:
#x = 104 #(True)
#x = 115 #(False)
#x = -106 #(True)
#x = -99 #(False)
not ((x%2 != 0) and (x<100 or x>-100))
# [x] Write a program to validate that user input is outside of the range [0, 100]
x = int(input("Enter an integer : "))
if x < 0 and x >100:
    print("You are outside of the range [0, 100]")
else:
    print("You are within range of [0,100]")

# [x] Write a program to ask a user for her/his BMI index, then display the user's BMI category
bmi = round(float(input("Enter your BMI : ")),1)
if bmi < 18.5:
    print("You are underweight!")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You have a normal weight!")
elif bmi >=25 and bmi <= 29.9:
    print("You are overweight!")
elif bmi >= 30:
    print("You are obese!")
else:
    print("Sorry, I didn't understand your . Please retry!")
