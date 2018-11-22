from random import randrange
from math import ceil

money = 50

def roulette(choice):
	number = 0
	color = ""
	black_red = False
	win_number = False
	number = randrange(51)
	if number%2 == 0:
		color = "black"
	if number %2 == 1:
		color = "red"
	if (choice %2 == 0 and number%2 == 0) or (choice %2 != 0 and number%2 != 0):
		black_red = True
	if choice == number:
		win_number = True
	print("The roulette shows",number)
	print("The color is",color)
	return black_red, win_number

while True:
	yes_no = input("Do you wanna play ? (y/n) ")
	if yes_no.lower().startswith("n"):
		break
	else:
		print("Welcome to Z casino! Today we will play roulette.")
		print("You have "+str(money)+"$.")
		bet = 0
		while bet <= 0 or bet > money:
			try:
				bet = input("How many dollars do you wanna bet (only units allowed) ? ")
				bet = float(bet)
				bet = int(bet)
			except ValueError as exception:
				print("Your bet is not a number")
				bet = 0
				continue
			except TypeError as exception:
				print("Your bet is not a number")
				bet = 0
				continue
			else:
				if bet == 0:
					print("You cannot bet nothing!")
					continue
				if bet < 0:
					print("You cannot bet a negative number!")
					continue
				if bet > money:
					print("Your bet is more than what you have!")
					continue
		print("Your bet is $"+str(bet))
		money -= bet
		print("You now have $"+str(money))
		choice = -1
		while choice <= -1 or choice > 50:
			try:
				choice = input("Which number do you want to play ? ")
				choice = float(choice)
				choice = int(choice)
			except ValueError as exception:
				print("Your bet is not a number")
				choice = -1
				continue
			except TypeError as exception:
				print("Your bet is not a number")
				choice = -1
				continue
			else:
				if choice <= -1:
					print("Your choice is out of range!")
					continue
				if choice > 50:
					print("Your choice is out of range!")
					continue
		print("Your choice is",choice)
		if choice%2 ==0:
			print("Your color is black")
		if choice%2 ==1:
			print("Your color is red")
		black_red, number = roulette(choice)
		if number:
			print("You have the right number! You win 3 times your bet!")
			print("You have won $",int(ceil(3*bet)))
			money += int(ceil(3*bet))
			print("You now have $",money)
		elif black_red:
			print("You didn't get the right number but you have the right color!")
			print("You have won $",int(ceil(bet/2)))
			money += int(ceil(bet/2))
			print("You now have $",money)
		else:
			print("Sorry! You have lost.")
			print("You now have $",money)
print("Thank you for playing !")
