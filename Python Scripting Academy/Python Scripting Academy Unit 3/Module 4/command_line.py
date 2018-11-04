import sys

# Number of arguments
argc = len(sys.argv)
print(argc, "arguments and options were passed")

# List of arguments and options
print("The arguments and options passed are: ")
for i in range(argc):
    print("argv[{:d}] = {}".format(i, sys.argv[i])) 