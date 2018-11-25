# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-3].lower()
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
		carte = Carte(nom_carte, contenu)
		cartes.append(carte)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# On propose d'abord le choix d'un numéro de labyrinthe
choix = input("\nEntrez un numéro de labyrinthe pour commencer à jouer : ")
while choix.isdigit() is False or int(choix)-1 not in range(len(cartes)):
	print("\nDésolé, votre choix est incorrect. Veuillez recommencer.")
	choix = input("\nEntrez un numéro de labyrinthe pour commencer à jouer : ")

# Si il y a une partie sauvegardée, on propose de l'afficher sinon on affiche le labyrinthe de base
# On commence par créer le répertoire des sauvegardes s'il n'existe pas
if os.path.exists("sauvegardes") is False:
	os.mkdir("sauvegardes")
if os.path.exists("sauvegardes/"+cartes[int(choix)-1].nom+"txt"):
	sauvegarde = input("\nVoulez-vous charger la partie sauvegardée ? \
Sinon, la partie enregistée sera écrasée ! (y/n) ")
	if sauvegarde.lower().startswith("y"):
		chemin = "sauvegardes/"+cartes[int(choix)-1].nom+"txt"
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
		carte = Carte(cartes[int(choix)-1].nom, contenu)
		labyrinthe = carte.labyrinthe
		print("\n"+labyrinthe.chaine)
	else:
		chemin = "cartes/"+cartes[int(choix)-1].nom+"txt"
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
		carte = Carte(cartes[int(choix)-1].nom, contenu)
		labyrinthe = carte.labyrinthe
		print("\n"+labyrinthe.chaine)
else:
	chemin = "cartes/"+cartes[int(choix)-1].nom+"txt"
	with open(chemin, "r") as fichier:
		contenu = fichier.read()
	carte = Carte(cartes[int(choix)-1].nom, contenu)
	labyrinthe = carte.labyrinthe
	print("\n"+labyrinthe.chaine)

# Boucle principale du jeu
while True:
	direction = input("> ")
	while direction.lower()[0] not in ["s", "n", "e", "o", "q"]:
		print("\nJe n'ai pas compris votre requête. Veuillez recommencer.")
		direction = input("> ")
	if direction.lower().startswith("s"):
		labyrinthe.sud()
	if direction.lower().startswith("n"):
		labyrinthe.nord()
	if direction.lower().startswith("e"):
		labyrinthe.est()
	if direction.lower().startswith("o"):
		labyrinthe.ouest()
	if direction.lower().startswith("q"):
		print("\nVous abandonnez! Dommage! Au revoir!")
		break
	if labyrinthe.robot == labyrinthe.sortie:
		labyrinthe.deplacer()
		print("\n"+labyrinthe.chaine)
		with open("sauvegardes/"+cartes[int(choix)-1].nom+"txt", "w") as fichier:
			fichier.write(labyrinthe.chaine)
		print("\nFélicitations ! Vous avez gagné !\n")
		break
	labyrinthe.deplacer()
	print("\n"+labyrinthe.chaine)
	with open("sauvegardes/"+cartes[int(choix)-1].nom+"txt", "w") as fichier:
		fichier.write(labyrinthe.chaine)

"""
Améliorations à faire:
- Rendre le code plus lisible.
- éliminer la redondance de lecture des cartes lorsqu'on appelle Carte une fois
pour avoir le nom (et charger les cartes inutilement) et l'autre pour charger les cartes
- mettre un message lorsqu'on charge une partie gagnée que la partie a déjà été gagnée
et que ça ne sert à rien de la continuer (ou bien ne pas enrgistrer le fichier quand on est
sur le point de gagner)
- trouver un moyen de 'reconstruire' les portes
"""