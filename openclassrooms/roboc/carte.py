# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

# On va appeler notre labyrinthe et ses attributs ici
from labyrinthe import Labyrinthe

# Cette fonction ne dépend pas de la classe.
def creer_labyrinthe_depuis_chaine(chaine):
	obstacles, portes = [], []
	for cle in range(len(chaine)):
		if chaine[cle] == "O":
			obstacles.append(cle)
		if chaine[cle] == ".":
			portes.append(cle)
	robot, sortie, taille_ligne = chaine.index("X"), chaine.index("U"),\
	 chaine.index("\n") + 1
	labyrinthe = Labyrinthe(chaine, robot, obstacles, sortie, taille_ligne, portes)
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