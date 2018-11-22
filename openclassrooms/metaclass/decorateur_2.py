def mon_decorateur(fonction):
	"""Notre decorateur : il va afficher un message avant l'appel de la\
	fonction definie"""

	def fonction_modifiee():
		"""Fonction que l'on va renvoyer. Il s'agit en fait d'une version\
		un peu modifiee de notre fonction originellement definie. On se \
		contente d'afficher un avertissement avant d'executer notre fonction\
		originellement definie"""

		print("Attention ! On appelle {0}".format(fonction))
		return fonction()
	return fonction_modifiee

@mon_decorateur
def salut():
	print("Salut !")

salut()