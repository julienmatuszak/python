def creer_personne(personne, nom, prenom):
	"""La fonction qui jouera le role de constructeur pour notre classe Personne.

	Elle prend en parametre, outre la personne :
	nom -- son nom
	prenom -- son prenom"""

	personne.nom = nom
	personne.prenom = prenom
	personne.age = 21
	personne.lieu_residence = "Lyon"

def presenter_personne(personne):
	"""Fonction representant la personne.

	Elle affiche son prenom et son nom"""

	print("{} {}".format(personne.prenom, personne.nom))

# Dictionnaire des methodes
methodes = {
	"__init__": creer_personne,
	"presenter": presenter_personne,
}

# Creation dymamique de la classe
Personne = type("Personne", (), methodes)
