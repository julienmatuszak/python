import random
import sys

def RPS():
    while True:
        play = input("Choose your play: Rock, Paper or Scissors ? ")
        a=['Rock','Paper','Scissors']
        if play != 'Rock' and play != 'Paper' and play != 'Scissors':
            print("Invalid choice. Please write your choice again.")
            continue
        b=random.choice(a)
        print(b)
        if play == b:
            print ("Draw!")
        else:
            for i in a:
                if i == play and b == a[(a.index(i)-1) % len(a)]:
                    print ("Congratulations! You won! ")
                    break
                elif i==play and b == a[(a.index(i)+1) % len(a)]:
                    print ("Sorry! You lost.")
                    break
        while True:
            next = input("Do you want to play again? Y/N ")
            if next == 'Y':
                RPS()
            elif next == 'N':
                sys.exit()
            else:
                print("Invalid choice. Please write your choice again.")
                continue
RPS()