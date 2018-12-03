# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

# On va appeler notre labyrinthe et ses attributs ici
from random import choice
from labyrinthe import Labyrinthe
from math import ceil

""" Cette fonction ne dépend pas de la classe. Elle permet de creer le labyrinthe et 
ses attributs qui seront utilisés par l'objet labyrinthe. Elle place aussi le robot.
"""
def creer_labyrinthe_depuis_chaine(chaine):
	obstacles, portes = [], []
	for cle in range(len(chaine)):
		if chaine[cle] == "O":
			obstacles.append(cle)
		if chaine[cle] == ".":
			portes.append(cle)
	sortie, taille_ligne = chaine.index("U"), chaine.index("\n") + 1
	robot = -1
	while chaine[robot] != " ":
		robot = choice(list(range(0,len(chaine)-1)))
	chaine = chaine[0:robot] + "X" + chaine[robot+1: len(chaine)]
	autre_robot = -1
	while chaine[autre_robot] != " ":
		autre_robot = choice(list(range(0,len(chaine)-1)))
	chaine = chaine[0:autre_robot] + "x" + chaine[autre_robot+1: len(chaine)]

	#On définit les limites du labyrinthe :
	limites = []
	for a in range(len(chaine)):
		if a in range(taille_ligne-1):
			limites.append(a)
		if a/(taille_ligne) in range(1,ceil(len(chaine)/taille_ligne)-1):
			limites.append(a)
			limites.append(a+taille_ligne-2)
		if a in range(len(chaine) - taille_ligne, len(chaine) - 1):
			limites.append(a)
	limites.remove(chaine.index("U"))

	labyrinthe = Labyrinthe(chaine, robot, obstacles, sortie, taille_ligne, portes, \
		limites, autre_robot)
	return labyrinthe

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        """L'attribut labyrinthe sera lui-même un objet qui nous intéressera car il
        contiendra lui-même les attributs de la classe Labyrinthe"""
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
    	return "<Carte {}>".format(self.nom)