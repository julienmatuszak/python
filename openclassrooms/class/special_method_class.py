class Personne:
	"""Cette classe represente une personne"""
	def __init__(self, nom, prenom):
		"""Constructeur de notre classe"""
		self.nom = nom
		self.prenom = prenom
		self.age = 33
	def __repr__(self):
		"""Quand on entre notre objet dans l'interpreteur"""
		return "Personne: nom({}), prenom({}), age({})".format\
		(self.nom, self.prenom, self.age)
	def __str__(self):
		"""Methode permettant d'afficher plus joliment notre objet"""
		return "{} {}, age de {} ans".format(self.nom, self.prenom, self.age)