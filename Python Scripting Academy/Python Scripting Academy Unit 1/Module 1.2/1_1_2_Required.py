# Create Allergy check CODE

# 1[x] get input for test
input_test = input("enter some things eaten in the last 24 hours: ").lower()

# 2/3[x] print True if "dairy" is in the input or False if not
print("dairy" in input_test)

# 4[x] Check if "nuts" are in the input
print('nuts' in input_test)

# 4+[x] Challenge: Check if "seafood" is in the input
print("seafood is in the input: ", 'seafood' in input_test)

# 4+[x] Challenge: Check if "chocolate" is in the input
print("chocolate is in the input: ", 'chocolate' in input_test)

# 5[x] Challenge: make your code work for input regardless of case, e.g. - print True for "Nuts", "NuTs", "NUTS" or "nuts"
