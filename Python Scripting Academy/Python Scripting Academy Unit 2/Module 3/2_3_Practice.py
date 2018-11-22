# [x] print out the "physical states of matter" (matter_states) in 4 sentences using list iteration
# each sentence should be of the format: "Solid - is state of matter #1" 
matter_states = ['solid', 'liquid', 'gas', 'plasma']
index = 1
for a in matter_states:
    print(a.capitalize(),"- is state of matter #",index)
    index += 1

# [x] iterate the list (birds) to see any bird names start with "c" and remove that item from the list
# print the birds list before and after removals
birds = ["turkey", "hawk", "chicken", "dove", "crow"]
print(birds)
for a in birds:
    if a.lower().startswith("c"):
        birds.remove(a)
print (birds)

# the team makes 1pt, 2pt or 3pt baskets
# [x] print the occurrence of each type of basket(1pt, 2pt, 3pt) & total points using the list baskets
baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
number_1_pt = 0
number_2_pt = 0
number_3_pt = 0
for a in baskets:
    if a == 1:
        number_1_pt += 1
    elif a == 2:
        number_2_pt += 1
    elif a == 3:
        number_3_pt += 1
print("number of 1pt : ",number_1_pt)
print("number of 1pt : ",number_2_pt)
print("number of 1pt : ",number_3_pt)

# [x] using range() print "hello" 4 times
for a in range(0,4):
    print("hello")

# [x] find spell_list length
# [x] use range() to iterate each half of spell_list  
# [x] label & print the first and second halves
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
spell_list_1 = []
spell_list_2 = []
for a in range(0,int(len(spell_list)/2)):
    spell_list_1.append(spell_list[a]) 
for a in range(int(len(spell_list)/2),int(len(spell_list))):
    spell_list_2.append(spell_list[a])
print(spell_list_1)
print(spell_list_2)

# [x] build a list of numbers from 20 to 29: twenties 
# append each number to twenties list using range(start,stop) iteration
# [x] print twenties
twenties = []
for a in range(20,30):
    twenties.append(a)
print(twenties)

# [x] iterate through the numbers populated in the list twenties and add each number to a variable: total
# [x] print total
total = 0
for a in twenties:
    total += a
print(total)

# check your answer above using range(start,stop)
# [x] iterate each number from 20 to 29 using range()
# [x] add each number to a variable (total) to calculate the sum
# should match earlier task 
total = 0
for a in range(20,30):
    total += a
print(total)

# [x] create a list of odd numbers (odd_nums) from 1 to 25 using range(start,stop,skip)
# [x] print odd_nums
# hint: odd numbers are 2 digits apart
odd_nums = list(range(1,26,2))
print(odd_nums)

# [x] create a descending list of odd numbers (odd_nums) from 25 to 1 using range(start,stop,skip)
# [x] print odd_nums,  output should resemble [25, 23, ...]
odd_nums = list(range(1,26,2))
odd_nums.reverse()
print(odd_nums)

# the list, elements, contains the names of the first 20 elements in atomic number order
# [x] print the even number elements "2 - Helium, 4 - Beryllium,.." in the list with the atomic number
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']
for a in range(0,20,2):
    print(elements[a+1])

# [x] print the combined lists (numbers_1 & numbers_2) using "+" operator
numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# pythonic casting of a range into a list
numbers_2 = list(range(30,50,2))
print("numbers_1:",numbers_1)
print("numbers_2",numbers_2)
numbers = numbers_1 + numbers_2
print(numbers)

# [x] print the combined element lists (first_row & second_row) using ".extend()" method
first_row = ['Hydrogen', 'Helium']
second_row = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
print("1st Row:", first_row)
print("2nd Row:", second_row)
first_row.extend(second_row)
print(first_row)

# [x] create the program: combined 3 element rows 

elem_1 = ['Hydrogen', 'Helium'] 
elem_2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem_3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
elem = elem_1 + elem_2 + elem_3
print("The 1st three rows of the Period Table of Elemets contain:\n",elem,"\n\nThe row breakdown is\nRow 1:",", ".join(elem_1),"\nRow 2:",", ".join(elem_2),"\nRow 3:",", ".join(elem_3))

# [x] .extend() jack_jill with "next_line" string - print the result
jack_jill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
next_line = ['To', 'fetch', 'a', 'pail', 'of', 'water']
jack_jill.extend(next_line)
print(" ".join(jack_jill))

# [x] use .reverse() to print elements starting with "Calcium", "Chlorine",... in reverse order
#this exercise is not clear because it says "Calcium", Chlorine" but "Chlorine" is not the 2nd element
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 
            'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 
            'Potassium', 'Calcium']
elements.reverse()
print(elements)

# [x] reverse order of the list... Then print only words that are 8 characters or longer from the now reversed order
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
spell_list.reverse()
for a in spell_list:
    if len(a) >= 8:
        print(a)

# [x] sort the list element, so names are in alphabetical order and print elements
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']
elements.sort()
print(elements)

# [x] print the list, numbers, sorted and then below print the original numbers list 
numbers = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
numbers_copy = []
for a in numbers:
    numbers_copy.append(a)
numbers.sort()
print(numbers)
print(numbers_copy)

# [x] split the string, daily_fact, into a list of word strings: fact_words
# [x] print each string in fact_words in upper case on it's own line
daily_fact = "Did you know that there are 1.4 billion students in the world?"
fact_words = daily_fact.split()
for a in fact_words:
    print(a)

# [x] convert the string, code_tip, into a list made from splitting on the letter "o"
code_tip = daily_fact.split("o")
print(code_tip)

# [x] split poem on "b" to create a list: poem_words
# [x] print poem_words by iterating the list
poem = "The bright brain, has bran!"
poem_words = poem.split("b")
for a in poem_words:
    print(a)

# [x] split the sentence, code_tip, into a words list
# [x] print the joined words in the list with no spaces in-between
# [x] Bonus: capitalize each word in the list before .join()
code_tip ="Read code aloud or explain the code step by step to a peer"
code_splat = code_tip.split()
code_cap = []
for a in code_splat:
    code_cap.append(a.capitalize())
#there is probably a faster method with title()
print(''.join(code_splat))
print(''.join(code_cap))

# [x] cast the long_word into individual letters list 
# [x] print each letter on a line
long_word = 'decelerating'
letters = list(long_word)
for a in long_word:
    print (a)

# [x] use use end= in print to output each string in questions with a "?" and on new lines
questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]
for a in questions:
    print (a, end ="? ")

# [x] print each item in foot bones 
#    - capitalized, both words if two word name
#    - separated by a comma and space
#    - and keeping on a single print line
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
for a in foot_bones:
    print (a.title(), end = ", ")


