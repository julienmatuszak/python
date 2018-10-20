# [x] use a "forever" while loop to get user input of integers to add to sum, 
# until a non-digit is entered, then break the loop and print sum
sum = 0
while True:
    added_num = input("Enter a digit : ")
    if added_num.isdigit() is False:
        break
    else:
        sum += int(added_num)
print(sum)

# [x] use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
rainbow = "red orange yellow green blue indigo violet"
i = 4
while True:
    if i == 0:
        print("You didn't find any color of the rainbow after 4 guesses. You lost!")
        break
    guess = input("Guess the color in the rainbow : ")
    if guess in rainbow:
        print("Congratulations, you found one color of the rainbow after "+str(i)+" guesses!")
        break
    else:
        i -= 1
        print("You have",str(i),"guesses left")

# [x] Get input for a book title, keep looping while input is Not in title format (title is every word capitalized)
title = ""
while title.istitle() is False:
    title = input("Write a title, and don't forget that every word is capitalized : ")
print("Congratulations, you managed to write your title!")

# [x] create a math quiz question and ask for the solution until the input is correct
guess = 0
while guess != 1+2:
    guess = int(input("How much is 1 + 2 ? "))
    if guess == 1+2:
        break
    print("You don't have the correct result! Try again!")
print("Well done! You found the right result!")

# [x] review the code, run, fix the error
tickets = int(input("enter tickets remaining (0 to quit): "))

while tickets > 0:
        # if tickets are multiple of 3 then "winner"
    if int(tickets/3) == tickets/3:
        print("you win!")
    else:
        print("sorry, not a winner.")
    tickets = int(input("enter tickets remaining (0 to quit): "))
    
print("Game ended")

# Create quiz_item() and 2 or more quiz questions that call quiz_item()
solution = "white"
question = "What is the color of a white horse ? "
def quiz_item(question, solution):
    answer = ""
    while answer.lower() != solution:
        answer = input(question)
    return True 
    
quiz_item(question, solution)