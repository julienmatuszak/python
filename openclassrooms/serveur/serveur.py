# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu, inclus dans le serveur.

Ce code est exécutable sur un système Unix, mais pas nécessairement sur Windows.

Exécutez-le avec Python pour lancer le serveur et la boucle principale du jeu.

Les autres fichiers sont:
- labyrinthe.py qui crée l'objet labyrinthe,
- carte.py qui crée l'objet carte,
- client.py qui permet aux joueurs de se connecter au serveur et de jouer la partie,
- unittest.py qui permet de faire des tests sur les différentes fonctionnalités du jeu.

Nota Bene: 
- pour pouvoir exécuter le jeu correctement, il faut aussi lancer deux terminaux 
différents qui feront office de clients. Merci donc d'exécuter également le fichier 
./client.py à partir de deux terminaux différents suite à l'exécution de ce fichier.
- Comme l'énoncé laissait une certaine liberté dans l'organisation des règles du 
jeu (à moins que je n'aie pas compris toutes 
les consignes), j'ai décidé qu'il n'y aurait un ordre dans le tour, c'est-à-dire que 
ça n'est pas le joueur qui jouera le plus vite qui se verra jouer en premier. J'ai 
aussi choisi de faire passer le tour quand le joueur 'fait une erreur'.
Enfin, percer un mur ou murer une porte compte pour un tour.
Signalons aussi que si un mur est percé ou une porte murée et que les deux joueurs se
sont entrechoqués, l'action de percer le mur ou de murer la porte reste conséquente.
"""

# On charge tous les modules nécessaires à l'exécution du programme
import os
import re
import socket
import select
from carte import Carte
from labyrinthe import Labyrinthe

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

""" C'est le serveur qui va choisir le numéro de labyrinthe mais on ne va pas l'afficher 
sur le terminal du serveur cette fois mais sur celui des clients"""
choix = input("\nEntrez un numéro de labyrinthe pour commencer à jouer : ")
while choix.isdigit() is False or int(choix)-1 not in range(len(cartes)):
	print("\nDésolé, votre choix est incorrect. Veuillez recommencer.")
	choix = input("\nEntrez un numéro de labyrinthe pour commencer à jouer : ")

# On lance le socket du serveur, ses oreilles et la limite pour qu'il décide de les fermer
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind(('', 1024))
print("On attend les clients.")
connexion_principale.listen(10)

""" Maintenant, notre serveur va attendre les deux clients. Une fois le client connecté,
 on lui envoie un message d'information"""
demarrage_du_jeu = True
clients_connectes = []
while demarrage_du_jeu:
	connexion_avec_client, infos_connexion = connexion_principale.accept()
	clients_connectes.append(connexion_avec_client)
	connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
	clients_connectes[0].send(bytes("Connexion établie avec le serveur.\nBienvenue, \
joueur 1.\nAttente d'un autre joueur.\n", 'utf-8'))
	while len(clients_connectes) < 2:
		connexion_avec_client, infos_connexion = connexion_principale.accept()
		clients_connectes.append(connexion_avec_client)
		""" Quand les deux joueurs sont connectés, on crée les objets-labyrinthes et on les
		 envoie à chacun des clients pour qu'ils s'affichent sur leurs terminaux"""
		if len(clients_connectes) == 2:
			clients_connectes[1].send(bytes("Connexion établie avec le serveur.\n", 'utf-8'))
			clients_connectes[0].send(bytes("Le joueur 2 s'est connecté.\n\n", 'utf-8'))
			connexions_demandees, wlist, xlist = select.select([connexion_principale], \
				[], [], 0.05)
			clients_connectes[1].send(bytes("Bienvenue, joueur 2.\n\n", 'utf-8'))
			chemin = "cartes/"+cartes[int(choix)-1].nom+"txt"
			with open(chemin, "r") as fichier:
				contenu = fichier.read()
				labyrinthe = cartes[int(choix)-1].labyrinthe
				labyrinthe_autre_chaine = labyrinthe.inverser_robots()

			"""Une fois qu'on a reçu les confirmations des deux clients, la prochaine étape 
			peut commencer"""
			pas_commencer = True
			msg_recu = []
			while pas_commencer and len(msg_recu) < 2:
				clients_a_lire = []
				try:
					clients_a_lire, wlist, xlist = select.select(clients_connectes, [],\
					 [], 0.05)
				except select.error:
					pass
				else:
					for client in clients_a_lire:
						msg_recu.append(client.recv(1024))
					if len(msg_recu) == 2:
						pas_commencer = False
			print("La partie commence !\n")
			clients_connectes[0].send(bytes("\n"+labyrinthe.chaine, 'utf-8'))
			clients_connectes[1].send(bytes("\n"+labyrinthe_autre_chaine, 'utf-8'))
			demarrage_du_jeu = False

