# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, chaine, robot, obstacles, sortie, taille_ligne, portes):
        self.chaine = chaine
        self.robot = robot
        self.grille = {}
        self.obstacles = obstacles
        self.sortie = sortie
        self.taille_ligne = taille_ligne
        self.portes = portes

    def sud(self):
    	self.robot += self.taille_ligne
    	if self.mur_bloque():
    		print("\nVous n'êtes pas le passe-murailles de Marcel Aymé! \
Choisissez une autre direction.\n")
    		self.robot -= self.taille_ligne
    	return self.robot

    def nord(self):
    	self.robot -= self.taille_ligne
    	if self.mur_bloque():
    		print("\nVous n'êtes pas le passe-murailles de Marcel Aymé! \
Choisissez une autre direction.\n")
    		self.robot += self.taille_ligne
    	return self.robot

    def ouest(self):
    	self.robot -= 1
    	if self.mur_bloque():
    		print("\nVous n'êtes pas le passe-murailles de Marcel Aymé! \
Choisissez une autre direction.\n")
    		self.robot += 1
    	return self.robot

    def est(self):
    	self.robot += 1
    	if self.mur_bloque():
    		print("\nVous n'êtes pas le passe-murailles de Marcel Aymé! \
    			Choisissez une autre direction.\n")
    		self.robot -= 1
    	return self.robot

    def mur_bloque(self):
    	if self.robot in self.obstacles:
    		return True
    	else:
    		return False

    def deplacer(self):		
    	if self.robot in self.portes:
    		print("\nVous avez détruit une porte !")
    	liste = list(self.chaine)
    	liste[self.chaine.index("X")] = " "
    	liste[self.robot] = "X"
    	self.chaine = "".join(liste)
    	return self.chaine
