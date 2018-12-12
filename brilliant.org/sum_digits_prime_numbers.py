#!usr/bin/python

print("We want to test if there are some digits who never appear to be the \
sum of the digits of prime numbers.")
print("Example: 997 is a prime number. The sum of its digits is 9+9+7 = 25 \
and 2+5 = 7 so 7 is not included in the list of digits")
print("We consider that going up to 99 is more than enough to verify. \
So we try every prime number until 99 and check if some digits as calculated \
in the example never show up. Here are the results.\n")

numbers = list(range(1,99))
prime_numbers = []
digits = list(range(1,10))

# We create the list of prime numbers
for number in numbers:
	divisors = []
	for inferior_number in range(1,number+1):
		if number%inferior_number == 0:
			divisors.append(inferior_number)

	compare_list = [1,number]
	if divisors == compare_list:
		prime_numbers.append(number)

# We calculate the sum of the digits for each prime number
for number in prime_numbers:
	if number < 10:
		digits.remove(number)
	else:
		while number >= 10:
			number = (number-number%10)/10 + number%10
		if number in digits:
			digits.remove(number)

print("These digits never appear in the results: ",digits)

