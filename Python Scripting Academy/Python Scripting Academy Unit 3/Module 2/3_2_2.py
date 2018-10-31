# [x] The following program tests if `num` is prime or not, use a `break` statement to improve its efficiency
# and reduce the number of necessary iterations
# Compare the number of necessary iterations with and without the `break` statement
# Use the following numbers for the comparison: 
num = 45345
#num = 11579
#num = 948240
#num = 128093
#num = 519937
#num = 694394
prime = True # assume num is prime unless proven otherwise
iteration_count = 0
for i in range(2, num):
    if num % i == 0:
        prime = False;
        break
    iteration_count = iteration_count + 1
# Display results
if prime:
    print(num, "is prime")
else:
    print(num, "is NOT prime")
print("Total number of iterations:", iteration_count)

# [x] Write a program to prompt the user for an odd number; use an infinite loop and a `break` statement.
while True:
    x = int(input("Enter an odd number: "))
    if (x%2 != 0):
        break

# [x] Modify the following program to display numbers that are divisible by 7 along with their square roots.
# HINT: Use a `continue` statement in the loop
from math import sqrt
for num in range(1, 100):
    if (num%7 != 0):
        continue
    print(num)
    print(round(sqrt(num),2))

# [x] Write a program to display the sum of each row in table
table = [[5, 2, 6], [4, 6, 0], [9, 1, 8], [7, 3, 8]]
for row in table:
    a = 0
    for b in row:
        a += b
    print(a, end = " ")
# [x] Complete the function `generate_star` so it displays a star of variable `size` using "*"
# For size = 5 the star should look like:
# *   *
#  * * 
#   *  
#  * * 
# *   *

def generate_star(size):
    star = []
    for a in range(size):
        for b in range(size):
            if b == a:
                print("*", end = " ")
            elif (a+b) == 4:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
    #pass
# Display star
generate_star(5)
# [x] Complete the following program to count the number of even positive numbers, odd negative numbers, and zeros in `lst`
lst = [9, 0, -2, -4, -5, 2, -15, 6, -65, -7]
even_positives = 0
odd_negatives = 0
zeros = 0
for a in range(len(lst)):
    if (lst[a]%2 == 0 and lst[a]>=0):
        even_positives +=1
    elif (lst[a] <=0 and lst[a]%2 != 0):
        odd_negatives += 1
    elif lst[a] == 0:
        zeros += 1
    else:
        pass         
print("Number of even positives:", even_positives)
print("Number of odd negatives:", odd_negatives)
print("Number of zeros:", zeros)

# [x] Write a program to count the number of punctuation marks (. , ? ! ' " : ;) in `s`

s = "Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth." # Sherlock Holmes (by Sir Arthur Conan Doyle, 1859-1930)
p=0
for a in range(len(s)):
    if s[a]=="." or s[a]=="," or s[a]=="?" or s[a]=="!" or s[a]=="\'"or s[a]=="\"" or s[a] == ":" or s[a] == ";":
        p+=1
print("There is",str(p),"punctuation marks")

# [x] Write a program to prompt the user for an odd positive number; use an infinite  loop and a `break` statement.

while True:
    x = int(input("Enter an odd positive number: "))
    if (x > 0 and x%2 !=0):
        break
