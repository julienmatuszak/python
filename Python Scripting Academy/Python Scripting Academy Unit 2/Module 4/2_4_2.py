# [x] import cities
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
# [x] open cities.txt as cities_file and read the file as a list: cities_lines
cities_file = open('cities.txt', 'r')
cities_lines = cities_file.readlines()
# [x] use list iteration to print each city in cities_lines list
print(cities_lines)
for a in cities_lines:
    print(a)

# [x] re-open file and read file as a list of strings 
# [x] open cities.txt as cities_file and read the file as a list: cities_lines
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file = open('cities.txt', 'r')
cities_lines = cities_file.readlines()
# [x] remove the last character, "\n", of each cities_lines list item 
i = 0
for a in cities_lines:
    cities_lines[i] = a[:-1]
    i += 1
print(cities_lines)
# [x] print each list item in cities_lines
for line in cities_lines:
    print(line)

# [x] open cities.txt as cities_file
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file = open('cities.txt', 'r')
# [x] read the lines as cities_lines
cities_lines = cities_file.readlines()
# [x] print the cities that start with the letter "D" or greater
d_cities = ""
for a in cities_lines:
    if a.lower() > "d":
        d_cities += a
    else:
        pass
print(d_cities)
# [x] close cities_file
cities_file.close()
# [x] test that file is closed
print(cities_file)
# The output shows the object but the file is not read anymore because the lines are not displayed in a list

# [x] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt as poem2.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt -o poem.2.txt
# [x] open poem2.txt as poem2_text in read mode
poem2_text = open('poem_2.txt', 'r')
# [x] create a list of strings, called poem2_lines, from each line of poem2_text
poem2_lines = poem2_text.readlines()
print(poem2_lines)
# [x] remove the newline character for each list item in poem2_lines
i = 0
for a in poem2_lines:
    poem2_lines[i] = a[:-1]
    i += 1
print(poem2_lines)
# [x] print the poem2 lines in reverse order
poem2_lines.reverse()
for a in poem2_lines:
    print(a)
