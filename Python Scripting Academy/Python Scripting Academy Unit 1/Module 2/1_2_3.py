# [x] fix the sequence of the code to remove the NameError
def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)

have_hat = hat_available('green')  
  
print('hat available is', have_hat)

# [x] create function bird_available
def bird_available(x):
    bird_types = "eagle, magpie, mockingbird"
    return(x.lower() in bird_types)
# [x] user input
bird = input("Which type of bird are you looking for ? : ")
# [x] call bird_available
# [x] print availbility status
print("bird availability is", bird_available(bird))

# define function how_many
def how_many():
    requested = input("enter how many you want: ")
    return requested

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")
