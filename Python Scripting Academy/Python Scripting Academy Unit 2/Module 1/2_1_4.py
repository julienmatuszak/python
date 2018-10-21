# [x] use len() to find the midpoint of the string 
# [x] print the halves on separate lines
random_tip = "wear a hat when it rains"
print(random_tip[:int(len(random_tip)/2)])
print(random_tip[int(len(random_tip)/2):])

# for letters: "e" and "a" in random_tip
# [x] print letter counts 
# [x] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains"
count_a = 0
count_e = 0
count_a = random_tip.count("a")
count_e = random_tip.count("e")
print("Number of a's : "+str(count_a))
print("Number of e's : "+str(count_e))
if count_a > count_e:
    print("There are more a's than e's")
elif count_e > count_a:
    print("There are more e's than a's")
else:
    print("There are as many a's than e's")

# [x] print long_word from the location of the first and second "t"
# not sure if I understood well: do we have to print from the first t to the second t or do we have to print twice, one from the first then one from the second t,
long_word = "juxtaposition"
print(long_word[long_word.find("t"):])
print(long_word[long_word[::-1].find("t",long_word.find("t")+1):])

# [x] Print each word in the quote on a new line  
quote = "they stumble who run fast"

start = 0
space_index = quote.find(" ")
while space_index != -1:
    print(quote[start:space_index])
    start = space_index+1
    space_index = quote.find(" ",space_index+1)
print(quote[start:len(quote)])        
