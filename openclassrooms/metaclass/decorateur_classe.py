def decorateur(classe):
	print("Definition de la classe {0}".format(classe))
	return classe

@decorateur
class Test:
	pass
