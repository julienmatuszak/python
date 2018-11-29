from fractions import Fraction

un_demi = Fraction(1,2)
print(un_demi)
un_quart = Fraction('1/4')
print(un_quart)
Fraction(1,4)
autre_fraction = Fraction(-5, 30)
print(autre_fraction)

Fraction.from_float(0.5)
print(Fraction(1, 2))

print(float(un_quart))

un_dixieme = Fraction(1, 10)
un_dixieme + un_dixieme + un_dixieme
print(Fraction(3, 10))

print(un_dixieme * un_quart)
print(un_dixieme + 5)
print(un_demi / un_quart)
print(un_quart / un_demi)