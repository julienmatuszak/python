# [x] print ft_bones list
# [x] delete "cuboid" from ft_bones
# [x] reprint list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
print (ft_bones)
del ft_bones[2]
print (ft_bones)

# [x] print ft_bones list
# [x] delete "cuboid" from ft_bones
# [x] delete "navicular" from list
# [x] reprint list
# [x] check for deletion of "cuboid" and "navicular"
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
print (ft_bones)
del ft_bones[2]
print (ft_bones)
del ft_bones[2]
print (ft_bones)

# [x] pop() and print the first and last items from the ft_bones list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
pop1 = ft_bones.pop()
print(ft_bones.pop(0),pop1)
# [x] print the remaining list
print(ft_bones)

# [x] complete the Register Input task above
purchase_amounts = []
index = 0
while True:
    price = purchase_amounts.append(input("Price of your item ? (enter price without symbol or 'done' when finished) "))
    if purchase_amounts[index] == "done":
        purchase_amounts.pop()
        break
    index += 1
print (purchase_amounts)

# [x] remove one "Poodle" from the list: dogs , or print "no Poodle found"
# [x] print list before and after
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
print(dogs)
while "Poodle" in dogs:
    dogs.remove("Poodle")
print("no more Poodle found !")
print(dogs)
