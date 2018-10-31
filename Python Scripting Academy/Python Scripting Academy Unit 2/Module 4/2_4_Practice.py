# [x] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt
# [x]  Open rainbow.txt in read mode & read as list with .readlines()
rainbow = open('rainbow.txt','r')
rainbow_lines = rainbow.readlines()
# [x] sort rainbow_colors list, iterate the list to print each color
rainbow_lines.sort()
for a in rainbow_lines:
    print(a.strip())

# [x] The Weather: import world_mean_team.csv as mean_temp.txt
https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv
# [x] The Weather: open file, read/print first line, convert line to list (splitting on comma)
mean = open('mean_temp.txt', 'r')
headings = mean.readline()
print(headings)
headings_list = headings.split(',')
for a in headings_list:
    print(a)
# [x] The Weather: use while loop to print city and highest monthly average temp in celsius
city_temp = mean.read()
print(city_temp)

# [x] use curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi as pi.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o pi.txt

# [x] Set up the project files and initial values
pi = open('pi.txt', 'r')
name = input("What's your name ? ")
print ("hi", name,"!")
seed = len(name)
pi.seek(seed)
digit = pi.read(1)
guess = input("Enter a single digit guess or 'q' to quit ")
correct = 0
wrong = 0
while guess.isdigit():
    if digit == ".":
        pi.seek(0,1)
        digit = pi.read(1)
    elif digit == "\n":
        seed += 1
        pi.seek(seed)
    else:
        if digit == guess:
            print("correct")
            correct += 1
        else:
            print("incorrect")
            wrong += 1
    guess = input("Enter a single digit guess or 'q' to quit ")
print(correct,"correct answer(s)")
print(wrong,"incorrect answer(s)")