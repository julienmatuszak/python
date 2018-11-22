def obsolete(fonction_origine):
	"""Decorateur levant une exception pour noter que la fonction_origine\
	est obsolete"""

	def fonction_modifiee():
		raise RuntimeError("La fonction {0} est obsolete !".format(fonction_origine))
	return fonction_modifiee

@obsolete
def salut():
	print("Salut !")

salut()