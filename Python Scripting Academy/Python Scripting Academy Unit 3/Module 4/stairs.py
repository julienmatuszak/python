
# [x] The following program generates a staircase character art
# The `size` variable controls the number of steps
# The `base_shape` defines the characters used to generate the art
# Modify the program so the `size` is set as a positional command line argument, and base_shape as an optional 
# command line argument with a default value of `[]`

import argparse

def gen_stairs(steps, base_shape):
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print(base_shape, end = "")
        print()

# Define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('size', action = 'store', type = int, help = 'Controls the numbers of steps')

# Add optional arguments
parser.add_argument('-b', '--base_shape', metavar = "shape", action = 'store', type = str, default = "[]", help = 'Defines the characters used to generate the art')

# Parse command-line arguments
args = parser.parse_args()

# Program
# Generate a staircase with steps using '[]` as default a base shape 
gen_stairs(args.size, args.base_shape)
