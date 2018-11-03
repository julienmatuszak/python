import random
import string

limit = random.randint(10,14)
i = 0
passwd = []
c = ['@', '.', '-', '_']
while i < limit:
	j = random.randint(1,20)
	if j > 0 and j < 9:
	    passwd.append(str(random.randint(1,9)))
	elif j > 8 and j < 18:
	    passwd.append(random.choice(string.letters))
	else:
		passwd.append(random.choice(c))
	i+=1

print("Your password is " + ''.join(passwd))