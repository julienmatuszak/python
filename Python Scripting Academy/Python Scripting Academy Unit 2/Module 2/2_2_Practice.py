# [x] create and populate list called days_of_week then print it
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print (days_of_week)

# [x] after days_of_week is run above, print the days in the list at odd indexes 1,3,5
print(days_of_week[1::2])

# [x] create and populate list called phone_letters then print it
phone_letters = [" ","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
print(phone_letters)

# [x] create a variable: day, assign day to "Tuesday" using days_of_week[]
# [x] print day variable
day = days_of_week[1]
print(day)

# PART 2
# [x] assign day to days_of_week index = 5
# [x] print day
day = days_of_week[5]
print(day)

# [x] Make up a new day! - append an 8th day of the week to days_of_week 
# [x] print days_of_week
days_of_week.append("Newday")
print(days_of_week)

# [x] Make up another new day - insert a new day into the middle of days_of_week between Wed - Thurs
# [x] print days_of_week
days_of_week.insert(3,"Midday")
print(days_of_week)

# [x]  Extend the weekend - insert a day between Fri & Sat in the days_of_week list
# [x] print days_of_week
days_of_week.insert(6,"Weekendday")
print(days_of_week)

# [x] print days_of_week 
# [x] modified week is too long - pop() the last index of days_of_week & print .pop() value
# [x] print days_of_week
print(days_of_week)
days_of_week.pop()
print(days_of_week)

# [x] print days_of_week 
# [x] delete (del) the new day added to the middle of the week 
# [x] print days_of_week
print(days_of_week)
del days_of_week[3]
print(days_of_week)

# [x] print days_of_week 
# [x] programmers choice - pop() any day in days_of week & print .pop() value
# [x] print days_of_week
print(days_of_week)
day = days_of_week.pop(0)
print(day,"is boring")
print(days_of_week)

# [x] create let_to_num()
phone_letters = [" ","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
def let_to_num(letter):
    key = 0
    if letter == "":
        return 1
    while key < 10:
        if letter.isdigit():
            return "Sorry, you entered a digit, please try again"
            break
        elif letter.upper() in phone_letters[key]:
            return key
            break
        else:
            key += 1
    return "Not Found"
letter = input("Which letter (or character) are you looking the number for ? ")
print(let_to_num(letter))

# [x] Challenge: write the code for "reverse a string"
def reverse(toReverse):
    a = ""
    reverted = []
    while toReverse != []:
        a = toReverse.pop()
        reverted.insert(0,a)
    return reverted

toReverse = ["String","to","Reverse"]
print(reverse(toReverse))
