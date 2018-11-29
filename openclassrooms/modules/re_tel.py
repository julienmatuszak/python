import re
chaine = input("Entrez votre numéro de téléphone : ")
if re.match("^0[0-9]([ -.]?[0-9]{2}){4}", chaine):
	print("Le numéro de téléphone est correctement formaté !")
else:
	print("Le numéro de téléphone n'est pas correctement formaté.")