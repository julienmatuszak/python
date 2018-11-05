# [x] Write an expression to raise a `SyntaxError` exception
print a

# [x] Write an expression to raise a `TypeError` exception
a = 1+"1"

## [x] The following program divides the elements of `lst` by a float number `x` specified by the user
# Use exception handling to correct for the ALL generated exceptions
# When you handle all exceptions correctly, you should see the word "Done!" in the program output
# HINT: You might need to use 2 `try..except` statements
# Test cases:
# x = 5
# x = 6.3
# x = "number"
# x = 0
lst = [8, 85.4, [55, 4], 'word', (59,), {2:43.5}]
try:
    x = input("Enter a number: ")
    x = float(x)
except ValueError as exception:
    print(exception)
else:
    try:
        for i in range(7):
            print("{} / {:.2f} = {:.2f}".format(lst[i], x, lst[i] / x))
    except ZeroDivisionError as exception:
        print(exception)
print("Done!") 

# [x] The following program asks the user for a file name.
# The file is then opened, the first line printed out, then closed.

# Use exception handling to show the user a message confirming the file process was completed successfully
# your exception handling should also deal with the cases when the file does not exist

# test cases:
# fname = text_file.txt (should display: File process was completed successfully)
# fname = nofilehere.txt (should display: nofilehere.txt was not found)
import os
# ask user for a file name
try:
    fname = input("Enter file name: ")
except FileNotFoundError as exception:
    print(exception)
else:   
# the file should be located in `parent_dir`
    fname = os.path.join("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3", fname)
# opening text_file.txt for reading
    try:
        f = open(fname, 'r')
    except FileNotFoundError as exception:
        print(exception)
        print("No",fname,"was found")
    except IsADirectoryError as exception:
        print(exception)
        print(fname,"is a directory! You should enter the name of a file")
    else:
        f = open(fname, 'r')
        print(f.readline())
        f.close()
        print("File process was completed successfully")

# [x] The following program tries to read from a file opened for writing.
# The program will terminate before closing the file, and the file resources will not be released.
# Use exception handling with a `finally` to make sure the file is closed
# Open a text file for writing
try:
    f = open("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/text_file_2.txt", 'w')
# trying to read from a file open for writing (will raise an exception)
    print(f.readline())
# closing the file (will not be reached if an exception was raised)
finally:
    f.close()
    print("File closed")

## [x] Write a program to keep prompting the user for a number from a predefined numerical tuple `valid_nums`
# Your program should raise an exception with an appropriate message if the input is not valid
valid_nums = (1, 2, 8, 16, 32, 64)
try:
    num = int(input("Guess a number in the list : "))
except ValueError as exception:
    print(exception)
else:
    try:
        while num not in valid_nums:
            num = int(input("Guess a number in the list : "))
    except ValueError as exception:
        print(exception)
    else:
        print("Congratulations! You found the number !")

# Do not modify or add anything to this code segment.
# This code segment must be run before attempting any of the tasks in this lesson.
# It prepares the directories and files necessary to complete the tasks.
import os, random, shutil
# Navigate to `parent_dir` directory (if not already in it)
current_path = os.getcwd()
if ("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3" in current_path):
    nb_path = current_path.split("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3")[0]
else:
    nb_path = current_path
print("Changing working dir to parent_dir")
os.chdir(os.path.join(nb_path,'/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3'))
print("Current working directory:", os.getcwd())
# Remove the `files_exercises` directory (if it exists)
if('files_exercises' in os.listdir()):
    print('Removing "files_exercises"')
    shutil.rmtree('files_exercises') 
# Create a new directory called `files_exercises`
print('Making "files_exercises"')
os.mkdir('files_exercises')
# Change the working directory to `files_exercises`
print('Changing working directory to "files_exercises"')
os.chdir('files_exercises')
# Display the current working directory to verify you are in the correct location
print("Current working directory:", os.getcwd())
# Create 100 text files, the first line of each file is a random number in the range [1000, 9999]
print("Creating 100 text files")
random.seed(25000) # to get the same random numbers every time the setup runs
for i in range(100):
    file_name = str(i) + ".txt"
    f = open(file_name, 'w')
    f.write(str(random.randint(1000, 9999)))
    f.close()
# Create 5 directories
print("Creating 5 directories")
for i in range(1, 6):
    os.mkdir("dir_"+str(i))
print("Environment setup completed!")

# [x] Complete the function `delete_files` so the program deletes all the files in the `files_exercises` directory
# Make sure the to run the environment setup code before running your own program.
import os
os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises")
if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")
for a in range(100):
    os.remove(str(a)+".txt")
for a in range(1,6):
    os.rmdir("dir_"+str(a))
print("Environment setup completed!")

