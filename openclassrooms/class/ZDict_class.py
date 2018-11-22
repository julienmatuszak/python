class ZDict:
	"""CLasse enveloppe d'un dictionnaire"""

	def __init__(self):
		"""Notre classe n'a aucun parametre"""
		self._dictionnaire = {}
	def __repr__(self):
		return "Dictionary contains: {}".format(self._dictionnaire)
	def __getitem__(self, index):
		"""Cette methode speciale est appelee quand on fait objet[index]
		Elle redirige vers self._dictionnaire[index]"""

		return self._dictionnaire[index]
	def __setitem__(self, index, valeur):
		self._dictionnaire[index] = valeur
	def __delitem__(self, index):
		del self._dictionnaire[index]
	def __contains__(self, index):
		"""Cette methode revient au meme que de faire ma_liste.\
		__contains__(index) ou index in ma_liste et renvoie un bool"""
		for a in range(0, len(self)):
			if self[a] == index:
				return True
			else:
				return False
	def __len__(self):
		return len(self)
