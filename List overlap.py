import random
a=random.sample(range(1, 101),10)
b=random.sample(range(1, 101),10)
c=[]
for i in a:
    for j in b:
        if i == j:
            c.append(i)
d=[]
for i in c:
    if i not in d:
        d.append(i)
if d == []:
    print("There are no common elements between those two lists !")
else:
    print("The common elements between the two lists are : " + str(d))