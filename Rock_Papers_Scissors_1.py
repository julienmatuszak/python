import sys

user1 = input("Player 1 - What's your name ? ")
user2 = input("Player 2 - What's your name ? ")
user1_answer = input("%s, what do you choose, rock, paper or scissors ? " % user1)
user2_answer = input("%s, what do you choose, rock, paper or scissors ? " % user2)

def compare(u1,u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors wins!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors wins!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors. Try again.")
        sys.exit()

print(compare(user1_answer,user2_answer))