trace_classes = {} # Notre dictionnaire vide

class MetaWidget(type):

	"""Notre metaclasse pour nos Widgets.

	Elle herite de type, puisque c'est une metaclasse.
	Elle va ecrire dans le dictionnaire trace_classes a chaque fois
	qu'une classe sera creee, utilisant cette metaclasse naturellement."""

	def __init__(cls, nom, bases, dict):
		"""Constructeur de notre metaclasse, appele quand on cree une classe."""
		type.__init__(cls, nom, bases, dict)
		trace_classes[nom] = cls