# [x] Say "Hello" with nested if
# [x] Challenge: handle input other than y/n

hello = input('Say "Hello"? (y/n) ')
# select sandwich type sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')

if hello.lower() == "y":
    # select cheese type
    full_hello = input('Full "Hello"? (y/n) ')
    
    if full_hello.lower() == "y":
        print("Hello")
    elif full_hello.lower() == "n":
        print("Hi") 
    else:
        print("Sorry, I didn't understand your greeting.")

elif hello.lower() == "n":
    print("{friendly nod}")
        
else:
    print("Sorry, I didn't understand your greeting.")


# [x] Create the "Guess the bird" program 
birds = "eagle, magpie, owl"

print("Start: Guess the bird")
bird1 = input('Guess the bird : ')
# select sandwich type sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')

if bird1.lower() in birds :
    # select cheese type
    print("Yes, 1st try!")
else:
    print("Sorry, wrong")
    bird2 = input('Guess the bird : ')
    if bird2.lower() in birds :
        print("Yes, 2nd try!") 
    else:
        print("Sorry, wrong")
        bird3 = input('Guess the bird : ')
        if bird3.lower() in birds :
            print("Yes, 3rd try!") 
        else:
            print("Sorry, out of tries.")
