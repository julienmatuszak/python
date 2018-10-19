# [x] input a variable: age as digit and cast to int
# if age greater than or equal to 12 then print message on age in 10 years 
# or else print message "It is good to be" age
age = int(input("What is your age ? "))
if age >= 12:
    print("In 10 years, you will be", age+10)
else:
    print("It is good to be",age)

# [x] input a number 
# if number IS a digit string then cast to int
# print number "greater than 100 is" True/False
# if number is NOT a digit string then message the user that "only int is accepted"
num = int(input("Give me a number : "))
if type(num) == str:
    num = int(num)
if num > 100:
    print(num,"greater than 100 is",num>100)
else:
    print(num,"greater than 100 is",num>100)

# [x] create check_guess()
# call with test
def check_guess(letter,guess):
    letter = str(letter)
    guess = str(guess)
    if letter.isalpha() is False:
        print("invalid")
    else:
        if guess.isalpha() is False:
            print("invalid")
        else:
            if letter == guess:
                print("correct", letter == guess)
            if letter != guess:
                if guess < letter:
                    print("low")
                else:
                    print("high")
        
check_guess('m','m')
check_guess('m','b')
check_guess('m','w')
check_guess(2,'m')

# [x] call check_guess with user input
def check_guess(letter,guess):
    if letter.isalpha() is False:
        print("invalid")
    else:
        if guess.isalpha() is False:
            print("invalid")
        else:
            if letter == guess:
                print("correct", letter == guess)
            if letter != guess:
                if guess < letter:
                    print("low")
                else:
                    print("high")
        
letter = input("Ask your friend to put a letter that you'll have to guess : ")
guess = input("Gimme your letter : ")
check_guess(letter, guess)

# [x] create letter_guess() function, call the function to test
# would be easier with a loop
# could be improved with a message when more than one character is entered 
def check_guess(letter,guess):
    if letter.isalpha() is False:
        print("invalid")
    else:
        if guess.isalpha() is False:
            print("invalid")
        else:
            if letter == guess:
                print("correct")
            if letter != guess:
                if guess < letter:
                    print("low")
                else:
                    print("high")

def letter_guess():
    letter = input("Ask your friend to put a letter that you'll have to guess : ")
    guess = input("Gimme your letter : ")
    check_guess(letter, guess)
    if letter == guess:
        print(letter == guess, "Well done")
        pass
    else:
        print (letter == guess)
        guess = input("Gimme your letter : ")
        check_guess(letter, guess)
        if letter == guess:
            print(letter == guess, "Well done")
            pass
        else:
            print (letter == guess)
            guess = input("Gimme your letter : ")
            check_guess(letter, guess)
            if letter == guess:
                print(letter == guess, "Well done")
            else:
                print("Sorry, you lost the game :(")

letter_guess()

# [x] complete pet conversation
about_pet = input("Say something about your favourite pet : ")
if 'dog' in about_pet:
    print("Ah, it's a story about a dog")
    pass
if 'cat' in about_pet:
    print("Ah, it's a story about a cat")
    pass
if 'fish' in about_pet:
    print("Ah, it's a story about a fish")
    pass
print("Well, thank you for your story")
