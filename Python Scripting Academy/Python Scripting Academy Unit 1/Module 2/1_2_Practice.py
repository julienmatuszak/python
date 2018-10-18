# [x] define and call a function short_rhyme() that prints a 2 line rhyme
def short_rhyme(a,b):
    print("I am a",a)
    print("And you are a",b,"!")

first_rhyme = input("Type in a simple word : ")
second_rhyme = input("Type a second word that ends the same : ")
short_rhyme(first_rhyme,second_rhyme)

# [x] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case
def title_it(msg):
    print(msg.title())
    
message = input("What's your message ? ")
title_it(message)

# [x] get user input with prompt "what is the title?" 
# [x] call title_it() using input for the string argument
message = input("what is the title ? ")
title_it(message)

# [x] define title_it_rtn() which returns a titled string instead of printing
# [x] call title_it_rtn() using input for the string argumetnt and print the result

def title_it_rtn(msg):
    return(msg.title())

message = input("What is the title ? ")
print(title_it_rtn(message))

# [x] create, call and test bookstore() function
def bookstore(book,price):
    rtn = "Title: "+ title_it_rtn(book) + ", costs " + price
    return(rtn)

b = input("What's the name of the book please ? ")
p = input("How about the price ? ")
print(bookstore(b,p))

def make_greeting(name, greeting):
    return (greeting + " " + name + "!")

def get_name():
    name_entry = input("enter a name: ")
    return name_entry

def get_greeting():
    greeting_entry = input("enter a greeting: ")
    return greeting_entry

# get name and greeting, send to make_greeting 
print(make_greeting(get_name(), get_greeting()))

