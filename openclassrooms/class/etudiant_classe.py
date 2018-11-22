class Etudiant:

	"""Classe representant un etudiant.

	On represente un etudiant par son prenom (attribut prenom), son age\
	(attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

	Parametres du constructeur :
	    prenom -- le prenom de l'etudiant
	    age -- l'age de l'etudiant
	    moyenne -- la moyenne de l'etudiant

	"""

	def __init__(self, prenom, age, moyenne):
		self.prenom = prenom
		self.age = age
		self.moyenne = moyenne

	def __repr__(self):
		return "<Etudiant {} (age={}, moyenne={})>".format(\
			self.prenom, self.age, self.moyenne)