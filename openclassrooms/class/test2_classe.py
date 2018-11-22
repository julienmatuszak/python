class Test:
	"""Une classe de test tout simplement"""

	def __init__(self):
		"""On definit dans le constructeur un unique attribut"""
		self.mon_attribut = "ok"

	def afficher_attribut(self):
		"""Methode affichant l'attribut 'mon_attribut'"""
		print("Mon attribut est {}".format(self.mon_attribut))