# [x] The following program is designed to remove all files in `files_exercises` that contain a number divisible by 3 on the first line.
# To complete the program, you need to:
# 1) complete the function `delete_files` as you did in a previous exercise
# 2) iterate over all content in `file_exercises`:
#    2.1) if an element in the directory is a file open it for reading using `with` statement
#    2.2) read the first line in the file
#    2.3) if the first line contains a number divisible by 3, add the file name to the `to_be_deleted` list
#    2.4) your code should handle exception appropriately (i.e. a blank file or a file containing a string in the first line)
# 3) make sure the to run the environment setup code before running your own program.

# The output of your program should look like:
'''
Unexpected error found in 49.txt: invalid literal for int() with base 10: ''
Deleting matching files:
------------------------------
Removing 15.txt
Removing 16.txt
Removing 18.txt
Removing 19.txt
Removing 20.txt
Removing 23.txt
Removing 28.txt
Removing 35.txt
Removing 39.txt
Removing 40.txt
Removing 44.txt
Removing 46.txt
Removing 5.txt
Removing 51.txt
Removing 52.txt
Removing 54.txt
Removing 55.txt
Removing 58.txt
Removing 59.txt
Removing 65.txt
Removing 67.txt
Removing 68.txt
Removing 69.txt
Removing 71.txt
Removing 73.txt
Removing 77.txt
Removing 80.txt
Removing 81.txt
Removing 85.txt
Removing 87.txt
Removing 91.txt
Removing 94.txt
Removing 95.txt
Removing 96.txt
'''
import os
def delete_files(to_be_deleted):
    """
    Remove all the files listed in `to_be_deleted` and leave the directories.
    
    args:
        to_be_deleted: list of paths
    
    returns:
        None
    """
    for a in to_be_deleted:
        try:
            os.remove(str(a)+".txt")
        except FileNotFoundError as exception:
            print(a+".txt",exception)
        else:
            print("Removing "+a+".txt")
os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises")
if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")
   
# list the content of `files_exercises`
print('Content of "files_exercises" before removing the files')
print(os.listdir()) 
print(30 * "-")
# clearing (49.txt) so an exception is raised below as a result of int( )
# opening a file without doing anything clears it!
with open('49.txt', 'w') as file: pass
to_be_deleted = []
#TODO: iterate over directory content and store file names containing numbers divisible by 3 in `to_be_deleted` list
for a in os.listdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises"):
    if (a[-3:]) == "txt":
        try:
            f = open(a,"r")
            line = f.readline()
            int(line)
        except ValueError as exception:
            print("Unexpected error found in",a,exception)
        else:
            if int(line) %3 == 0:
                to_be_deleted.append(a[:-4])
        finally:
            f.close()
print()
print("Deleting matching files:")
print(30 * "-")
delete_files(to_be_deleted)

