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

# [x] Complete the following program to delete the first 10 files inside `files_exercises` (0.txt, 1.txt ... 9.txt)
# Make sure the to run the environment setup code before running your own program.
import os
if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")
# list the content of `files_exercises`
print('Content of "files_exercises" before removing the files')
print(os.listdir()) 
for i in range(10):
    os.remove(str(i)+".txt")   
# list the content of `files_exercises`
print('Content of "files_exercises" after removing the files')
print(os.listdir()) 

# [x] Write a program to delete all the even numbered files inside `files_exercises`
# Make sure the to run the environment setup code before running your own program.
import os
os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises")
if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")
for i in range(100):
    if i%2 == 0:
        try:
            os.remove(str(i)+".txt")
        except FileNotFoundError as exception_object:
            print("Cannot find file: ", exception_object)

# [x] Write a program to delete all the directories inside `files_exercises`
# Make sure the to run the environment setup code before running your own program.
import os
os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises")
if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")   
for i in range(1,6):
    try:
        os.rmdir("dir_"+str(i))
    except FileNotFoundError as exception_object:
        print("Cannot find file: ", exception_object)
    except PermissionError as exception_object:
        print("Cannot delete a directory: ", exception_object)
    except Exception as exception_object:
        print("Unexpected exception: ", exception_object)
      
# [x] Write a program to ask the user for a file number, 
# then delete the file if it exists or display an appropriate error message if it does not.
# Make sure the to run the environment setup code before running your own program.
# Test your program with the following:
# case 1: user inputs 84, 84.txt should be deleted
# case 2: user inputs 84 (again), a File does not exist message is printed
# case 3: user inputs 5, 5.txt should be deleted
import os
os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises")
if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")
num = input("Please enter a file number to delete : ")
try:
    os.remove(num+".txt")
    print("File removed !")
except FileNotFoundError as exception_object:
    print("Cannot find file: ", exception_object)
except PermissionError as exception_object:
    print("Cannot delete a directory: ", exception_object)
except Exception as exception_object:
    print("Unexpected exception: ", exception_object)

# [x] Write a program to print the first line of every file inside `files_exercises`
# Use a `with` statement to open (and close) every file
# Make sure the to run the environment setup code before running your own program.
import os
os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises")
if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")
file_path = "/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 3/files_exercises"
for a in range(100):
    try:
        with open(file_path+"/"+str(a)+".txt", 'r') as file:
            x = int(file.readline()) #raise an exception if lines are not numeric
            print(x)
    except FileNotFoundError as exception_object:
        print("Cannot find file: ", exception_object)
    except Exception as exception_object:
        print("Unexpected exception", exception_object)
print("File is closed?", file.closed)
