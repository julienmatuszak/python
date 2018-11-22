import pickle

score = {"joueur 1":5,"joueur 2":35,"joueur 3":20,"joueur 4":2,}

with open("donnees","wb") as fichier:
	mon_pickler = pickle.Pickler(fichier)
	mon_pickler.dump(score)

with open("donnees","rb") as fichier:
	mon_depickler = pickle.Unpickler(fichier)
	score_recupere = mon_depickler.load()