# [x] Write a program to:
# 1) ask the user for a number between 1000 and 9999
# 2) test if the number matches the first line of any file in `files_directory`
# 3) if a match was found, print the file name; otherwise, print no match is found
# 4) your code should handle exception appropriately (i.e. a blank file or a file containing a string in the first line)
# 5) you should use `with` statement for opening/closing files
# 6) make sure the to run the environment setup code before running your own program.
# test cases:
# 3932, should print out: Match found in 74.txt : 3932
# 2177, should print out: Match found in 27.txt : 2177
# 4932, should print out: No matching files found
import os
os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises")
if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")
c = True
num = input("What number are you looking for ? ")
for a in os.listdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises"):
    for b in range(len(os.listdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises"))):
            if (a[-3:]) == "txt":
                with open(a,"r") as f:
                    try:
                        line = f.readline()
                    except ValueError as exception:
                        print("Unexpected error found in",a,exception)
                    else:
                        if not line.isdigit():
                            print("File",a,"does not contain a digit number only !")
                        elif line == "":
                            print("File",a,"is blank !")
                        else:
                            if line == num:
                                c = False
                                print("Match found in",a,":",num)
                                break
if (c):
    print("No matching files found")

# [x] The tuples `x` and `y` contain the (x, y) coordinates of 10 points.
# Write a program to create a single tuple `coordinates` that contains 10 sub-tuples of the (x, y) coordinates
# The final tuple should look like:
# ((75, 57), (77, 6), (55, 64), (93, 36), (41, 63), (62, 53), (70, 26), (30, 71), (74, 88), (97, 66))
x = (75, 77, 55, 93, 41, 62, 70, 30, 74, 97)
y = (57, 6, 64, 36, 63, 53, 26, 71, 88, 66)
z=()
for a in range(10):
    z += (x[a],y[a]),
print (z)

# [x] Write a program to merge the two sorted tuples T1, T2 into a larger (also sorted) tuple T
# Output should be:
#Merged sorted tuple:
#(12, 13, 15, 20, 20, 26, 30, 37, 40, 55, 60, 68, 72, 78, 81, 84, 89, 97, 97, 100)
# sorted tuples
T1 = (15, 20, 30, 37, 55, 60, 78, 81, 84, 100)
T2 = (12, 13, 20, 26, 40, 68, 72, 89, 97, 97)
print(tuple(sorted(list(T1)+list(T2))))

# [x] Complete the function `simple_stats` so it returns:
# 1) The maximum number in the tuple T
# 2) The minimum number in the tuple T
# 3) The average of the numbers in the tuple T
def simple_stats(T):
    return max(T),min(T),sum(T)/len(T) 
T = (257, 462, 18, 369, 415, 994, 541, 752, 78, 895, 0, 576, 40, 552, 438, 605, 54, 296, 433, 986, 685, 651, 523, 855, 777, 437, 65, 360, 265, 858, 260, 819, 586, 358, 860, 250, 531, 7, 801, 259, 155, 376, 374, 828, 475, 62, 52, 184, 186, 283, 643, 86, 472, 267, 692, 750, 948, 683, 452, 770, 322, 492, 871, 360, 88, 883, 764, 288, 383, 411, 679, 90, 857, 802, 974, 403, 798, 990, 475, 260, 289, 438, 873, 779, 895, 939, 462, 469, 183, 520, 366, 267, 896, 732, 303, 754, 195, 949, 546, 180)
# unpacking and displaying the returned values
largest, smallest, average = simple_stats(T)
print("Maximum number in T:", largest)
print("Minimum number in T:", smallest)
print("Average of numbers in T:", average)

# [x] Complete the function `longer` to compare and return the longest of 2 tuples

def longer(T1, T2):
    """
    Return the longer of two tuples 
    args:
        T1: tuple of arbitrary length
        T2: tuple of arbitrary length     
    returns:
        T1: if T1 is longer than T2
        T2: if T2 is longer or the same length as T1
    """
    if len(T1) > len(T2):
        return "T1"
    elif len(T1) < len(T2):
        return "T2"
    else:
        return "None"  
T1 = (98, 84, 71, 87, 54, 16, 70, 62, 1, 29, 66, 1, 74, 71, 68, 58, 65, 75, 74, 77, 94, 19, 46)
T2 = (62, 30, 58, 75, 0, 61, 37, 93, 40, 33, 93, 94, 72, 27, 92, 75, 38, 70, 99, 74, 89, 8, 42, 32, 4, 60, 5)
print("The longer tuple is:", end = " ")
print(longer(T1, T2))

# [x] Complete the function `search` so it looks for the first instance of `num` in `T`
# The function should return 2 values:
# 1) Boolean value indicating if num was found or not
# 2) Index of the first instance of `num` in `T`

def search(T, num):
    """
    Search T for num and return the index if found; otherwise return None.
    
    args:
        T: Tuple to be searched
        num: number to use for the search
        
    returns:
        found: Boolean value to indicate if the num is contained in T or not
        i: If num is found in T return index of the first instance of num in T; otherwise, return the value `None`
    """
    count = 0
    for a in T:
        count += 1
        if a == num:
            return True, count
            break
    return False, None


T = (257, 462, 18, 369, 415, 994, 541, 752, 78, 895, 0, 576, 40, 552, 438, 605, 54, 296, 433, 986, 685, 651, 523, 855, 777, 437, 65, 360, 265, 858, 260, 819, 586, 358, 860, 250, 531, 7, 801, 259, 155, 376, 374, 828, 475, 62, 52, 184, 186, 283, 643, 86, 472, 267, 692, 750, 948, 683, 452, 770, 322, 492, 871, 360, 88, 883, 764, 288, 383, 411, 679, 90, 857, 802, 974, 403, 798, 990, 475, 260, 289, 438, 873, 779, 895, 939, 462, 469, 183, 520, 366, 267, 896, 732, 303, 754, 195, 949, 546, 180)
x = int(input("Enter a number to search for in T: "))
# unpacking returned tuple
found, i = search(T, x)
if found:
    print("First instance found at index {:}".format(i))
else:
    print("{} was not found in T".format(x))
    
# [x] Complete the functions `search` and `split` to slice a tuple `T` around a number `num`
# The function should use the `search` function you developed in a previous exercise to find its index in `T`
# If `num` is in T, you discard it and return two tuples:
#   1) from the beginning of T till index of num
#   2) from index+1 of num till the end of T
# If `num` is not in T, you return:
#   1) The whole Tuple 
#   2) The `None` value

# Example input/output using T = (15, 20, 30, 37, 55, 60, 78, 81, 84, 100):

#Enter a number around which you want to split T: 55
#T1 = (15, 20, 30, 37)
#T2 = (60, 78, 81, 84, 100)

#Enter a number to search for in T: 400
#T1 = (15, 20, 30, 37, 55, 60, 78, 81, 84, 100)
#T2 = None


def search(T, num):
    """
    Search T for num and return the index if found; otherwise return None.
    
    args:
        T: Tuple to be searched
        num: number to use for the search
        
    returns:
        found: Boolean value to indicate if the num is contained in T or not
        i: If num is found in T return index of the first instance of num in T; otherwise, return the value `None`
    """
    count = 0
    for a in T:
        count += 1
        if a == num:
            return True, count
            break
    return False, None
def split(T, num):
    """
    Split the tuple T around num (num should be discarded).
    
    args:
        T: Tuple to be searched
        num: number to use for the split
    
    returns:
        T1: The first half of the tuple, from the beginning till num ( excluded).
            If num is not in T, T1 should be the whole tuple T
        T2: The second half of the tuple, from num (excluded) till the end.
            If num is not in T, T2 should be the value `None`
    """
    a,x = search(T,num)
    T1 = ()
    T2 = ()
    if (a):
        for b in range(0,x-1):
            T1 += T[b],
        for b in range(x,len(T)):
            T2 += T[b],
        return T1,T2
    else:
        return T,None
T = (15, 20, 30, 37, 55, 60, 78, 81, 84, 100)
x = int(input("Enter a number around which you want to split T: "))
# unpacking returned tuple
T1, T2 = split(T, x)
print("T1 =", T1)
print("T2 =", T2)

# [x] The `data` list contains grocery store inventory information, the list is organized into sublists where each of
# the sublists contains: [UPC, Description, Unit Price, Quantity in Stock]
# Use the `data` list to create an inventory dictionary with the UPC as keys and lists containing [Description, Item Price, Quantity in Stock] as values:
# UPC (as keys): [Description, Unit Price, Quantity in Stock] (as values)
# NOTE: UPC is short for (Universal Product Code), which is the number found under a barcode and identify different products in a store
# The created dictionary should look like:
# {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}
data = [[847502, "APPLES 1LB", 1.99, 50], [847283, "OLIVE OIL", 10.99, 100], [839529, "TOMATOS 1LB", 1.29, 25], [483946, "MILK 1/2G", 3.45, 35], [493402, "FLOUR 5LB", 2.99, 40], [485034, "BELL PEPPERS 1LB", 1.35, 28], [828391, "WHITE TUNA", 1.69, 100], [449023, "CHEESE 1/2LB", 4.99, 15]]
dictionary = {}
for a in data:
    dictionary[a[0]] = [a[1],a[2],a[3]]
print(dictionary)

# [x] Use the `inventory` dictionary in a program that asks the user for a UPC number then prints the item information
# Your program should print an appropriate message if the UPC is not in the inventory
# test cases:
# input 1: 847283
# output:
'''
  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
847283  | OLIVE OIL         |        10.99 |     100.00
'''
# input 2: 340344
# output: No inventory found for 340344
inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}
num = int(input("Please enter a valid UPC number : "))
for a in inventory.keys():
    if a == num:
        print("{:^9s}| {:<18s}|{:^13s}| {:^10s}".format("UPC","Description","Unit Price", "Quantity"))
        print("-------------------------------------------------------")
        print("{:<9d}| {:<18s}|{:>12.2f} |{:>11.2f}".format(a, inventory[a][0], inventory[a][1], inventory[a][2]))
        break
else:
    print("No inventory found for",num)

# [x] Use the `inventory` dictionary in a program that asks the user for a UPC number, description, unit price, 
# quantity in stock.
# If the item already exists in the inventory, the information is updated, 
# and your program should display a message that it is updating the entry.
# If the item does NOT exists in the inventory, a new dictionary entry is created, 
# and your program should display a message that it is creating a new entry.
# Use try/except in the program.
# test cases
# For an existing item
'''
Enter UPC number: 839529
Enter item description: TOMATOS 1LB
Enter unit price: 1.55
Enter item quantity: 21
Existing item, updating: ['TOMATOS 1LB', 1.29, 25]
  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
839529  | TOMATOS 1LB       |         1.55 |      21.00
'''
# For a new item
'''
Enter UPC number: 29430
Enter item description: ORANGE 1LB
Enter unit price: 0.99
Enter item quantity: 40
New item, creating ORANGE 1LB
  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
29430   | ORANGE 1LB        |         0.99 |      40.00
'''
inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}
num = 0
description = ""
unit_price = 0
item_quantity = 0
while num == 0:
    try:
        num = int(input("Enter UPC number: "))
    except ValueError as exception:
        print(exception)
