class LigneInventaire:

	"""Classe representant une ligne d'un inventaire de vente.

	Attributs attendus par le constructeur :
	    produit -- le nom du produit
	    prix -- le prix unitaire du produit
	    quantite -- la quantite vendue du produit.

	"""


	def __init__(self, produit, prix, quantite):
		self.produit = produit
		self.prix = prix
		self.quantite = quantite

	def __repr__(self):
		return "<Ligne d'inventaire {} ({}X{})>".format(\
			self.produit, self.prix, self.quantite)