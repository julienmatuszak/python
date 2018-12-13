import math

first_number = input("Choose a number: ")
while first_number.isdigit() is False or int(first_number) <= 0 :
	print("Sorry, wrong input, choose a strictly positive integer.")
	first_number = input("Choose a maximum number: ")

second_number = input("Choose another number: ")
while second_number.isdigit() is False or int(second_number) <= 0 :
	print("Sorry, wrong input, choose a strictly positive integer.")
	second_number = input("Choose a maximum number: ")

first_number, second_number = int(first_number), int(second_number)

first_divisors = []
second_divisors = []

for number in range(1,first_number+1):
	if first_number%number == 0:
		first_divisors.append(number)

print("The divisors of the first number are : ",first_divisors)


for number in range(1,second_number+1):
	if second_number%number == 0:
		second_divisors.append(number)

print("The divisors of the first number are : ",second_divisors)

for number in first_divisors:
	if number in second_divisors:
		first_gcd = number

for number in second_divisors:
	if number in first_divisors:
		second_gcd = number

print("The greatest common divisor between",first_number,"and",second_number,"is",max(first_gcd,second_gcd))