# [x] extend the list common_birds with list birds_seen which you must create
common_birds = ["chicken", "blue jay", "crow", "pigeon"]
birds_seen = ["eagle", "parrot"]
birds = common_birds + birds_seen
print(birds)

# [x] Create 2 lists zero_nine and ten_onehundred that contain 1-9, and 10 - 100 by 10's.
# [x] use list addition to concatenate the lists into all_num and print
zero_nine = [0,1,2,3,4,5,6,7,8,9]
ten_onehundred = [10,20,30,40,50,60,70,80,90]
all_num = zero_nine + ten_onehundred
print(all_num)

# [x] create and  print a list of multiples of 5 from 5 to 100
# [x] reverse the list and print
multiple5 = list(range(5,101,5))
multiple5.reverse()
print(multiple5)

# [x] Create two lists: fours & more_fours containing multiples of four from 4 to 44
# [x] combine and print so that the output is mirrored [44, 40,...8, 4, 4, 8, ...40, 44]
fours = list(range(4,45,4))
print(fours)
more_fours = fours
fours.reverse()
more_fours += fours
print(more_fours)

# [x] print cites from visited_cities list in alphbetical order using .sort()
# [x] only print cities that names start "Q" or earlier
visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
visited_cities.sort()
print(visited_cities)

# [x] make a sorted copy (sorted_cities) of visited_cities list
# [x] remove city names 5 characters or less from sorted_cities 
# [x] print visitied cites and sorted cities
visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
visited_cities.sort()
sorted_cities = []
for a in range(0,len(visited_cities)):
    sorted_cities.append(visited_cities[a])
for a in sorted_cities:
    if len(a) <= 5:
        sorted_cities.remove(a)
print(visited_cities)
print(sorted_cities)

# [x] build a list (add_animals) using a while loop, stop adding when an empty string is entered
add_animals = []
animal = " "
while animal != "":
    animal = input("Enter the name of an animal : ")
    add_animals.append(animal)
add_animals.pop()
print (add_animals)

# [x] extend the lists into animals, then sort 
animals = ["Chimpanzee", "Panther", "Wolf", "Armadillo"]
animals = animals + add_animals
animals.sort()

# [x] get input if list should be viewed alpha or reverse alpha and display list
answer = input("do you want to see the list alpha or reverse (alpha/reverse) ? ")
if answer == "alpha":
    print(animals)
elif answer == "reverse":
    animals.reverse()
    print(animals)
else:
    print("Sorry, I didn't get your choice so i will assume you're a regular guy and you chose alpha, so here we go : ")
    print(animals)

