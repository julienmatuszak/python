# [x] Import the math module and use an appropriate function to find the greatest common divisor of 16 and 28
from math import gcd
gcd(16,28)

# [x] Prompt the user to input 2 positive integers then print their greatest common divisor
num1 = input("Give me a positive integer : ")
num2 = input("Give me a positive integer : ")
from math import gcd
gcd(int(num1),int(num2))

# [x] Fill out the function is_even with a code block that returns True if n is even and returns False if n is odd
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
# Test the function 
x = 5
if is_even(x):
    print("Number is even")
else:
    print("Number is odd")

# [x] Use the function is_even to print the square root of all the even numbers in the following list
from math import sqrt
def is_even(n):
    return (n % 2) == 0
l = [25, 34, 193, 2, 81, 26, 44]
even_sqrt_l = []
for a in range(0,len(l)):
    if is_even(l[a]):
        even_sqrt_l.append(round(sqrt(l[a]),2))                          
print(even_sqrt_l)

# [x] Correct the following expression so the answer is 10
(4 + 16) / 2

# [x] Correct the following expression so the answer is 250; review the operator precedence table and use only one () pair
2 * (3 + 2) ** 3

# [x] Use an appropriate rounding function to round 75.34 to 75 and then to 76
import math
x = 75.34
print(floor(x))
print(ceil(x))

# [x] Use an appropriate rounding function to fix the following `float` error
# Price of a chocolate box
p = 4.35
# Quantity needed
q = 200
# Order total price (Should be 4.35 * 200 = $870.00)
total = p * q
print("Total price: ", ceil(total))

# [x] Modify the die_roller() function to use randrange instead of randint
from random import randrange
def die_roller ():
    return (randrange(1, 7))
# roll a die
print(die_roller())

# [x] Modify the odd_random() function to use randint instead of randrange
from random import randint
def odd_random():
    return 2*(randint(0, 50)) + 1
# Generate an odd random integer
print(odd_random())

# [x] Complete the function dice_roller() so it rolls 2 dice
# Use the die_roller function
from random import randint
def die_roller():
    return(randint(1, 6))
def dice_roller():
    return die_roller() + die_roller()
print(dice_roller())

# [x] Modify the pick_card() function to use `shuffle` instead of choice
from random import shuffle, randint

def pick_card():
    card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades'];
    card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'] 
    shuffle(card_type)
    shuffle(card_number)  
    # choose a type at random
    t = card_type[0]
    n = card_number[0]
    return [n, t]
# Show the randomly picked card
print(pick_card())

# [x] The following list contain the 10 most populous American cities; write code to randomly select one of the cities to visit
from random import randint, randrange, shuffle, choice
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
print("Next year, I'm gonna visit",cities[randint(0,len(cities)-1)])
print("The year after, I'm gonna visit",cities[randrange(0,len(cities))])
shuffle(cities)
print("Then I will visit",cities[0])
print("And then",choice(cities))