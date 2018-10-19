# [x] code and test SHIRT SALE
guess = input("What is your shirt size (S, M, L): ")

if guess.isalpha() == False:
    print("Invalid: guess should only use characters")
elif guess == "S":
    print("Small = $6")
elif guess == "M":
    print("Medium = $7")
elif guess == "L":
    print("Large = $8")
else:
    print(guess, "is not available")

str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [x] Add the 3 numbers as integers and print the result
print(int(str_num_1)+int(str_num_2)+int_num_3)

str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [x] Add the 3 numbers as test strings and print the result
print(int(str_num_1)+int(str_num_2)+int_num_3)

# [x] code and test: adding using int casting
str_integer = "2"
int_number = 10
number_total = int(str_integer) + int_number
print(number_total)

# [x] code and test the adding calculator
num1 = input("Gimme your first integer : ")
if num1.isdigit() == False:
    print("Sorry, you didn't give me an integer")
else:
    num2 = input("Gimme your first integer : ")
    if num2.isdigit() == False:
        print("Sorry, you didn't give me an integer")
    else:
        print(num1,"+",num2,"=",int(num1)+int(num2))
