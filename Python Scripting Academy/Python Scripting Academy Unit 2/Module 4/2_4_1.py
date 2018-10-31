# [x] import cities.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt

# [x] open cities.txt as cities_file
# [x] test cities.txt was opened 
cities_file = open('cities.txt', 'r')
print(cities_file)

# [x] after import and open of cities.txt in task 1
# [x] read cities_file as cities
# [x] display the string: cities
cities = cities_file.read()

# [x] after import and open of cities.txt in task 1
# [x] read cities_file as cities
# [x] display the string: cities
cities = cities_file.read()

# [x] digits of pi
# 1. import digits_of_pi.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o digits_of_pi.txt

# [x] digits of pi
# 2. open as digits_of_pi_text 
# 3. read() 4 char of digits_of_pi_text to pi_digits variable 
# 4. print pi_digits  
digits_of_pi = open('digits_of_pi.txt', 'r')
pi_digits = digits_of_pi.read(4)
print(pi_digits)

# [x] digits of pi
# 5. add to pi_digits string with string addition  
#   a. add next 4 characters from digits_of_pi obtained from read()  
#   b. run the cell multiple times to get more digits of *pi*
pi_digits += digits_of_pi.read(4)
print(pi_digits)

# [x] compelete the task
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file = open('cities.txt', 'r')
cities = cities_file.read()
initials = ""
for a in cities:
    if a.isupper():
        initials += a
    elif a == "\n":
        initials += "\n"
    else:
        pass
print(initials)