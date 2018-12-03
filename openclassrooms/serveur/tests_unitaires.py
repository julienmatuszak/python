""" Ce module permet de réaliser des test unitaires sur les fonctionnalités du jeu :
-  constitution d'un labyrinthe standard,
-  création d'un labyrinthe depuis une chaîne,
-  fonctionnalités du jeu multi-joueurs.
Pour lancer le test, exécutez simplement la commande 'python3 -m unittest' dans le 
répertoire racine du jeu.
Remarque: toutes les fonctionnalités ne sont pas testées, car certaines se trouvent 
dans l'exécutable principal.
"""

import unittest
import random
from carte import Carte
from labyrinthe import Labyrinthe

class Test(unittest.TestCase):

	"""Test case utilisé pour tester les fonctions du jeu 'roboc' sur le serveur."""


	def setUp(self):

		""" Initialisation des tests."""

		""" On crée l'objet carte qui est un attribut de notre instance issue de la 
		classe Test, qui sera créé lors du lancement de l'exécutable."""
		with open("cartes/carte_test", 'r') as fichier:
			contenu = fichier.read()
			self.carte = Carte("carte", contenu)

	def test_Carte(self):

		"""Teste la constitution de l'objet carte."""

		# On vérifie l'existence de tous les attributs cités.
		elt = [self.carte.nom, self.carte.labyrinthe]
		self.assertTrue(elt)
		self.assertTrue(elt)


	def test_Labyrinthe(self):

		"""Teste la constitution de l'objet labyrinthe."""

		# On vérifie l'existence de tous les attributs cités.
		elt = [self.carte.labyrinthe.chaine, self.carte.labyrinthe.robot, \
		self.carte.labyrinthe.obstacles, self.carte.labyrinthe.sortie, \
		self.carte.labyrinthe.taille_ligne, self.carte.labyrinthe.portes, \
		self.carte.labyrinthe.limites, self.carte.labyrinthe.autre_robot, \
		self.carte.labyrinthe.message, self.carte.labyrinthe.message_robot, \
		self.carte.labyrinthe.message_autre_robot, self.carte.labyrinthe.robot_passe,\
		self.carte.labyrinthe.autre_robot_passe] 
		self.assertTrue(elt)


	def test_creer_labyrinthe_depuis_chaine(self):

		"""Teste le fonctionnement de la fonction 'creer_labyrinthe_depuis_chaine'."""
		elt = [[0,1,2,3,4,6,10,12,18,22,24,25,26,27,28], 6, 16, [9, 14], \
		[0, 1, 2, 3, 4, 6, 8, 10, 12, 18, 20, 22, 24, 25, 26, 27, 28], \
		self.carte.labyrinthe.robot, self.carte.labyrinthe.autre_robot, "", 0]
		self.assertEqual(elt[0], self.carte.labyrinthe.limites)
		self.assertEqual(elt[1], self.carte.labyrinthe.taille_ligne)
		self.assertEqual(elt[2], self.carte.labyrinthe.sortie)
		self.assertEqual(elt[3], self.carte.labyrinthe.portes)
		self.assertEqual(elt[4], self.carte.labyrinthe.obstacles)
		self.assertNotIn(elt[5], self.carte.labyrinthe.limites)
		self.assertNotIn(elt[5], self.carte.labyrinthe.portes)
		self.assertNotIn(elt[5], self.carte.labyrinthe.obstacles)
		self.assertNotEqual(elt[5], self.carte.labyrinthe.sortie)
		self.assertNotIn(elt[6], self.carte.labyrinthe.limites)
		self.assertNotIn(elt[6], self.carte.labyrinthe.portes)
		self.assertNotIn(elt[6], self.carte.labyrinthe.obstacles)
		self.assertNotEqual(elt[6], self.carte.labyrinthe.sortie)
		self.assertEqual(elt[7], self.carte.labyrinthe.message)
		self.assertEqual(elt[7], self.carte.labyrinthe.message_robot)
		self.assertEqual(elt[7], self.carte.labyrinthe.message_autre_robot)
		self.assertEqual(elt[7], self.carte.labyrinthe.message_autre_robot)
		self.assertEqual(elt[8], self.carte.labyrinthe.robot_passe)
		self.assertEqual(elt[8], self.carte.labyrinthe.autre_robot_passe)
		""" Remarque: on devrait en toute logique tester que la fonction random
		fonctionne pour attribuer la position des robots mais on démontre ici
		l'existence des attributs des positions des robots ainsi que leur placement
		judicieux, ce qui devrait être suffisant."""

	def test_serveur(self):

		"""Teste les fonctionnalités du jeu multi-joueurs."""

		# On teste la fonction sud lorsqu'elle fait déplacer le robot ou bien le bloque.
		self.carte.labyrinthe.robot = 15
		self.assertEqual(21, self.carte.labyrinthe.sud(self.carte.labyrinthe.robot)[1])
		self.carte.labyrinthe.robot = 21
		self.assertEqual(21, self.carte.labyrinthe.sud(self.carte.labyrinthe.robot)[1])

		# On peut se permettre de ne tester que le passage pour les autres directions.
		self.assertEqual(15, self.carte.labyrinthe.nord(self.carte.labyrinthe.robot)[1])
		self.carte.labyrinthe.robot = 15
		self.assertEqual(14, self.carte.labyrinthe.ouest(self.carte.labyrinthe.robot)[1])
		self.carte.labyrinthe.robot = 14
		self.assertEqual(15, self.carte.labyrinthe.est(self.carte.labyrinthe.robot)[1])

		# On teste que la fonction mur_bloque renvoie bien la valeur "True"
		self.carte.labyrinthe.robot = 8
		self.assertTrue(self.carte.labyrinthe.mur_bloque(self.carte.labyrinthe.robot))

		"""On crée une chaîne (car les robots sont placés aléatoirement) pour pouvoir
		tester quelques fonctionnalités de la fonction 'deplacer', ainsi on peut comparer
		le résultat de la fonction avec la chaîne escomptée."""
		self.carte.labyrinthe.chaine = "OOOOO\nOXO.O\nOx. U\nO O O\nOOOOO"
		self.carte.labyrinthe.robot = 13
		self.carte.labyrinthe.autre_robot = 14
		self.carte.labyrinthe.deplacer()
		self.assertEqual("OOOOO\nO O.O\nOXx U\nO O O\nOOOOO", self.carte.labyrinthe.chaine)
		
		# On teste que la porte réapparaît après le passage d'un des deux robots
		self.carte.labyrinthe.robot = 13
		self.carte.labyrinthe.autre_robot = 15
		self.carte.labyrinthe.autre_robot_passe = 14
		self.carte.labyrinthe.deplacer()
		self.assertEqual("OOOOO\nO O.O\nOX.xU\nO O O\nOOOOO", self.carte.labyrinthe.chaine)

		# On prend l'ancienne chaîne et on teste l'inversion
		self.assertEqual("OOOOO\nO O.O\nOx.XU\nO O O\nOOOOO", self.carte.labyrinthe.\
			inverser_robots())

		""" On teste maintenant la fonctionnalité 'percer_mur'. On teste dans un premier
		 temps si le joueur a fait l'erreur de vouloir percer le mur dans la direction des 
		 limites du labyrinthe."""
		self.carte.labyrinthe.robot = 7
		self.carte.labyrinthe.chaine = "OOOOO\nOXO.O\nO .xU\nO O O\nOOOOO"
		self.assertTrue(self.carte.labyrinthe.mur_limites(self.carte.labyrinthe.robot, "o"))

		""" Ou si le joueur souhaite percer un mur alors qu'il n'y en a pas dans la direction 
		demandée."""
		self.assertFalse(self.carte.labyrinthe.presence_mur(self.carte.labyrinthe.robot, "s"))

		""" Sinon, et si il peut, il perce un mur et on vérifie dans la chaîne obtenue que la 
		porte est percée."""
		self.carte.labyrinthe.percer_mur(self.carte.labyrinthe.robot, "e")
		self.carte.labyrinthe.deplacer()
		self.assertEqual("OOOOO\nOX..O\nO .xU\nO O O\nOOOOO", self.carte.labyrinthe.chaine)

		""" Il reste à tester la fonctionnalité 'murer_porte'. Faisons-le donc sur notre autre
		robot."""

		""" On commence par voir si la fonction 'presence_porte' renvoie 'False' là où il n'y a 
		pas de porte."""
		self.assertFalse(self.carte.labyrinthe.presence_porte(self.carte.labyrinthe.autre_robot, "s"))

		""" Enfin, si le joueur le peut, on fait murer une porte disponible. On compare la 
		chaîne obtenue."""
		self.carte.labyrinthe.murer_porte(self.carte.labyrinthe.autre_robot, "n")
		self.carte.labyrinthe.deplacer()
		self.assertEqual("OOOOO\nOX.OO\nO .xU\nO O O\nOOOOO", self.carte.labyrinthe.chaine)	
