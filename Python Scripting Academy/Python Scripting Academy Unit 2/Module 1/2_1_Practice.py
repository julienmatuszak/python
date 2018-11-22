# [x] access and print the second character from planet_name: "u"
planet_name = "Jupiter"
print(planet_name[1])

# [x] access and print the first character from planet_name: "J"
planet_name = "Jupiter"
print(planet_name[0])

# [x] access and print the first and last characters from planet_name
planet_name = "Jupiter"
print(planet_name[0],planet_name[-1])

# [x] using a negative index access and print the first character from planet_name: "J"
planet_name = "Jupiter"
print(planet_name[-7])

# [x] print planet_name sliced into the first 3 characters and remaining characters
planet_name = "Neptune"
print(planet_name[:3])
print(planet_name[3:])

# [x] print 1st char and then every 3rd char of wise_words
# use string slice with a step
wise_words = 'Play it who opens'
print(wise_words[0::3])

# [x] print planet_name in reverse
print(planet_name[::-1])

# [x] Get user input for 1 fav_food
# [x] iterate through letters in fav_food 
#    - print each letter on a new line
fav_food = input("What's your favourite food ? ")
for a in fav_food:
    print(a)

# [x] iterate work_tip string concatenate each letter to variable: new_string 
# [x] concatenate the letter or a "-" instead of a space " "
# tip: concatenate string example: word = word + "a"
work_tip = "Good code is commented code"
new_string = ""
for a in work_tip:
    if a == " ":
        a = "-"
    new_string += a
print(new_string)

# [x] Print the first 4 letters of name on new line
name = "Hiroto"
for a in name[:4]:
    print (a)

# [x] Print every other letter from 2nd to last letter of name 
name = "Hiroto"
other = ""
for a in name[1::2]:
    other += a
print(other)

# [x] Create Mystery Name
first_name = input("What is your first name ? ")
new_name = ""
for a in first_name[::-1]:
    if a.lower() == "e":
        a = "?"
    if a.lower() == "t":
        a = "?"
    if a.lower() == "a":
        a = "?"
    new_name += a
print (new_name)

# [x] find and display the length of the string: topic
topic = "len() returns the length of a string"
print(len(topic))

# [x] use len() to find and display the mid_pt (middle) index (+/- 1) of the string: topic
# note: index values are whole numbers
topic = "len() can take a sequence, like a string, as an argument"
print(str(int(len(topic)/2)))

# [x] print index where first instance of the word "code" starts using .find()
work_tip = "Good code is commented code"
work_tip.find("code")

# [x] search for "code" in code_tip using .find() 
# [x] search substring with substring index start= 13,end = last char 
# [x] save result in variable: code_index
# [x] display index of where "code" is found, or print "not found" if code_index == -1
work_tip = "Good code is commented code"
print(work_tip.find("code"))
code_index = work_tip.find("code",13)
if code_index == -1:
    print("not found")
else:
    print ("code_index =",code_index)

# [x] find and report (print) number of w's, o's + use of word "code"
work_tip = "Good code is commented code"
print("Number of w's :",work_tip.count("w"))
print("Number of o's :",work_tip.count("o"))
print('Number of "code"\'s :',work_tip.count("code"))

# [x]  count times letter "i" appears in code_tip string
# [x] find and display the index of all the letter i's in code_tip
# Remember: if .find("i") has No Match, -1 is returned
code_tip = "code a conditional decision like you would say it"
index_i = ""
code_index = 0
print ("code_tip:" , code_tip)
print("Number of i's :",code_tip.count("i"))
while code_tip.find("i",code_index+1) != -1:
    code_index = code_tip.find("i",code_index+1)
    index_i += str(code_index)+" "
print ("Indexes of i's:",index_i)

# [x] create words after "G"
#quote="Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)

def words_after_g(quote):
    a = ""
    result = ""
    start = 0
    space_index = quote.find(" ")
    while space_index != -1:
        word = quote[start:space_index]
        if word[0].lower() <= "g":
            result += ""
        else:
            for x in word:
                if x.isalpha() is False:
                    result += ""
                result += x
            result += "\n"
        start = space_index+1
        space_index = quote.find(" ",start)
    result += quote[start:]
    print(result.upper())

quote = input("enter a 1 sentence quote, non-alpha separate words : ")
words_after_g(quote)

