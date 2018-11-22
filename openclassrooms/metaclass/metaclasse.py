class MaMetaClasse(type):

	"""Exemple d'une metaclasse."""

	def __new__(metacls, nom, bases, dict):
		"""Creation de nitre classe."""
		print("On cree la classe {}".format(nom))
		return type.__new__(metacls, nom, bases, dict)

class MaClasse(metaclass=MaMetaClasse):
	pass