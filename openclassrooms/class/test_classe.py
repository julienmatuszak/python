class Test:
	"""Une classe de test tout simplement"""

	def afficher():
		"""Fonction chargee d'afficher quelque chose"""
		print("On affiche la meme chose.")
		print("Peu importe les donnees de l'objet ou de la classe.")
	afficher = staticmethod(afficher)
