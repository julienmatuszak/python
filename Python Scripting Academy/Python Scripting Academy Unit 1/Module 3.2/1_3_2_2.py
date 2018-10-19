# [x] print the result of subtracting 15 from 43
print("43 - 15 =",43-15)

# [x] print the result of multiplying 15 and 43
print("15 * 43 =",15*43)

# [x] print the result of dividing 156 by 12
print("156 / 12 = ", 156/12)

# [x] print the result of dividing 21 by 0.5
print("21 / 0.5 =",21/0.5)

# [x] print the result of adding 111 plus 84 and then subtracting 45
print("111 + 84 - 45 =", 111+84-45)

# [x] print the result of adding 21 and 4 and then multiplying that sum by 4
print("(21 + 4) / 5 = ",(21+4)/5)

# [x] create and test multiply() function
def multiply():
        num1 = int(input("gimme a number : "))
        num2 = int(input("gimme another number : "))
        return str(num1)+" * "+str(num2)+" = "+str(num1*num2)

print(multiply())

# [x] create improved multiply() function and test with /, no argument, and an invalid operator ($)
# [x] create and test multiply() function
def multiply(operator):
    if operator == "*":
        num1 = int(input("gimme a number : "))
        num2 = int(input("gimme another number : "))
        return str(num1)+" * "+str(num2)+" = "+str(num1*num2)
    elif operator == "/":
        num1 = int(input("gimme a number : "))
        num2 = int(input("gimme another number : "))
        return str(num1)+" / "+str(num2)+" = "+str(num1/num2)
    else:
        print("Invalid Operator")

operator = input("Do you want to multiply or divide (choose * or /) : ")
print(multiply(operator))

# Review, run, fix 
student_name = input("enter name: ").capitalize()
if student_name.startswith("F"):
    print(student_name,"Congratulations, names starting with 'F' get to go first today!")
elif student_name.startswith("G"):
    print(student_name,"Congratulations, names starting with 'G' get to go second today!")
else:
    print(student_name, "please wait for students with names starting with 'F' and 'G' to go first today.")
