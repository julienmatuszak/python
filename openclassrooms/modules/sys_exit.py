import sys
import signal

def fermer_programme(signal, frame):
	"""Fonction appelée quand vient l'heure de fermer notre programme"""
	print("C'est l'heure de la fermeture !")
	sys.exit(0)

signal.signal(signal.SIGINT, fermer_programme)

print("Le programme va boucler...")
while True: # Boucle infinie, True est toujours vrai
	continue