import random
import unittest

class RandomTest(unittest.TestCase):

	"""Test case est utilisé pour tester les fonctions du module 'random'."""

	def test_sample(self):
		"""Teste le fonctionnement de la fonction 'random.sample'."""
		liste = list(range(10))
		extrait = random.sample(liste, 5)
		for element in extrait:
			self.assertIn(element, liste)

		with self.assertRaises(ValueError):
			random.sample(liste, 20)
