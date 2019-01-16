#!usr/bin/python

max_number = input("Choose a maximum number: ")
while max_number.isdigit() is False or int(max_number) <= 0 :
	print("Sorry, wrong input, choose a strictly positive integer.")
	max_number = input("Choose a maximum number: ")

max_number = int(max_number)

numbers = list(range(max_number + 1))

count = 0
numbers_with_3_divisors = []

for number in numbers:
	divisors = []
	for inferior_number in range(1,number+1):
		if number%inferior_number == 0:
			divisors.append(inferior_number)

	if len(divisors) == 3:
		numbers_with_3_divisors.append(number)
		count += 1

print("The number of numbers with exactly three divisors is",count)
print("Those numbers are",numbers_with_3_divisors)