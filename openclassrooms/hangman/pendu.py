from fonctions import *
import donnees

print("Welcome to the hangman!")

name = input("What is your name ? ")
print("Welcome "+name+"!")

while True:
	score = scores(name)
	print("You have",score,"point(s).")
	stay_or_not = input("Do you wanna play ? (y/n) ")
	if stay_or_not.lower().startswith("n"):
		break
	elif not stay_or_not.lower().startswith("y"):
		print("I didn't understand your choice. Please retry.")
		continue
	else:
		tries = donnees.tries
		letters = []
		word_to_find = choice_word().lower()
		word_guessed = display_word(word_to_find, letters)
		while word_guessed != word_to_find:
			print("Here is the word to find:",word_guessed)
			print("You have",tries,"tries left.")
			letter =""	
			while letter == "" or len(letter)>1 or not letter.isalpha() or letter in letters:
				letter = input("What is your letter ? ")
				if letter == "":
					print("You haven't entered anything !")
					continue
				if len(letter) > 1:
					print("You have entered too many characters !")
					continue
				if not letter.isalpha():
					print("You haven't entered a letter !")
					continue
				if letter in letters:
					print("You already have chosen this letter !")
			print("Your letter is",letter)
			letters.append(letter)
			tries -= 1
			if tries == -1:
				break
			word_guessed = pendu(letter,word_to_find, word_guessed)
		if tries >= 0:
			print("Congratulations, you have found the word !")
			score += tries
			register(name, score)
		else:
			print("Sorry, you lost!")


print("Thank you for playing!")
print("Your final score is "+str(score)+".")
