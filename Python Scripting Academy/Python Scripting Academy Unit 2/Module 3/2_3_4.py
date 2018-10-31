# [x] split the string(rhyme) into a list of words (rhyme_words)
# [x] print each word on it's own line
rhyme = 'Jack and Jill went up the hill To fetch a pail of water' 
rhyme_words = rhyme.split()
for a in rhyme_words:
    print(a)

# [x] split code_tip into a list and print the first and every other word
code_tip = "Python uses spaces for indentation"
code_split = code_tip.split()
for a in range(0,len(code_split),2):
    print(code_split[a])

# [x] split poem into a list of phrases by splitting on "*" a
# [x] print each phrase on a new line in title case
poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*"
poem_split = poem.split("*")
for a in poem_split:
    print(a)

# [x] .join() letters list objects with an Asterisk: "*"
letters = ["A", "s", "t", "e", "r", "i", "s", "k"]
print("*".join(letters))

# [x] complete Choose the separator
phrase_words = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill', 'To', 'fetch', 'a', 'pail', 'of', 'water']
separator = input("Choose the separator (better take space or * or - for readability :D) : ")
print(separator.join(phrase_words))

# [x] use 3 print() statements to output text to one line 
# [x] separate the statements by using "- " (dash space)
print("Line 1 (or not)", end = "-")
print("Line 2 (or not)", end = "-")
print("Line 3 (or not)", end = " ")

# [x] create a string (fact) of 20 or more characters and cast to a list (fact_letters)
# [x] iterate fact, printing each char on one line, except for spaces print a new line
fact = input("What is your fun fact ? ")
fact_letters = list(fact)
for a in fact_letters:
    if a != " ":
        print(a)

# [x] create add the digits
big_number = "123456789101112131415"
number_list = list(big_number)
sum_list = 0
equation = " + ".join(big_number)
print(number_list)
for a in number_list:
    sum_list += int(a)
print(equation,"=",sum_list)
