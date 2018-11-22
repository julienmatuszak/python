class Compteur:
	objets_crees = 0
	def __init__(self):
		Compteur.objets_crees += 1
	def combien(cls):
		print("Jusqu'a present, {} objets ont ete crees.".format(
			cls.objets_crees))
	combien = classmethod(combien)
	def afficher():
		print("On affiche")
	afficher = staticmethod(afficher)