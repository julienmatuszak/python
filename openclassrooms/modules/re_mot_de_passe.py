import re

chn_mdp = "^[A-Za-z0-9]{6,}$"
exp_mdp = re.compile(chn_mdp)
mot_de_passe = str()
while exp_mdp.search(mot_de_passe) is None:
	mot_de_passe = input("Tapez votre mot de passe : ")
	print("Désolé, votre mot de passe ne respecte pas \
les normes demandées. Veuillez le ressaisir.")