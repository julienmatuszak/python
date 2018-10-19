msg = "hello"
# [x] print the True/False results of testing if msg string equals "Hello" string
if msg == "Hello":
    print(msg == "Hello")
else:
    print(msg == "Hello")

greeting = "Hello"
# [x] get input for variable named msg, and ask user to 'Say "Hello"'
# [x] print the results of testing if msg string equals greeting string
msg = input('Say "Hello": ')
if msg == greeting:
    print(msg==greeting)
else:
    print(msg==greeting)

# [x] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# [x] print messages for correct answer "21" or incorrect answer using if/else
# note: input returns a "string"
answer = input('What is 8 + 13? : ')
if answer == "21":
    print("Congrats, your answer is correct !")
else:
    print("incorrect answer")

# [x] Create the program, run tests
def tf_quiz():
    question = "Should save your notebook after edit ? (T/F) : "
    correct_ans = input(question)
    if correct_ans == "T":
        print("correct")
    elif correct_ans == "F":
        print("incorrect")
    else:
        print("didn't get your answer, try again please")
        exit()
    
tf_quiz()
