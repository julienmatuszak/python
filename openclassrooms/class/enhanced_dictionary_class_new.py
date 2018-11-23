class DictionnaireOrdonne:
	def __init__(self, base = {}, **donnees):
		self._cles = []
		self._valeurs = []
		if type(base) not in (dict, DictionnaireOrdonne):
			raise TypeError("You didn't enter a dictionary ! Please try again.")
		elif base != {}:
			self._cles = list(base)
			self._valeurs = list(base.values())
		elif donnees != None:
			self._cles = list(donnees)
			self._valeurs = list(donnees.values())
		else:
			print("This is a brand new dictionary !")

	def __repr__(self):
		rep = "{"
		for a in range(0, len(self._cles)):
			if a == 0:
				rep += "\'"+str(self._cles[a])+"\': "+str(self._valeurs[a])
			else:
				rep += ", \'"+str(self._cles[a])+"\': "+str(self._valeurs[a])
		else:
			rep += "}"
		return rep

	def __delitem__(self, cle):
		del self._valeurs[self._cles.index(cle)]
		del self._cles[self._cles.index(cle)]

	def __getitem__(self, cle):
		for a in range(len(self._cles)):
			if self._cles[a] == cle:
				return self._valeurs[a]
				break

	def __setitem__(self, cle, valeur):
		if self._cles == []:
				self._cles.append(cle)
				self._valeurs.append(valeur)
		elif cle in self._cles:
			self._cles[self._cles.index(cle)] == cle
			self._valeurs[self._cles.index(cle)] = valeur
		else:
			self._cles.append(cle)
			self._valeurs.append(valeur)

	def __str__(self):
		return self.__repr__()

	def __len__(self):
		return len(self._cles)

	def __add__(self, nouveau_dictionnaire):
		self._cles.extend(nouveau_dictionnaire._cles)
		self._valeurs.extend(nouveau_dictionnaire._valeurs)
		return self

	def __contains__(self, cle):
		if cle in self._cles:
			return True
		else:
			return False

	def __iter__(self):
		return iter(self._cles)

	def sort(self):
		self._cles = sorted(self._cles)
		self._valeurs = sorted(self._valeurs)

	def reverse(self):
		self._nouvelles_cles = []
		self._nouvelles_valeurs = []
		i = 0
		for a in range(len(self._cles)):
			i -= 1
			self._nouvelles_cles.append(self._cles[i])
			self._nouvelles_valeurs.append(self._valeurs[i])
		self._cles = self._nouvelles_cles
		self._valeurs = self._nouvelles_valeurs

	def keys(self):
		return self._cles

	def values(self):
		return self._valeurs

	def items(self):
		item = []
		for a in range(len(self._cles)):
			item.append((self._cles[a], self._valeurs[a]))
		return item
