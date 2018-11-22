def intervalle(borne_inf, borne_sup):
	"""Generateur parcourant la serie des entiers entre borne_inf et borne_sup.

	Note: borne_inf doit etre inferieure a borne_sup"""

	if borne_inf > borne_sup:
		while borne_inf > borne_sup:
			yield borne_inf
			borne_inf -= 1
	else:
		borne_inf += 1
		while borne_inf < borne_sup:
			valeur_recue = (yield borne_inf)
			if valeur_recue is not None:
				borne_inf = valeur_recue #Notre generateur a recu quelque chose
			borne_inf += 1

	"""
	else:
		borne_inf += 1
		while borne_inf < borne_sup:
			yield borne_inf
			borne_inf += 1
	"""

def intervalle2(borne_inf, borne_sup):
	borne_inf += 1
	while borne_inf < borne_sup:
		valeur_recue = (yield borne_inf)
		if valeur_recue is not None:
			borne_inf = valeur_recue #Notre generateur a recu quelque chose
		borne_inf += 1
