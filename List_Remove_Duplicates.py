def duplist():
	import random
	a=[]
	i=0
	while i < 10:
		a.append(random.randint(1,19))
		i+=1
	print(a)
	return(a)

def remove_duplicates(a):
	return(set(a))

print(remove_duplicates(duplist()))