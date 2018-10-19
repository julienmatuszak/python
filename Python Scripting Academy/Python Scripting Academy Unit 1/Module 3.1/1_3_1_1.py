sunny_today = True
# [x] test if it is sunny_today and give proper responses using if and else
if sunny_today:
    print("Sun is shining!")
else:
    print("Enjoy the rain!")

sunny_today = False
# [x] use code you created above and test sunny_today = False
if sunny_today:
    print("Sun is shining!")
else:
    print("Enjoy the rain!")

test_string_1 = "welcome"
test_string_2 = "I have $3"
# [x] use if, else to test for islower() for the 2 strings
if test_string_1.islower():
    print('"'+test_string_1+'"'+" is all in lower case")
else:
    print('"'+test_string_1, "is not all in lower case")
if test_string_2.islower():
    print('"'+test_string_2+'"'+" is all in lower case")
else:
    print('"'+test_string_2+'"'+" is not all in lower case")

test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"
# [x] create a function w_start_test() use if & else to test with startswith('w')
def w_start_test(test):
    if test.lower().startswith('w'):
        print('"'+test+'"'+" starts with 'w'")
    else:
        print('"'+test+'"'+" doesn't start with 'w'")

# [x] Test the 3 string variables provided by calling w_start_test()
w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)
