import random

a=random.sample(range(1,30),12)
b=random.sample(range(1,30),16)

c=[j for j in a if j in b]