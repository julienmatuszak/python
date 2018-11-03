import random

i=0
a=[]
b=[]

while i<10:
	a.append(random.randint(1, 19))
	b.append(random.randint(1, 19))
	i+=1

c=[j for j in a if j in b]

set(c)