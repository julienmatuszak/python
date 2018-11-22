import donnees
import pickle
from random import randrange

def scores(name):
	try:
		with open('scores','rb') as f:
			pass
	except FileNotFoundError as exception:
		with open('scores','wb') as f:
			a={}
			b = pickle.Pickler(f)
			b.dump(a)
	finally:	
		with open('scores','rb') as f:
			a = pickle.Unpickler(f)
			b = a.load()
			if name in b.keys():
				with open('scores','r+b') as f:
					c = pickle.Pickler(f)
					c.dump(b)
					return(b[name])
			else:
				with open('scores','r+b') as f:
					b.update({name:0})
					c = pickle.Pickler(f)
					c.dump(b)
					return(b[name])

def register(name, score):
	try:
		with open('scores','rb') as f:
			pass
	except FileNotFoundError as exception:
		print (exception)
	else:
		with open('scores','rb') as f:
			a = pickle.Unpickler(f)
			b = a.load()
			b[name] = score
			with open('scores','r+b') as f:
				c = pickle.Pickler(f)
				c.dump(b)

def choice_word():
	index = -1
	index = randrange(len(donnees.words))
	while len(donnees.words[index]) > 8:
		index = randrange(len(donnees.words))
	return donnees.words[index]

def display_word(word, letters):
	b=list(word)
	c=[]
	for a in b:
		if a in letters:
			c.append(a)
		else:
			c.append("*")
	return "".join(c)

def pendu(letter, word_to_find, word_guessed):
	word_guessed = list(word_guessed)
	if letter in word_to_find:
		print("Congratulations! Your letter is in the word to find !")
		for a in range(len(word_to_find)):
			if letter == word_to_find[a]:
				word_guessed[a] = word_to_find[a]
	word_guessed = "".join(word_guessed)
	return word_guessed
