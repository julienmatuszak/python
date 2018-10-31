# [x] for x = 6, use range(x) to print the numbers 1 through 6
x = 6
for a in range(x+1):
    print(a)

# [x] using range(x) multiply the numbers 1 through 7
# 1x2x3x4x5x6x7 = 5040
x = 7
b = 1
for a in range(x):
    a = a+1
    b*= a
print (b)

# [x] print the second half of a spelling list using a range(stop) loop to iterate the list
spell_list = ["Wednesday", "Tuesday", "February", "November", "Annual", "Calendar", "Solstice"]

for a in range(int(len(spell_list)/2)):
    print(spell_list[a])

# [x] using range(start,stop), .append() the numbers 5 to 15 to the list: five_fifteen
# [x] print list five_fifteen
five_fifteen = []

for a in range(5,16):
    five_fifteen.append(a)
print (five_fifteen)

# [x] using code find the index of "Annual" in spell_list
# [x] using range, print the spell_list including "Annual" to end of list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
index = -1
for a in spell_list:
    while True:
        if a == "Annual":
            break
        else:
            index += 1
        break
    
for a in range(0,index):
    print(spell_list[a])

# [x] print numbers 10 to 20 by 2's using range
for a in range(10,21,2):
    print(a)

# [x] print numbers 20 to 10 using range (need to countdown)
# Hint: start at 20
b = 0
for a in range(20,31):
    print(a-2*b)
    b+=1

# [x] print first and every third word in spell_list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
for a in range(0,7,3):
    print (spell_list[a])

# [x] complete List of letters program- test with the word "complexity"
word = input("Gimme some string : ")
odd_letters = []
even_letters = []
for a in range(0,len(word),2):
    even_letters.append(word[a])
for a in range(1,len(word),2):
    odd_letters.append(word[a])
print(even_letters)
print(odd_letters)

# [x] fix the error printing odd numbers 1 - 9
for num in range(1,10,2):
    print(num)
