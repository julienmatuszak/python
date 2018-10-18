#[x] increase the number of arguments used in print() to 8 or more 
student_age = 17
student_name = "Hiroto Yamaguchi"
print(student_name,'will be in the class for',student_age, 'year old students.')

#[x] define (def) a simple function called yell_it() and call the function
def yell_it():
    phrase = "phrase"
    print(phrase.upper()+"!")
yell_it()

# [x] define yell_this() 
def yell_this(yell):
    print(yell.upper() + "!")

# [x] get user input in variable words_to_yell
words_to_yell = input("What do you wanna yell ? : ")

# [x] call yell_this function with words_to_yell as argument
yell_this(words_to_yell)
