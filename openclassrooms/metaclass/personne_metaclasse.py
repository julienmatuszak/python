class Personne:

	"""Classe definissant une personne.

	Elle possede comme attributs :
	nom -- le nom de la personne
	prenom -- son prenom
	age -- son age
	lieu_residence -- son lieu de residence

	Le nom et le prenom doivent etre passes au constructeur."""

	def __new__(cls, nom, prenom):
		print("Appel de la methode __new__ de la classe {}".format(cls))
		# On laisse le travail a object
		return object.__new__(cls)

	def __init__(self, nom, prenom):
		"""Constructeur de notre personne."""
		print("Appel de la methode __init__")
		self.nom = nom
		self.prenom = prenom
		self.age = 23
		self.lieu_residence = "Lyon"