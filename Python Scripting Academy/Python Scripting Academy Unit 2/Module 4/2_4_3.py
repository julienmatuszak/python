# [x] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt
# [x] open rainbow.txt as rainbow_text
rainbow_text = open('rainbow.txt', 'r')
# [x] read the first 3 lines into variables: color1, color2, color3
color1 = rainbow_text.readline()
color2 = rainbow_text.readline()
color3 = rainbow_text.readline()
# [x] close rainbow.txt
rainbow_text.close()
# [x] print the first 3 colors
print(color1 + color2 + color3)

# [x] open rainbow.txt as rainbow_text as read-only
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt
rainbow_text = open('rainbow.txt', 'r')
# [x] read the color from lines of rainbow_text in a while loop
# [x] print each color capitalized as the loop runs
rainbow_line = rainbow_text.readline()
while rainbow_line:
    print(rainbow_line[:-1].capitalize())
    rainbow_line = rainbow_text.readline()
# [x] close rainbow_text 
rainbow_text.close()

# [x] open rainbow.txt as rainbow_text as read-only  
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt
rainbow_text = open('rainbow.txt', 'r')
# [x] read a color from each line of rainbow_text in a while loop  
# use .strip to remove the whitespace '\n' character 
# print each color upper case 
rainbow_line = rainbow_text.readline().strip()
while rainbow_line:
    print(rainbow_line.upper())
    rainbow_line = rainbow_text.readline().strip()
rainbow_text.close()

# [x] import the file
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities_messy -o cities_messy.txt
# [x] run to read the file into memory
cities_messy = open('cities_messy.txt', 'r')
# [x] edit the code to remove leading or trailing colon, newline and space characters
line = cities_messy.readline().strip(':\n')
while line:
    print(line)
    line = cities_messy.readline().strip(':\n')

# [x] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy as poem2_messy.txt  
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy -o poem2_messy.txt
# [x] open poem2_messy.txt as poem2_messy in read mode
poem2_messy = open('poem2_messy.txt', 'r')
# [x] edit while loop to strip the leading and trailing parentheses, and newlines
# [x] print the poem 
line = poem2_messy.readline().strip('(').strip(')\n')
while line:
    print(line)
    line = poem2_messy.readline().strip('(').strip(')\n')
