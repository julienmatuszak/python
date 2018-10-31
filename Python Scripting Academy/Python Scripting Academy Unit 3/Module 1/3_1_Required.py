# [x] The following program is designed to generate a number of directories.
# The directory names follow the pattern (MM_DD_YY_randnum), where:
#     - MM_DD_YY: is today's date as month/day/year
#     - randnum: is a random integer between 10000 and 50000
# For example, if today is May 12th, 2016, then the following would be valid names: 05_12_16_11050 or 05_12_16_15001
#
# For this task, you should complete the functions:
# 1) `directory_count()`
# 2) `name_generator()`
# 3) `directory_creator(name)`
# 4) `create()`
#
# HINT: You should import all necessary modules
import os
from random import randint
import math
from datetime import datetime
def directory_count():
    """
    Calculate the number of directories to be generated.   
    I) Get the current minute using appropriate functionality from `datetime`
    II) Take the square root of ..the current minute + 15
    III) Round the square root to an integer
    VI) return the rounded number as the number of directories to be created   
    args: 
          NONE   
    returns: 
         `dir_count`: number of directories to be created 
    """
    current_minute = 0
    dir_count = 0
    current_minute = datetime.today().minute
    dir_count = int(math.sqrt(current_minute+15))
    return(dir_count)
def name_generator():
    """
    Generate a single directory name using the pattern (MM_DD_YY_randnum).   
    args:
         NONE    
    returns:
         `dir_name`: string containing a valid directory name
    """
    dir_name = ""
    randnum = 0
    randnum = randint(10000,50000)
    dir_name = datetime.today().strftime("%m_%d_%Y_")+str(randnum)
    return(dir_name)
def directory_creator(name):
    """
    Create a single directory called `name` in the current working directory.   
    args:
         name: directory to be created   
    returns:
         NONE
    """
    os.mkdir(name)
def create():
    """
    Generate the necessary directories.    
    Use `directory_count` to calculate the number of directories, then use `directory_creator` and `name_generator`.
    args:
         NONE    
    returns:
         NONE
    """
    for a in range(0,directory_count()):
        directory_creator(name_generator())        
# Change working directory to `parent_dir` or `create`
if("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/parent_dir" not in os.getcwd()):
    if os.path.exists("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/parent_dir"):
        print("Changing working dir to /Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/parent_dir")
        os.chdir("/Users/julien.matuszak/Repos/python/Python Scripting Academy/Python Scripting Academy Unit 3/Module 1/parent_dir")
    else:
        os.mkdir(os.getcwd() + "/parent_dir")
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
else:
    # so the code can run multiple times 
    # while directory not ending with 'parent_dir' move up the path ..\
    while "parent_dir" not in os.getcwd()[-11:]:
        # move up in dir to find 'parent_dir'
        os.chdir("..")
        print("moved up", os.getcwd())       
# print the current working directory (should be "parent_dir")
print("The current working directory is:", os.getcwd())
# check for randoms_directory if not present, create new
if os.path.exists(os.getcwd() + "/randoms_directory") != True:
    os.mkdir("randoms_directory")
# change the current working directory to randoms_directory
print("Changing working dir to randoms_directory")
os.chdir("randoms_directory")
# print the current working directory (should be "randoms_dir")
print("The current working directory is:", os.getcwd())
# create directories inside "randoms_directory"
create()   
# list the content of the current directory
print("Current directory content:", os.listdir())

