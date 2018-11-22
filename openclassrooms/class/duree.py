from duree_classe import *

d1 = Duree(3, 5)
print(d1)
print(d1+4)
print(4+d1)
print(d1.__add__(4))
d2 = d1 + 54
print(d2)
d1-=128
print(d1)