import time

def controler_temps(nb_secs):
	"""Controle le temps mis par une fonction pour s'executer.
	Si le temps d'execution est superieur a nb_secs, on affiche une alerte"""

	def decorateur(fonction_a_executer):
		"""Notre decorateur. C'est lui qui est appele directement LORS DE LA \
		DEFINITION de notre fonction (fonction_a_executer)"""

		def fonction_modifiee(*parametres_non_nommes, **parametres_nommes):
			"""Fonction renvoyee par notre decorateur. Elle se charge de \
			calculer le temps mis par la fonction a s'executer"""

			tps_avant = time.time() # Avant d'executer la fonction
			ret = fonction_a_executer(*parametres_non_nommes, **parametres_nommes)
			tps_apres = time.time()
			tps_execution = tps_apres - tps_avant
			if tps_execution >= nb_secs:
				print("La fonction {0} a mis {1} pour s'executer".format(\
					fonction_a_executer, tps_execution))
			return ret
		return fonction_modifiee
	return decorateur