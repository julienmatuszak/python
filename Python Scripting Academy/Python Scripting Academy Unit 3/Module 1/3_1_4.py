# [x] Write a program to:
# 1) Prompt the user for a directory name
# 2) Create the directory
# 3) Verify the directory was created by listing the content of the current working directory
# 4) Remove the created directory
# 5) Verify the directory was removed by listing the content of the current working directory
import os
directory = input("Choose a name for your new directory : ")
os.mkdir(directory)
print("Please check if the new directory has been created and under your name at the following path and in the list below\nPath:",os.getcwd(),"\nList:",os.listdir())
os.rmdir(directory)
print("Please check if the new directory was removed and under your name at the following path and in the list below\nPath:",os.getcwd(),"\nList:",os.listdir())

# [x] Write a program to:
# 1) Create a directory called "my_dir"
# 2) Change the current working directory to "my_dir"
# 3) Verify you are in the correct directory by displaying the current working directory
# 4) Change the working directory back to the parent directory
# 5) Verify you are in the correct directory by displaying the current working directory
# 6) Rename "my_dir" to "your_dir"
# 7) Verify the directory was renamed by listing the content of the current working directory
# 8) Remove "your_dir"
# 9) Verify the directory was removed by listing the content of the current working directory
import os
os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/")
directory = "my_dir"
os.mkdir(directory)
os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/"+directory)
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.rename("my_dir","your_dir")
print(os.listdir())
os.rmdir("your_dir")
print(os.listdir())

# [x] Write a program that prompts the user for a file or directory name 
# then prints a message verifying if it exists in the current working directory
import os
abs_path = input("Which file or directory are you looking for here ? ")
print(os.getcwd())
print(os.path.abspath(abs_path))
if os.path.exists(abs_path):
    print("There is a path to your file or directory !")
else:
    print("There is no path to your file or directory")

# [x] Write a program to print the absolute path of all directories in "parent_dir"
# HINTS:
# 1) Verify you are inside "parent_dir" using os.getcwd()
# 2) Use os.listdir() to get a list of files and directories in "parent_dir"
# 3) Iterate over the elements of the list and print the absolute paths of all the directories
import os
print(os.getcwd())
parent_list = os.listdir()
for a in parent_list:
    print(a)
