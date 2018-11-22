def mon_decorateur(fonction):
	"""Premier exemple de decorateur"""
	print("Notre decorateur est appele avec en parametre la fonction {0}".\
		format(fonction))
	return fonction

@mon_decorateur
def salut():
	"""Fonction modifiee par notre decorateur"""
	print("Salut !")

salut()