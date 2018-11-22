
# [x] The following program contains a few functions to count the number of: vowels, consonants, and digits in a sentence.
# Modify the program so it only run the test case when the program is executed directly. 
# In other words, when the program is imported as a module for another program, it shouldn't display the test cases.
def count_vowels(sentence):
    """Count the number of vowels in sentence."""
    vowels = 0
    for c in sentence:
        if c.lower() in "aeiouy":
            vowels = vowels + 1
    return vowels

def count_consonants(sentence):
    """Count the number of consonants in sentence."""
    consonants = 0
    for c in sentence:
        if c.isalpha():
            if c.lower() not in "aeiouy":
                consonants = consonants + 1
    return consonants

def count_digits(sentence):
    """Count the number of digits in sentence."""
    digits = 0
    for c in sentence:
        if c.isdigit():
            digits = digits + 1
    return digits

test_sentence = "Plan 2 is not working!"
print("Number of vowels = {:d}".format(count_vowels(test_sentence)))
print("Number of consonants = {:d}".format(count_consonants(test_sentence)))
print("Number of digits = {:d}".format(count_digits(test_sentence)))
