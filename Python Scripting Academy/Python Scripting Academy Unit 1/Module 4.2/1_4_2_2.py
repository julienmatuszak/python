# [x] Create the Animal Names program, run tests
all_animals = ""
num_animals = 0
while True:
    animal_name = input("Give me the name of an animal (press exit to leave) : ")
    if animal_name == "exit":
        if all_animals == "":
            print("no animals")
        break
    all_animals += animal_name+" "
    num_animals += 1
    if num_animals == 4:
        break
print (all_animals)

# [x] Create the program, run tests
int_num = "0"
long_num = ""
while int_num.isdigit() is True:
    int_num = input("Enter a digit : ")
    long_num += int_num
    if long_num == "":
        print("no digits")
        break
print(long_num)
    
# [x] review the code, run, fix the Logic error
count = 1

# loop 5 times
while count < 6:
    print(count, "x", count, "=", count*count)
    count +=1
    