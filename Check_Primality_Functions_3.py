#Assumes that "a" contains an integer > 2 whose primality needs to be verified
# The algorithm builds a list of factors including the number 2 and all odd numbers
# up to square root of "a", and then checks if any of those numbers divides "a"
# without a remainder - if so then "a" is not prime, else it is
import math
a=int(input("Enter a number : "))
if sum([ True if a%factor == 0 else False for factor in ([2] + list(range(3,int(math.sqrt(a)),2) ))]):
	print("Number is composite")
else:
	print("Number is prime")