"""
Ce fichier est l'exécutable python du premier client. Merci de le lancer suite à l'exécution de serveur.py.
Pour l'instant, l'application ne peut marcher que pour deux clients. Merci donc d'exécuter deux fois ce fichier pour pouvoir pleinement profiter de ce jeu !
"""

import socket
import re
import sys

# On lance le socket du client et on affiche le message du succès de la connexion
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect(('localhost', 1024))
print("On tente de se connecter au serveur...")
msg_recu = connexion_avec_serveur.recv(1024).decode()
print(msg_recu)

# On affiche le labyrinthe et les positions de départ
msg_recu = connexion_avec_serveur.recv(1024).decode()
print(msg_recu)
commencer = input("Entrez C pour commencer à jouer : \n")
while commencer.lower().startswith("c") is False:
	print("Je n'ai pas compris votre requête. Veuillez recommencer s'il vous plaît.\n")
	commencer = input("Entrez C pour commencer à jouer : \n")
connexion_avec_serveur.send(b"ok")
print(connexion_avec_serveur.recv(1024).decode())

""" On crée une boucle principale qui ne se terminera que lorsque le serveur fermera les 
connexions"""
while True:
	sys.stdin.flush()
	direction = ""
	direction = input("> ")
	sys.stdin.flush()
	while direction == "" or direction.lower()[0] not in ["s", "n", "e", "o", "q"] and \
	re.match("^[pm]{1}[oesn]{1}", direction[0:2]) is None:
		print("\nJe n'ai pas compris votre requête. Veuillez recommencer. \
(Pour murer les portes ou passer les murs, vous devez aussi indiquer la direction (ex.:\
 pe).")
		direction = input("> ")
	print("OK!")
	connexion_avec_serveur.send(direction.encode())
	print("ok!")
	msg_recu = connexion_avec_serveur.recv(1024).decode()
	if msg_recu == "\nFermeture de la connexion\n":	
		break
	else:
		print(msg_recu)
	print("ok")
	sys.stdin.flush()

connexion_avec_serveur.close()
