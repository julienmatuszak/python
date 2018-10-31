# [x] create a list of 4 to 6 strings: birds
# print each bird in the list
bird_list = ["eagle","goose","duck","magpie"]

for a in bird_list:
    print (a)

# [x]  create a list of 7 integers: player_points
# [x] print double the points for each point value
player_points = [1,2,3,4,5,6,7]

for a in player_points:
    print(2*a)

# [x] create long_string by concatenating the items in the "birds" list previously created
# print long_string - make sure to put a space betweeen the bird names
bird_list = ["eagle","goose","duck","magpie"]
long_string = ""
for a in bird_list:
    long_string += a+" "
print(long_string)

# [x] Using cities from the example above iterate throught the list using "for"/"in"
# [x] Print only cities starting with "m"
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
for a in cities:
    if a[0].upper() == 'M':
        print(a)

# [x] Using cities from the example above iterate throught the list using "for"/"in"
# [x] sort into lists with "A" in the city name and without "A" in the name: a_city & no_a_city
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
a_city = ""
no_a_city = ""
for a in cities:
    if "a" in a:
        a_city += a+" "
    else:
        no_a_city += a+" "
print("a_city : ",a_city)
print("no_a_city : ",no_a_city)

# [x] complete paint stock
def paint_stock(color_request,paint_colors):
    for color in paint_colors:
        if color.lower() == color_request.lower():
            return "found"
        else:
            pass
    return "not found"

paint_colors = ["blue", "red", "black", "white"]
color_request = input("enter your paint color: ")
print("Your color",color_request,"is",paint_stock(color_request,paint_colors))

# [x] Complete Foot Bones Quiz
def foot_bones_quiz(search,foot_bones):
    while True:
        for bone in foot_bones:
            if bone.lower() == search.lower():
                foot_bones.remove(bone)
                return "correct"
            else:
                pass
        return "incorrect"
        break

foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform","intermediate cuneiform", "medial cuneiform"]
print(foot_bones_quiz(input("1st try ! Find me a foot bone: "),foot_bones))
print(foot_bones_quiz(input("2nd try ? Find me a foot bone: "),foot_bones))
if len(foot_bones) == 5:
    print("2 bones found")
elif len(foot_bones) == 6:
    print("1 bone found")
else:
    print("0 bone found")

