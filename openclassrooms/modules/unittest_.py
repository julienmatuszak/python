import random
import unittest

class RandomTest(unittest.TestCase):

	"""TestCase est utilisé pour tester les fonctions du module 'random'."""

	def test_choice(self):
		"""Teste le fonctionnement de la fonction 'random.choice'."""
		liste = list(range(10))
		elt = random.choice(liste)
		# Vérifie que 'elt' est dans 'liste'
		self.assertIn(elt, liste)
		self.assertIn(elt, ('a', 'b', 'c'))
