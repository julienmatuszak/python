# review and run example using \n (new line)
print('Hello World!\nI am formatting print ')

# review and run code using \t (tab)
student_age = 17
student_name = "Hiroto Yamaguchi"
print("STUDENT NAME\t\tAGE")
print(student_name,'\t' + str(student_age))

# review and run code 
# using \" and \' (escaped quotes)
print("\"quotes in quotes\"")
print("I\'ve said \"save your notebook,\" so let\'s do it!")

# using  \\ (escaped backslash)
print("for a newline use \\n")

# [x] print "\\\WARNING!///"
print('"\\\\\\WARNING!///"')

# [x] print output that is exactly (with quotes): "What's that?" isn't a specific question.
print('"What\'s that? isn\'t a specific question."')

# [x] from 1 print statement output the text commented below using no spaces
# One     Two     Three
# Four    Five    Six
print("One\tTwo\tThree")
print("Four\tFive\tSix")

# [x] create and test pre_word()
def pre_word(word):
    if word.startswith("pre"):
        if word.isalpha():
            return True
        else:
            return False
    return False

word=input("Enter a word : ")
pre_word(word)

# [x] review, run, fix
print("Hello" + "\n" + "World!")
#can also be print("Hello\nWorld!")
