#!usr/bin/python

max_number = input("Choose a maximum number: ")
while max_number.isdigit() is False or int(max_number) <= 0 :
	print("Sorry, wrong input, choose a strictly positive integer.")
	max_number = input("Choose a maximum number: ")

max_number = int(max_number)


numbers_1000 = list(range(1,max_number+1))
prime_numbers = []
count = 0

for number in numbers_1000:
	divisors = []
	for inferior_number in range(1,number+1):
		if number%inferior_number == 0:
			divisors.append(inferior_number)

	compare_list = [1,number]
	if divisors == compare_list:
		prime_numbers.append(number)
		count += 1

print("The list of prime numbers up to",max_number,"is",prime_numbers)
print("The number of prime numbers up to",max_number,"is",count)