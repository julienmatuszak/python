import random
import unittest

class RandomTest(unittest.TestCase):

	"""Test case est utilisé pour tester les fonctions du module 'random'."""

	def setUp(self):
		"""Initialisation des tests."""
		self.liste = list(range(10))

	def test_choice(self):
		"""Teste le fonctionnement de la fonction 'random.choice'."""
		liste = list(range(10))
		elt = random.choice(liste)
		# Vérifie que 'elt' est dans 'liste'
		self.assertIn(elt, liste)

	def test_shuffle(self):
		"""Teste le fonctionnement de la fonction 'random.shuffle'."""
		liste = list(range(10))
		liste_a_comparer = liste
		random.shuffle(liste)
		liste.sort()
		self.assertEqual(liste, liste_a_comparer)

	def test_sample(self):
		"""Teste le fonctionnement de la fonction 'random.sample'."""
		liste = list(range(10))
		extrait = random.sample(liste, 5)
		for element in extrait:
			self.assertIn(element, liste)

		with self.assertRaises(ValueError):
			random.sample(liste, 20)
