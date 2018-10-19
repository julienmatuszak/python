# [x] print a string that outputs the following exactly: The new line character is "\n"
print("The new line character is \"\\n\"")

# [x] print output that is exactly (with quotes): "That's how we escape!"
print("\"That\'s how we escape!\"")

# [x] with only 1 print statement and using No Space Characters, output the text commented below  

# 1       one
# 22      two
# 333     three
print("1\tone\n22\ttwo\n333\tthree")

# [x] create and test quote_me()
def quote_me(string):
    return "\""+string+"\""

string=input("enter a string to quote")
print(quote_me(string))


# [x] create shirt order using nested if 
def shirt_order(color,size):
    if color.lower() == 'white':
        color_available = True
        if size.lower() == 's':
            size_available = False
        elif size.lower() == 'm':
            size_available = True
        elif size.lower() == 'l':
            size_available = True
        else:
            size_available = False
    elif color.lower() == 'blue':
        color_available = True
        if size.lower() == 's':
            size_available = True
        elif size.lower() == 'm':
            size_available = True
        elif size.lower() == 'l':
            size_available = False
        else:
            size_available = False
    else:
        color_available = False
    if color_available == True:
        print("Your color is available")
        if size_available == True:
            print("Your size is available\nWe will order a "+color.lower()+" shirt size "+size.upper())
        else:
            print("Sorry, your size is not available")
    else:
        print("Sorry, your color is not available")

color = input("Choose your color (White, Blue) : ")
size = input("Choose your size (S,M,L) : ")
shirt_order(color,size)


# [x] create and test str_analysis()
def str_analysis(sod):
    if sod.isdigit():
        sod = int(sod)
        if sod > 99:
            print("Your something is a big number")
        else:
            print("Your something is a small number")
    elif sod.isalpha():
        print("Your something is all alpha")
    else:
        print("Your something is neither all alpha nor all string")

str_or_digit = input("Enter something : ")
str_analysis(str_or_digit)

# [x] create and call ticket_check()
def ticket_check(section,seats):
    if section.startswith('g'):
        if seats>=1:
            if seats<=10:
                return True
            else:
                return False
        else:
            return False
    elif section.startswith('f'):
        if seats>=1:
            if seats<=4:
                return True
            else:
                return False
        else:
            return False
    else:
        print("Sorry, you chose a wrong section")

section = input("What's your section, floor or general (f/g) ? ")
seats = int(input("What's your seat number ? "))
print(ticket_check(section,seats))
