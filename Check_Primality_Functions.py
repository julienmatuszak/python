import sys
def get_number():
    return int(input("What's your number ? "))

def prime_or_not(a):
    b=range(2,a)
    for i in b:
        if a%i != 0:
            continue
        else:
            print("This number is not a prime number !")
            sys.exit()
    print("This number is a prime number !")

prime_or_not(get_number())