""" Puis on implémente la boucle principale de façon un peu différente que dans le premier 
 TP, car il faut échanger les différents input entre clients et serveur."""
clients_liste_entiere = []
directions = []
clients_a_lire = []
while True:
	while len(directions) < 2:
		try:
			clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
		except select.error:
			pass
		else:
			for client in clients_a_lire:
				if client in clients_liste_entiere:
					client.recv(1024)
				else:
					clients_liste_entiere.append(client)
					directions.append(client.recv(1024).decode())


	# Vidage du socket si le client a entré plusieurs fois une commande


	""" On met les clients lus dans un tableau et on les range dans l'ordre pour organiser
 le tour  à tour, on fait la même chose avec les directions données par les joueurs."""
	if clients_liste_entiere != clients_connectes:
		client = clients_liste_entiere.pop(0)
		clients_liste_entiere.append(client)
		direction = directions.pop(0)
		directions.append(direction)

# On initialise le passage précédent pour le cas du passage d'une porte.
	labyrinthe.robot_passe = labyrinthe.robot
	labyrinthe.autre_robot_passe = labyrinthe.autre_robot

# On commence par les cas où seule un des points cardinaux est donné
	if directions[0].lower().startswith("s"):
		labyrinthe.message_robot, labyrinthe.robot = labyrinthe.sud(labyrinthe.robot)
	if directions[0].lower().startswith("n"):
		labyrinthe.message_robot, labyrinthe.robot = labyrinthe.nord(labyrinthe.robot)
	if directions[0].lower().startswith("e"):
		labyrinthe.message_robot, labyrinthe.robot = labyrinthe.est(labyrinthe.robot)
	if directions[0].lower().startswith("o"):
		labyrinthe.message_robot, labyrinthe.robot = labyrinthe.ouest(labyrinthe.robot)

# Ainsi que le cas de l'abandon
	if directions[0].lower().startswith("q"):
		if directions[1].lower().startswith("q"):
			clients_connectes[0].send(bytes("\nVous abandonnez tous les deux ! Il n'y \
a aucun gagnant. Dommage ! Au revoir !\n", 'utf-8'))
			clients_connectes[1].send(bytes("\nVous abandonnez tous les deux ! Il n'y \
a aucun gagnant. Dommage ! Au revoir !\n", 'utf-8'))
		else:
			clients_connectes[0].send(bytes("\nVous abandonnez ! Dommage ! Au revoir \
!\n", 'utf-8'))
			clients_connectes[1].send(bytes("\nLe joueur 1 abandonne ! Bravo, vous \
avez gagné !\n", 'utf-8'))
		break

# On continue avec la fonctionnalité 'percer un mur' (ou pas).
	if directions[0].lower().startswith("p"):
		labyrinthe.message_robot = labyrinthe.percer_mur(labyrinthe.robot, \
			directions[0].lower()[1])

# Même chose avec la fonctionnalité 'murer porte'.
	if directions[0].lower().startswith("m"):	
		labyrinthe.message_robot = labyrinthe.murer_porte(labyrinthe.robot, \
			directions[0].lower()[1])

# On refait la même chose pour l'autre robot.
	labyrinthe.message = ""
	if directions[1].lower().startswith("s"):
		labyrinthe.message_autre_robot, labyrinthe.autre_robot = labyrinthe.sud\
		(labyrinthe.autre_robot)
	if directions[1].lower().startswith("n"):
		labyrinthe.message_autre_robot, labyrinthe.autre_robot = labyrinthe.nord\
		(labyrinthe.autre_robot)
	if directions[1].lower().startswith("e"):
		labyrinthe.message_autre_robot, labyrinthe.autre_robot = labyrinthe.est\
		(labyrinthe.autre_robot)
	if directions[1].lower().startswith("o"):
		labyrinthe.message_autre_robot, labyrinthe.autre_robot = labyrinthe.ouest\
		(labyrinthe.autre_robot)
	if directions[1].lower().startswith("q"):
		if directions[0].lower().startswith("q"):
			clients_connectes[0].send(bytes("\nLe joueur 2 abandonne ! Bravo, vous avez \
gagné !\n", 'utf-8'))
			clients_connectes[1].send(bytes("\nVous abandonnez ! Dommage ! Au revoir \
!\n", 'utf-8'))
		break
	if directions[1].lower().startswith("p"):	
		labyrinthe.message_autre_robot = labyrinthe.percer_mur(labyrinthe.autre_robot, \
			directions[1].lower()[1])
	if directions[1].lower().startswith("m"):	
		labyrinthe.message_autre_robot = labyrinthe.murer_porte(labyrinthe.autre_robot, \
			directions[1].lower()[1])

	""" On gère le cas où les deux robots se trouvent au même endroit après leur décision 
(spoiler: ils reviennent à leurs endroits précédents respectifs)."""
	if labyrinthe.robot == labyrinthe.autre_robot:
		labyrinthe.robot = labyrinthe.robot_passe
		labyrinthe.autre_robot = labyrinthe.autre_robot_passe
		labyrinthe.message_robot = "Vous vous êtes entrechoqués ! Vous revenez à vos \
positions respectives.\n"
		labyrinthe.message_autre_robot = "Vous vous êtes entrechoqués ! Vous revenez à vos \
positions respectives.\n"