while description == "":
    description = input("Enter item description: ")          
while unit_price == 0:
    try:
        unit_price = float(input("Enter unit price: "))
    except ValueError as exception:
        print(exception)
while item_quantity == 0:
    try:
        item_quantity = float(input("Enter item quantity: "))
    except ValueError as exception:
        print(exception)
if num not in inventory.keys():
    print("New item, creating {:s}".format(description))
    inventory.update({num:[description, unit_price, item_quantity]})
if num in inventory.keys():
    print("Existing item, updating: {:s}".format(str(inventory[num])))
    inventory[num] = [description,unit_price,item_quantity]
print()
print("{:^9s}| {:<18s}|{:^13s}| {:^10s}".format("UPC","Description","Unit Price", "Quantity"))
print("-------------------------------------------------------")
print("{:<9d}| {:<18s}|{:>12.2f} |{:>11.2f}".format(num, inventory[num][0], inventory[num][1], inventory[num][2]))

# [x] Write a program to display the current inventory information as follow
# Note the items are sorted by UPC
'''
  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
449023  | CHEESE 1/2LB      |         4.99 |      15.00
483946  | MILK 1/2G         |         3.45 |      35.00
485034  | BELL PEPPERS 1LB  |         1.35 |      28.00
493402  | FLOUR 5LB         |         2.99 |      40.00
828391  | WHITE TUNA        |         1.69 |     100.00
839529  | TOMATOS 1LB       |         1.29 |      25.00
847283  | OLIVE OIL         |        10.99 |     100.00
847502  | APPLES 1LB        |         1.99 |      50.00
'''
inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}
print("{:^8s}| {:<18s}|{:^14s}|{:^12s}".format("UPC","Description","Unit Price","Quantity"))
print("-------------------------------------------------------")
for item in sorted(inventory.keys()):
    print("{:<8d}| {:<18s}|{:>13.2f} |{:>11.2f}".format(item, inventory[item][0], inventory[item][1], inventory[item][2]))

