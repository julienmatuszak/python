import random
import unittest

class RandomTest(unittest.TestCase):

	"""TestCase est utilisé pour tester les fonctions du module 'random'."""

	def test_shuffle(self):
		"""Teste le fonctionnement de la fonction 'random.shuffle'."""
		liste = list(range(10))
		liste_a_comparer = liste
		random.shuffle(liste)
		liste.sort()
		self.assertEqual(liste, liste_a_comparer)
