# [x] complete rainbow colors
color = input("choose one of the colors of the rainbow (ROYGBIV) : ")
if color.upper() == "R":
    print(color+" = "+"Red")
elif color.upper() == "O":
    print(color+" = "+"Orange")
elif color.upper() == "Y":
    print(color+" = "+"Yellow")
elif color.upper() == "G":
    print(color+" = "+"Green")
elif color.upper() == "B":
    print(color+" = "+"Blue")
elif color.upper() == "I":
    print(color+" = "+"Indigo")
elif color.upper() == "V":
    print(color+" = "+"Violet")
else:
    print("no match")

# [x] make the code above into a function rainbow_color() that has a string parameter, 
# get input and call the function and return the matching color as a string or "no match" message.
# Call the function and print the return string.
def rainbow_color(color):
    if color.upper() == "R":
        return(color+" = "+"Red")
    elif color.upper() == "O":
        return(color+" = "+"Orange")
    elif color.upper() == "Y":
        return(color+" = "+"Yellow")
    elif color.upper() == "G":
        return(color+" = "+"Green")
    elif color.upper() == "B":
        return(color+" = "+"Blue")
    elif color.upper() == "I":
        return(color+" = "+"Indigo")
    elif color.upper() == "V":
        return(color+" = "+"Violet")
    else:
        return("no match")

color = input("choose one of the colors of the rainbow (ROYGBIV) : ")
print(rainbow_color(color))
    
# [x] complete age_20()
def age_20(real_age):
    if str(real_age).isdigit() is False:
        print("You didn't put a digit!")
    elif int(real_age)<20:
        print("You are less than 20, I cannot tell you how old you were 20 years ago!")
    else:
        return(str(int(real_age)-20)+" years old, 20 years difference from now")
    
real_age = input("What is your real age ? : ")
print(age_20(real_age))

# [x]  create rainbow_or_age()
def rainbow_or_age(roa):
    if roa.isalpha() is True:
        if roa.upper() == "R":
            return(roa+" = "+"Red")
        elif roa.upper() == "O":
            return(roa+" = "+"Orange")
        elif roa.upper() == "Y":
            return(roa+" = "+"Yellow")
        elif roa.upper() == "G":
            return(roa+" = "+"Green")
        elif roa.upper() == "B":
            return(roa+" = "+"Blue")
        elif roa.upper() == "I":
            return(roa+" = "+"Indigo")
        elif roa.upper() == "V":
            return(roa+" = "+"Violet")
        else:
            print("no match")
    elif roa.isdigit()is True:
        if str(roa).isdigit() is False:
            print("You didn't put a digit!")
        elif int(roa)<20:
            print("You are less than 20, I cannot tell you how old you were 20 years ago!")
        else:
            return(str(int(roa)-20)+" years old, 20 years difference from now")
    else:
        return("FALSE")
    
roa = input("Rainbow (ROYGBIV) or age (integer) ? : ")
print(rainbow_or_age(roa))

# [x]  add 2 numbers from input using a cast to integer and display the answer 
def add():
    num1 = int(input("gimme a number : "))
    num2 = int(input("gimme another number : "))
    return str(num1)+" + "+str(num2)+" = "+str(num1+num2)

print(add())

# [x] Multiply 2 numbers from input using cast and save the answer as part of a string "the answer is..."
# display the string using print
def multiply():
    num1 = int(input("gimme a number : "))
    num2 = int(input("gimme another number : "))
    return "the answer is : "+str(num1)+" * "+str(num2)+" = "+str(num1*num2)

print(multiply())

# [x] get input of 2 numbers and display the average: (num1 + num2) divided by 2
def avg():
    num1 = int(input("gimme a number : "))
    num2 = int(input("gimme another number : "))
    return "("+str(num1)+" + "+str(num2)+")/2 = "+str(float((num1+num2)/2))

print(avg())

# [x] get input of 2 numbers and subtract the largest from the smallest (use an if statement to see which is larger)
# show the answer
def substract_anything():
    num1 = float(input("gimme a number : "))
    num2 = float(input("gimme another number : "))
    if num1>num2:
        return str(num1)+" - "+str(num2)+" = "+str(num1-num2)
    else:
        return str(num2)+" - "+str(num1)+" = "+str(num2-num1)
        
print(substract_anything())

# [x] Divide a larger number by a smaller number and print the integer part of the result
# don't divide by zero! if a zero is input make the result zero
# [x] cast the answer to an integer to cut off the decimals and print the result
def divide_anything():
    num1 = float(input("gimme a number : "))
    num2 = float(input("gimme another number : "))
    if num1 == 0:
        print("result is 0")
    elif num2 == 0:
        print("result is 0")
    else:
        if num1>num2:
            return str(num1)+" / "+str(num2)+" = "+str(int(num1/num2))
        else:
            return str(num2)+" / "+str(num1)+" = "+str(int(num2/num1))
        
print(divide_anything())
