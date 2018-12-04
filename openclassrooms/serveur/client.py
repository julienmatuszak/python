"""
Ce fichier est l'exécutable python du premier client. Merci de le lancer suite à l'exécution de serveur.py.
Pour l'instant, l'application ne peut marcher que pour deux clients. Merci donc d'exécuter deux fois ce fichier pour pouvoir pleinement profiter de ce jeu !
"""

import socket
import re
import sys
import select

# On lance le socket du client et on affiche le message du succès de la connexion
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect(('localhost', 1024))
print("On tente de se connecter au serveur...")
msg_recu = connexion_avec_serveur.recv(1024).decode()
print(msg_recu)

""" Vu que le joueur peut entrer plusieurs fois une commande en attendant que l'autre joueur 
ait entré la sienne, il faut trouver un moyen d'empêcher ces commandes suivantes, qui se 
retrouvent dans le 'standard input', de passer dans la fonction 'input'. Il faut donc vider
ce dernier. On va donc l'écouter avec la fonction select.select et, tant qu'il en existe,
le lire; ainsi le 'standard input' se videra et on pourra recommencer la boucle"""
while select.select([sys.stdin], [], [], 0.0) == ([sys.stdin], [], []):
	sys.stdin.read(1)

# On affiche le labyrinthe et les positions de départ
msg_recu = connexion_avec_serveur.recv(1024).decode()
print(msg_recu)
commencer = input("Entrez C pour commencer à jouer : \n")
while commencer.lower().startswith("c") is False:
	print("Je n'ai pas compris votre requête. Veuillez recommencer s'il vous plaît.\n")
	commencer = input("Entrez C pour commencer à jouer : \n")
connexion_avec_serveur.send(b"ok")
print(connexion_avec_serveur.recv(1024).decode())

# On vide à nouveau le standard input
while select.select([sys.stdin], [], [], 0.0) == ([sys.stdin], [], []):
	sys.stdin.read(1)

""" On crée une boucle principale qui ne se terminera que lorsque le serveur fermera les 
connexions"""
while True:
	direction = ""
	direction = input("> ")
	while direction == "" or direction.lower()[0] not in ["s", "n", "e", "o", "q"] and \
	re.match("^[pm]{1}[oesn]{1}", direction[0:2]) is None:
		print("\nJe n'ai pas compris votre requête. Veuillez recommencer. \
(Pour murer les portes ou passer les murs, vous devez aussi indiquer la direction (ex.:\
 pe).")
		direction = input("> ")
	connexion_avec_serveur.send(direction.encode())
	msg_recu = connexion_avec_serveur.recv(1024).decode()
	print(msg_recu)
	if msg_recu == "\nFermeture de la connexion\n":
		break

	""" On vide à nouveau le standard input pour pas qu'un joueur puisse déplacer son robot
plusieurs fois de suite"""
	while select.select([sys.stdin], [], [], 0.0) == ([sys.stdin], [], []):
		sys.stdin.read(1)

connexion_avec_serveur.close()
