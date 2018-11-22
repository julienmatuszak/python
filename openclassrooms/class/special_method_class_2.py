class Protege:
	"""Classe possedant une methode paritculiere d'acces a ses attributs :
	Si l'attribut n'est pas trouve, on affiche une alerte et renvoie None"""

	def __init__(self):
		"""On cree quelques attributs par defaut"""
		self.a = 1
		self.b = 2
		self.c = 3
	def __getattr__(self, nom):
		"""Si Python ne trouve pas l'attribut nomme nom, il appelle\
		cette methode. On affiche une alerte"""
		print("Alerte! Il n'y a pas d'attribut {} ici !".format(nom))
		print("Redirecting to attribute  c")
		self.nom = self.c
	def __setattr__(self, nom_attr, val_attr):
		"""Methode appelee quand on fait objet.nom_attr = val_attr
		On se charge d'enregistrer l'objet"""

		object.__setattr__(self, nom_attr, val_attr)
		#self.enregistrer()
	def __delattr__(self, nom_attr):
		"""On elimine attribute en passant par l'objet"""
		"""Si on ne peut supprimer l'attribut, on leve l'exception \
		AttributeError"""
		try:
			object.__delattr__(self, nom_attr)
		except:
			raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")
		else:
			pass
	"""
	objet = maClasse()
	getattr(self, "nom") revient a rentrer self.nom dans l'interpreteur (il renvoie l'attribut\
	 s'il y en a un sinon un message AttributeError).
	 !!!On ne peut pas ecrire __getattr__ car il ne renvoie un message que si l'attribut n'existe pas!
	 Il faut utiliser __getattribute__ !!!
	setattr(objet, "nom", valeur) revient a rentrer objet.nom = valeur ou objet.__setattr__("nom", val)
	delattr(objet, "nom") revient a rentrer del objet.nom ou objet.__delattr__("nom")
	hasattr(objet, "nom") renvoie True (si l'attribut existe) et False sinon, mais attention avant cela,
	hasattr passe par getattr! Ca veut dire que si on ajoute ensuite un attribut, True sera renvoye.