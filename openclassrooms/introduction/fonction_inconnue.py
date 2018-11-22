def fonction_inconnue(*parametres, nom = "nom", prenom = "prenom"):
	print("J'ai reçu : {}.".format(parametres, nom))

fonction_inconnue(2) # On appelle la fonction sans paramètre
fonction_inconnue(33)
fonction_inconnue('a', 'e', 'f')
var = 3.5
fonction_inconnue(var, [4], "...")