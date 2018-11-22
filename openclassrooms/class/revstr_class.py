class RevStr(str):
	"""Classe reprenant les methodes et les attributs des chaines construites depuis 'str'.\
	On se contente de definir une methode de parcous differente : au lieu de parcourir la \
	chaine de la premiere a la derniere lettre, on la parcourt de la derniere a la premiere.
	Remarquons que comme la classe herite de string, il n'est pas la peine de definit une \
	methode de constructeur init, ainsi que d'autres methodes principales."""

	def __iter__(self):
		"""Cette methode renvoie un iterateur parcourant la chaine dans le sens inverse de \
		celui de 'str'"""

		return ItRevStr(self) # On renvoie l'iterateur cree pour l'occasion

class ItRevStr:
	"""Un iterateur permettant de parcourir une chaine de la derniere lettre a la premiere.
	On stocke dans des attributs la position courante et la chaine a parcourir"""

	def __init__(self, chaine_a_parcourir):
		"""On se posisitonne a la fin de la chaine"""
		self.chaine_a_parcourir = chaine_a_parcourir
		self.position = len(chaine_a_parcourir)
	def __next__(self):
		"""Cette methode doit renvoyer l'element suivant dans le parcours, ou lever l'excep\
		tion 'StopIteration' si le parcours est fini"""

		if self.position == 0: # Fin du parcours
			raise StopIteration
		self.position -= 1 # On decremente la position
		return self.chaine_a_parcourir[self.position]