# Gestion du cas où un des robots atteint la sortie.
	if labyrinthe.robot == labyrinthe.sortie:
		labyrinthe.chaine = labyrinthe.deplacer()
		labyrinthe_autre_chaine = labyrinthe.inverser_robots()
		clients_connectes[0].send(bytes("\nVous avez atteint la sortie en premier ! Bravo, \
vous avez gagné !\n\n"+labyrinthe.chaine, 'utf-8'))
		clients_connectes[1].send(bytes("\nLe joueur 1 a atteint la sortie en premier ! \
Vous avez perdu ! Au revoir !\n\n"+labyrinthe_autre_chaine, 'utf-8'))
		break

	if labyrinthe.autre_robot == labyrinthe.sortie:
		labyrinthe.chaine = labyrinthe.deplacer()
		labyrinthe_autre_chaine = labyrinthe.inverser_robots()
		clients_connectes[0].send(bytes("\nLe joueur 2 a atteint la sortie en premier ! \
Vous avez perdu ! Au revoir !\n\n"+labyrinthe.chaine, 'utf-8'))
		clients_connectes[1].send(bytes("\nVous avez atteint la sortie en premier ! Bravo, \
vous avez gagné !\n\n"+labyrinthe_autre_chaine, 'utf-8'))
		break

# Modification des chaînes et envoi aux clients.
	labyrinthe.chaine = labyrinthe.deplacer()
	labyrinthe_autre_chaine = labyrinthe.inverser_robots()
	clients_connectes[0].send(bytes("\n"+labyrinthe.message_robot+"\n"+labyrinthe.chaine, \
		'utf-8'))
	clients_connectes[1].send(bytes("\n"+labyrinthe.message_autre_robot+"\n"+\
		labyrinthe_autre_chaine, 'utf-8'))

# Réinitalisation des variables locales.
	directions = []
	clients_a_lire = []
	clients_liste_entiere = []
	labyrinthe.message = ""


"""Une fois le jeu terminé, on ferme toutes les connexions des joueurs et la connexion 
principale et le tour est joué !"""
print("Fermeture des connexions\n")
for client in clients_connectes:
	client.send(bytes("\nFermeture de la connexion\n", 'utf-8'))
	client.close()
connexion_principale.close()

"""
AMELIORATIONS POSSIBLES:
- simplifier le code:
      . il faudrait définir une fonction "rafraîchir chaîne" vu le nombre de fois où on 
      est obligés de le faire.
      . en particulier à cause de la redondance des directions (peut-être en utilisant 
      des décorateurs)
      . pour gagner du temps dans la reconstruction des chaînes (trop de reconstructions
      pour une seule action)
      . utiliser la méthode spécifique __repr__ pour afficher la chaîne.
- comprendre et réparer les problèmes associés au serveur:
      . lorsqu'un troisième client veut se connecter, plutôt que d'afficher un message "on
      tente de se connecter",
on indique que deux joueurs sont déjà connectés et qu'il faudra recommencer plus tard.
      . lorsqu'il y a plusieurs tentatives de lancer le serveur proches de suite ou bien 
      lorsque les données envoyées
des deux clients se suivent de près, il y a des problèmes d'ordre d'affichage des 
informations.
      . même chose pour la fermeture des connexions.
- faire apparaître les labyrinthes dans des fenêtres séparées avec le module tkinter.
- on peut imaginer, plutôt que de faire jouer les joueurs tour à tour, de faire du 
"threading", c'est à celui qui ira le plus vite à la sortie, un peu comme les MMORPG 
actuels. Mais ça demande sans doute de gros efforts de proga.
- il faudrait aussi modifier le code de manière à faire un vrai mode multi-joueurs 
(plus de 2) mais ça demande de repenser entièrement le code.
- autres règles possibles: on peut également imaginer, pour des raison stratégiques, 
volontairement passer son tour, par exemple avec la commande "espace".
"""