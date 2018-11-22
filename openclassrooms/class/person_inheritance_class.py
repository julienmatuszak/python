class Personne:
	"""Classe representant une personne"""
	def __init__(self, nom):
		"""Constructeur"""
		self.nom = nom
		self.prenom = "Martin"
	def __str__(self):
		"""Methode appelee lors d'une conversion de l'objet en chaine"""
		return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
	"""Classe definissant un agent special.
	Elle herite de la classe Personne"""

	def __init__(self, nom, matricule):
		"""Un agent se definit par son nom et son matricule"""
		Personne.__init__(self, nom)
		self.matricule = matricule
	def __str__(self):
		"""Methode appelee lors d'une conversion de l'objet en chaine"""
		return "Agent {0}, matricule {1}".format(self.nom, self.matricule)