import random
import sys

count = 0
num = random.randint(1,10)

while True:
    guess = input("Can you guess the number between 1 and 9 ? ")
    count+=1
    if guess == 'exit':
        break
    elif guess == num:
    	if count == 1:
    		print("Congrats! It took you only 1 time to find the right number!")
    	else:
			print("Congrats! You have guessed the right number! It took you " + str(count) + " times to find the right number!")
        sys.exit()
    elif guess > num:
    	print("Your guess is too high. Please choose a lower number.")
    	continue
    else:
    	print("Your guess is too low. Please choose a higher number.")
    	continue