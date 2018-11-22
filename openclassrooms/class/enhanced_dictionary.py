from enhanced_dictionary_class import *

fruits = DictionnaireOrdonne()
print(fruits)

fruits["pomme"] = 52
fruits["poire"] = 34
fruits["prune"] = 128
fruits["melon"] = 15
print(fruits)

fruits.sort()
print(fruits)

legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
print(legumes)

print(len(legumes))

legumes.reverse()

fruits = fruits + legumes

print(fruits)

del fruits['haricot']

print('haricot' in fruits)

print(legumes["haricot"])

for cle in legumes:
	print(cle)

print(legumes.keys())
print(legumes.values())

for nom, qtt in legumes.items():
	print("{0} ({1})".format(nom, qtt))
