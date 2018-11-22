def afficher(*parametres, sep=' ', fin ='\n'):
	parametres=list(parametres)
	new_string = ""
	for a in parametres:
		new_string +=a+sep
	new_string+=fin
	print(new_string)

afficher("hello","me","and","you")