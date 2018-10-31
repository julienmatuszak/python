# [x] Write a program to prompt the user for an integer input between 0 and 100
# then print if the number is contained in `lst`
lst = [22, 89, 69, 78, 58, 22, 56, 13, 74, 8, 32, 58, 8, 63, 46, 79, 9, 38, 25, 96]
guess = int(input("Guess a number between 0 and 100 : "))
for a in range(len(lst)):
    if guess == lst[a]:
        print("Your number",guess,"is contained in the list !")
        break

# [x] The `records` list contains information about a company's employees
# each of the elements in `records` is a list containing the name and ID of an employee.
# Write a program to test if `applicant` is contained in `records` and display an appropriate message
# Records of names and IDs
records = [['Colette', 22347], ['Skye', 35803], ['Alton', 45825], ['Jin', 24213]]

applicant = ['Joana', 20294]

for a in range(len(records)):
    for b in records[a]:
        if applicant[0] == b:
            print(applicant[0],"is contained in records")
            break      

# [x] Write a program to prompt the user for a letter (capital or small) then print if the letter is a vowel
# HINT: Use a string containing all the vowels and the `in` or `not in` operator
vowels = ["a","e","i","o","u"]
letter = input("Enter a letter : ")
for vowel in vowels:
    if letter == vowel:
        print(letter,"is a vowel")

# [x] Write a program to:
# 1) Create a variable `e` that is equal but NOT identical to `s`
# 2) Test the equality and identity of `s` and `e` and print the results
# 3) Create a variable `i` that is equal and identical to `s`
# 4) Test the equality and identity of `s` and `i` and print the results
# 5) Test the equality and identity of `e` and `i` and print the results
s = "Whole Wheat Bread"
e = "Whole Wheat Bread"
i = s
print("s equal e ? ", s == e)
print("s is identical to e ?", s is e)
print("s is not identical to e ?", s is not e)
print("s equal i ? ", s == i)
print("s is identical to i ?", s is i)
print("s is not identical to i ?", s is not i)
print("e equal i ? ", e == i)
print("e is identical to i ?", e is i)
print("e is not identical to i ?", e is not i)

# [x] Write a program to:
# 1) Create a variable `e` that is equal but NOT identical to `x`
# 2) Test the equality and identity of `x` and `e` and print the results
# 3) Create a variable `i` that is equal and identical to `x`
# 4) Test the equality and identity of `x` and `i` and print the results
# 5) Test the equality and identity of `e` and `i` and print the results
x = [[-1, 2],[3, 4],[-5, 6]]
e = [[-1, 2],[3, 4],[-5, 6]]
i = x
print("x equal e ? ", x == e)
print("x is identical to e ?", x is e)
print("x is not identical to e ?", x is not e)
print("x equal i ? ", x == i)
print("x is identical to i ?", x is i)
print("x is not identical to i ?", x is not i)
print("i equal e ? ", i == e)
print("i is identical to e ?", i is e)
print("i is not identical to e ?", i is not e)

# [x] Correct the following expression so the answer is `True`
((6 + 2) < 9) == True
# [x] Correct the following expression so the answer is `True`
((6 + 2) < 9) == True
# [x] Correct the following expression so the answer is `True`
(5 + 3) * 2 == 16
# [x] Correct the following expression so the answer is `True`
(4 > 3 and (5 + 6) > 7) == True