# [x] Write a program to calculate and display the total value and the number of items in an inventory.
# The total value can by calculated by multiplying each unit price by the quantity, 
# then adding up the answers for all items in the inventory.
inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}
total = 0
print("{:^8s}| {:<18s}|{:^14s}|{:^12s}|{:^12s}".format("UPC","Description","Unit Price","Quantity","Total"))
print("--------------------------------------------------------------------")
for item in inventory.keys():
    total += inventory[item][1]*inventory[item][2]
    print("{:<8d}| {:<18s}|{:>13.2f} |{:>11.2f} |{:>10.2f}".format(item, inventory[item][0], inventory[item][1], inventory[item][2], inventory[item][1]*inventory[item][2]))
print()
print("{:>56s} {:>10.2f}".format("TOTAL",total))

# [x] In this project, you will read a CSV file containing about 25K lines of weather information 
# and store the information in a Python dictionary. You will then use the dictionary to find out
# the hottest, coldest, rainiest years and so on...
# You will see that the dictionary's search optimization algorithms will allow you to explore 
# this large dataset without any noticeable delays.
# The logic of the program is in the `main` function, read it before writing any code.
# Use the description and examples under each of the following functions to implement them:
# 1) convert_file(file_path)
# 2) add_rainy(weather)
# 3) consolidate(weather)
# 4) year_info(year, yearly_weather)
# 5) hottest(yearly_weather)
# 6) coldest(yearly_weather)
# 7) rainiest_days(yearly_weather)
# 8) highest_prcp(yearly_weather)
from datetime import date, datetime
from IPython.display import clear_output #to clear the output (specific to Jupyter notebooks and ipython)
import os
def convert_file(file_path):
    """
    Convert CSV file to a Python dictionary.
    
    The CSV file contains daily weather information arranged in rows,
    the rows contain  (date, precipitation (inches), maximum temperature (F), minimum temperature (F)) in order.
    First line in CSV file is a header (DATE, PRCP, TMAX, TMIN), the rest contain the weather data.   
    The function should read the data in the file and generate a dictionary where:
        1) keys are date objects (from the datetime module), using the daily date info in the file
        2) values are lists containing [TMAX, TMIN, PRCP] in order      
    args:
        file_path: path to the CSV file    
    returns:
        weather: the generated dictionary using date objects as keys and lists of weather info as values        
    examples:
    Input CSV file:
    DATE,PRCP,TMAX,TMIN
    12/10/2017,0,49,34
    12/11/2017,0,49,29
    12/12/2017,0,46,32
    12/13/2017,0,48,34
    12/14/2017,0,50,36
    12/15/2017,0.06,43,37
    12/16/2017,0.14,45,37
    12/17/2017,0.03,50,42
    12/18/2017,0.7,49,41
    12/19/2017,1,50,40
    12/20/2017,0.13,49,32
    12/21/2017,0.01,41,29
    12/22/2017,0.09,40,35
    12/23/2017,0,38,29
    12/24/2017,0.12,38,28
    Output dictionary (weather):
    {datetime.date(2017, 12, 10): [49, 34, 0.0],
     datetime.date(2017, 12, 11): [49, 29, 0.0],
     datetime.date(2017, 12, 12): [46, 32, 0.0],
     datetime.date(2017, 12, 13): [48, 34, 0.0],
     datetime.date(2017, 12, 14): [50, 36, 0.0],
     datetime.date(2017, 12, 15): [43, 37, 0.06],
     datetime.date(2017, 12, 16): [45, 37, 0.14],
     datetime.date(2017, 12, 17): [50, 42, 0.03],
     datetime.date(2017, 12, 18): [49, 41, 0.7],
     datetime.date(2017, 12, 19): [50, 40, 1.0],
     datetime.date(2017, 12, 20): [49, 32, 0.13],
     datetime.date(2017, 12, 21): [41, 29, 0.01],
     datetime.date(2017, 12, 22): [40, 35, 0.09],
     datetime.date(2017, 12, 23): [38, 29, 0.0],
     datetime.date(2017, 12, 24): [38, 28, 0.12]}
    """
    os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/")
    if (file_path not in os.listdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/")):
        print("STOP!!!! Run the environment setup code!")
        return None
    else:
        weather = {}
        with open(file_path, 'r') as f:
            skip = f.readline()
            for a in range(0,25561):
                u = f.readline()
                u = u.rstrip()
                u = u.split(",")
                c = date_creater(u[0])
                if u[1] == "":
                    u[1] = 0
                if u[2] == "":
                    u[2] = 0
                if u[3] == "":
                    u[3] = 0
                weather[c] = [int(u[2]),int(u[3]),float(u[1])]
        return weather   
    #[x] open the file for reading (HINT: use `with` statement)
    #[x] ignore the first header line (DATE, PRCP, TMAX, TMIN)
    #[x] remove newline characters from end of each line (HINT: use str.rstrip())
    #[x] split line into a list (HINT: use str.split(','))
    #[x] create the date object from the first list element 
    # HINT: use the date_creater(date_string) function provided below
    #[x] read the weather related variables
    # precipitation
    # maximum temperature
    # minimum temperature   
    #[x] create dictionary key:value pair
def add_rainy(weather):
    """
    Emphasize rainy days using Boolean values.    
    Modify the weather dictionary by adding another Boolean element to the values' lists. 
    If precipitation is observed on a day (more than 0"), the associated list is appended by True.
    If precipitation is not observed (0"), the associated list is appended by False.   
    args:
        weather: dictionary, keys are date objects and values are lists [TMAX, TMIN, PRCP]        
    returns:
        None: the weather dictionary is modified directly, keys are date objects and values are lists [TMAX, TMIN, PRCP, RAINY_DAY]        
    examples:
    Input weather dictionary:
    {datetime.date(2017, 12, 10): [49, 34, 0.0],
     datetime.date(2017, 12, 11): [49, 29, 0.0],
     datetime.date(2017, 12, 12): [46, 32, 0.0],
     datetime.date(2017, 12, 13): [48, 34, 0.0],
     datetime.date(2017, 12, 14): [50, 36, 0.0],
     datetime.date(2017, 12, 15): [43, 37, 0.06],
     datetime.date(2017, 12, 16): [45, 37, 0.14],
     datetime.date(2017, 12, 17): [50, 42, 0.03],
     datetime.date(2017, 12, 18): [49, 41, 0.7],
     datetime.date(2017, 12, 19): [50, 40, 1.0],
     datetime.date(2017, 12, 20): [49, 32, 0.13],
     datetime.date(2017, 12, 21): [41, 29, 0.01],
     datetime.date(2017, 12, 22): [40, 35, 0.09],
     datetime.date(2017, 12, 23): [38, 29, 0.0],
     datetime.date(2017, 12, 24): [38, 28, 0.12]}    
    Updated weather dictionary with Boolean values
    {datetime.date(2017, 12, 10): [49, 34, 0.0, False],
     datetime.date(2017, 12, 11): [49, 29, 0.0, False],
     datetime.date(2017, 12, 12): [46, 32, 0.0, False],
     datetime.date(2017, 12, 13): [48, 34, 0.0, False],
     datetime.date(2017, 12, 14): [50, 36, 0.0, False],
     datetime.date(2017, 12, 15): [43, 37, 0.06, True],
     datetime.date(2017, 12, 16): [45, 37, 0.14, True],
     datetime.date(2017, 12, 17): [50, 42, 0.03, True],
     datetime.date(2017, 12, 18): [49, 41, 0.7, True],
     datetime.date(2017, 12, 19): [50, 40, 1.0, True],
     datetime.date(2017, 12, 20): [49, 32, 0.13, True],
     datetime.date(2017, 12, 21): [41, 29, 0.01, True],
     datetime.date(2017, 12, 22): [40, 35, 0.09, True],
     datetime.date(2017, 12, 23): [38, 29, 0.0, False],
     datetime.date(2017, 12, 24): [38, 28, 0.12, True]}
    """
    for a in weather.keys():
        if weather[a][2] > 0:
            weather[a].append(True)
        else:
            weather[a].append(False)
def consolidate(weather):
    """
    Consolidate the daily weather information by year.    
    Use the weather dictionary to generate a new consolidated dictionary (yearly_weather). 
    The new dictionary uses years as keys, and the associated values are lists containing (in order):
        1) The average of the highest recorded temperatures in the year (AVG_TMAX)
        2) The average of the lowest recorded temperatures in the year (AVG_TMIN)
        3) The total recorded precipitation in the year (TOTAL_PRCP)
        4) The total number of rainy days in the year (TOTAL_RAINY_DAYS)
        5) The number of recorded days (TOTAL_DAYS). 
           This element is necessary to account for days where the station breaks (missing recordings),
           or if the year hasn't finished yet.         
    args: 
        weather: dictionary, keys are date objects and values are lists [TMAX, TMIN, PRCP, RAINY_DAY]   
    returns:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]                       
    examples:
    Input weather dictionary:
    {datetime.date(2017, 12, 10): [49, 34, 0.0, False],
     datetime.date(2017, 12, 11): [49, 29, 0.0, False],
     datetime.date(2017, 12, 12): [46, 32, 0.0, False],
     datetime.date(2017, 12, 13): [48, 34, 0.0, False],
     datetime.date(2017, 12, 14): [50, 36, 0.0, False],
     datetime.date(2017, 12, 15): [43, 37, 0.06, True],
     datetime.date(2017, 12, 16): [45, 37, 0.14, True],
     datetime.date(2017, 12, 17): [50, 42, 0.03, True],
     datetime.date(2017, 12, 18): [49, 41, 0.7, True],
     datetime.date(2017, 12, 19): [50, 40, 1.0, True],
     datetime.date(2017, 12, 20): [49, 32, 0.13, True],
     datetime.date(2017, 12, 21): [41, 29, 0.01, True],
     datetime.date(2017, 12, 22): [40, 35, 0.09, True],
     datetime.date(2017, 12, 23): [38, 29, 0.0, False],
     datetime.date(2017, 12, 24): [38, 28, 0.12, True]}     
     Output yearly_weather dictionary:
     {2017: [45.666666666666664, 34.333333333333336, 2.28, 9, 15]}
    """    
    yearly_weather = {}
    for a in range(1948,2018):
        total_days = 0
        rainy_days = 0
        total_prec = 0
        total_max = 0
        total_min = 0
        for b in weather.keys():
            if b.year == a:
                total_days += 1
                total_prec += weather[b][2]
                total_max += weather[b][0]
                total_min += weather[b][1]
                if weather[b][3] == True:
                    rainy_days += 1
        yearly_weather.update({a:[total_max/total_days, total_min/total_days, total_prec, rainy_days, total_days]})
    return yearly_weather
def year_info(year, yearly_weather):
    """
    Convert the year's weather information to a formatted string.   
    Look for the weather information of `year` in the `yearly_weather` dictionary.
    If it exists, convert the information list into a formatted string:
            YEAR | AVG_TMAX | AVG_TMIN | TOTAL_PRCP | TOTAL_RAINY_DAYS | TOTAL_DAYS
    If it does not exist, the formatted string should be:
            N/A  |    N/A   |    N/A   |     N/A    |        N/A       |    N/A       
    args:
        year: int value to look for in the yearly_weather dictionary       
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]    
    returns:
        formatted_string: containing the year's weather information                        
    examples:
    Input yearly weather dictionary:
    {2017: [45.666666666666664, 34.333333333333336, 2.28, 9, 15]}  
    Output formatted string:
    == year_info(2017, yearly_weather) == (contained in the dictionary)
    ' 2017 |         45.67 |        34.33 |   2.28" |            9 |             15 '
    
    == year_info(2055, yearly_weather) == (not contained in the dictionary)
    ' N/A  |      N/A      |     N/A      |   N/A   |     N/A      |      N/A       '
    """
    if year in yearly_weather.keys():
        return "{:>10s} | {:s} | {:s} | {:s} | {:s} | {:s}".format("YEAR","AVG_TMAX","AVG_TMIN","TOTAL_PRCP","TOTAL_RAINY_DAYS","TOTAL_DAYS")+"\n"+"{:>10d} | {:^8.5f} | {:^8.5f} | {:^10.2f} | {:^16d} | {:^10d}".format(year,yearly_weather[year][0],yearly_weather[year][1],yearly_weather[year][2],yearly_weather[year][3],yearly_weather[year][4])+"\n"          
    if year not in yearly_weather.keys():
        return "{:>10s} | {:s} | {:s} | {:s} | {:s} | {:s}".format("YEAR","AVG_TMAX","AVG_TMIN","TOTAL_PRCP","TOTAL_RAINY_DAYS","TOTAL_DAYS")+"\n"+"{:>10s} | {:^8s} | {:^8s} | {:^10s} | {:^16s} | {:^10s}".format("N/A","N/A","N/A","N/A","N/A","N/A")+"\n"
def hottest(yearly_weather):
    """
    Find the hottest year in yearly_weather.    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the highest average maximum temperature (highest AVG_TMAX)
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]     
    returns:
        hottest_year: the year with the highest maximum temperature average (AVG_TMAX)
    """
    return(max(yearly_weather))       
def coldest(yearly_weather):
    """
    Find the coldest year in yearly_weather.   
    Look through all the years in the yearly_weather dictionary and return the year with 
    the lowest average minimum temperature (lowest AVG_TMIN)
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] 
    
    returns:
        coldest_year: the year with the lowest minimum temperature average (AVG_TMIN)
    """
    return(min(yearly_weather))
def rainiest_days(yearly_weather):
    """
    Find the year with the largest number of rainy days in yearly_weather.
    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the largest TOTAL_RAINY_DAYS    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]     
    returns:
        rainiest_year: the year with the largest number of rainy days
    """
    total_rainy_max = 0
    for a in yearly_weather.keys():
        if yearly_weather[a][3] >= total_rainy_max:
            total_rainy_max = yearly_weather[a][3]
            year = a
    return(year)
def highest_prcp(yearly_weather):
    """
    Find the year with the highest total precipitation in yearly_weather.
    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the largest TOTAL_PRCP
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] 
    
    returns:
        rainiest_year: the year with the highest total precipitation
    """
    total_prec_max = 0
    for a in yearly_weather.keys():
        if yearly_weather[a][2] >= total_prec_max:
            total_prec_max = yearly_weather[a][2]
            year = a
    return(year)
def date_creater(date_string):
    """Convert the date_string (formatted as m/d/yyyy) to a date object."""
    date_string = date_string.split("/")
    if len(date_string[0]) == 1:
        a = "0"+date_string[0]
        date_string[0] = a
    if len(date_string[1]) == 1:
        b = "0"+date_string[1]
        date_string[1] = b
    if int(date_string[2]) >= 48 and int(date_string[2]) <= 99:
        c = "19"+date_string[2]
    if int(date_string[2]) >0 and int(date_string[2]) < 18:
        c = "20"+date_string[2]
    if date_string[2] == "00":
        c = "2000"
    date_string[2] = c
    date_string = "/".join(date_string)
    d = datetime.strptime(date_string, "%m/%d/%Y")
    return d.date()
def dashes(count):
    """Print a fancy line of `count` dashes"""
    print("o" + count *'-' + "o")
def page_header(title):
    """Print a page header with a title surrounded by dashes"""
    dashes(78)
    print("|{:^78s}|".format(title))
    dashes(78)
def table_header():
    """Print the first row in a table  (header row)"""
    print()
    print(' {0:^4s} | {1:^13s} | {2:^12s} | {3:^7s} | {4:^12s} | {5:^14s} '.format("Year", "Avg High Temp", "Avg Low Temp", "Precip", "# Rainy days", "# Recorded days"))
    dashes(78)    
def display(title, years, yearly_weather):
    """Print a page with a header, title, and the weather information of all years as found in yearly_weather"""
    clear_output()
    page_header(title)
    table_header()   
    # if years contain a single int, convert to a single item list
    if type(years) is not list: years = [years]    
    # print weather information for all years
    for year in years:
        print(year_info(year, yearly_weather))         
    # display this page till you go back to the main menu
    while True:
        m = input("Return to main menu [y/n]?")
        if m in 'yesYesYES':
            break     
def main():
    # convert the data in the (csv) file into a Python dictionary
    weather = convert_file("seattle_weather.csv")   
    # highlight rainy days by adding a Boolean entry to the dictionary's values
    add_rainy(weather)   
    # consolidate the weather data by year then store the result in a new dictionary
    yearly_weather = consolidate(weather)
    # earliest and latest years on record
    min_year = min(yearly_weather)
    max_year = max(yearly_weather)
    # menus functionality
    while True:
        clear_output()
        # display header
        page_header("Weather Records")
        # display main menu
        print()
        print("Main Menu (choose an option to display):\n")
        print("1. Summary of a certain year")
        print("2. All years summary table")
        print("3. Hottest year on record")
        print("4. Coldest year on record")
        print("5. Year with most rainy days")
        print("6. Year with the highest precipitation")
        print("7. Quit")
        print()
        # display footer with user input message
        dashes(78)
        while True:
            try:
                option = input("Select an option (1, 7): ")
                option = int(option)
                if 1 <= option <= 7:
                    break # break the user input loop only, main loop does NOT break
            except ValueError:
                print("Cannot convert {:} to int".format(type(option)))       
        # execute relevant function
        # 1. Summary of a certain year
        if option == 1:
            # ask the user for a valid year
            while True:
                try:
                    year = input("Enter a year ({} - {})".format(min_year, max_year))
                    year = int(year)
                    if min_year <= year <= max_year:
                        break
                except ValueError:
                    print("Cannot convert {:} to int".format(type(option)))
            display("Year Summary", year, yearly_weather)
        # 2. All years summary table 
        elif option == 2:
            years = list(sorted(yearly_weather))
            display("Tabular Summary", years, yearly_weather)      
        # 3. Hottest year on record
        elif option == 3:
            year = hottest(yearly_weather)
            display("Hottest year on record", year, yearly_weather)            
        # 4. Coldest year on record   
        elif option == 4:
            year = coldest(yearly_weather)
            display("Coldest year on record", year, yearly_weather)           
        # 5. Year with most rainy days    
        elif option == 5:
            year = rainiest_days(yearly_weather)
            display("Year with most rainy days", year, yearly_weather)      
        # 6. Year with the highest precipitation
        elif option == 6:
            year = highest_prcp(yearly_weather)
            display("Year with the highest precipitation", year, yearly_weather)          
        # 7. Quit    
        elif option == 7:
            clear_output()
            break
# Run the program  
main()
