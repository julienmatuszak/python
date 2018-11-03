def get_table():
	import random
	a=[]
	i=0
	while i < 10:
	    a.append(random.randint(1,99))
	    i+=1
	return(a)

def keep_first_and_last(a):
	print(a)
	b=[]
	i=0
	while i < len(a):
		if i == 0:
			b.append(a[0])
		c = i
		i+=1
	b.append(a[c])
	print(b)

keep_first_and_last(get_table())