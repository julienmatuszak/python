"""Pour gerer le temps, on importe le module time.
On va utiliser surtout la fonction time() de ce module qui renvoie le nombre \
de secondes ecoulees depuis le premier janvier 1970 (habituellement).
On va s'en servir pour calculer le temps mis par notre fonction pour \
s'executer"""

import time

def controler_temps(nb_secs):
	"""Controle le temps mis par une fonction pour s'executer.
	Si le temps d'execution est superieur a nb_secs, on affiche une alerte"""

	def decorateur(fonction_a_executer):
		"""Notre decorateur. C'est lui qui est appele directement LORS DE LA \
		DEFINITION de notre fonction (fonction_a_executer)"""

		def fonction_modifiee():
			"""Fonction renvoyee par notre decorateur. Elle se charge de \
			calculer le temps mis par la fonction a s'executer"""

			tps_avant = time.time() # Avant d'executer la fonction
			valeur_renvoyee = fonction_a_executer() # On execute la fonction
			tps_apres = time.time()
			tps_execution = tps_apres - tps_avant
			if tps_execution >= nb_secs:
				print("La fonction {0} a mis {1} pour s'executer".format(\
					fonction_a_executer, tps_execution))
			return valeur_renvoyee
		return fonction_modifiee
	return decorateur