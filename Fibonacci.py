def get_number():
	a=int(input("How many Fibonacci numbers do you want? "))
	if a == 0:
		print("Invalid choice. Try again.")
	return(a)

def Fibonacci(a):
	b=[1,1]
	i=1
	while i < a-1:
	    c = b[i] + b[i-1]
	    b.append(c)
	    i+=1
	return(b)

print(Fibonacci(get_number()))