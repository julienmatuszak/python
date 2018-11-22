def controler_types(*a_args, **a_kwargs):
	"""On attend en parametres du decorateur les types souhaites. On accepte\
	une liste de parametres indetermines, etant donne que notre fonction \
	definie pourra etre appelee avec un nombre variable de parametres et que \
	chacun doit etre controle"""

	def decorateur(fonction_a_executer):
		"""Notre decorateur. Il doit renvoyer fonction_modifiee"""
		def fonction_modifiee(*args, **kwargs):
			"""Notre fonction modifiee. Elle se charge de controler \
			les types qu'on lui passe en parametres"""

			# La liste des parametres attendus (a_args) doit etre de meme \
			# Longueur que celle recue (args)
			if len(a_args) != len(args):
				raise TypeError("Le nombre d'arguments attendu n'est pas egal" \
				" au nombre recu")
			#On parcourt la liste des arguments recus et non nommes
			for i, arg in enumerate(args):
				if a_args[i] is not type(args[i]):
					raise TypeError("L'argument {0} n'est pas du type "\
						"{1}".format(i, a_args[i]))

			# On parcourt a present la liste des parametres recus et nommes
			for cle in kwargs:
				if cle not in a_kwargs:
					raise TypeError("L'argument {0} n'a aucun type "\
						"precise".format(repr(cle)))
				if a_kwargs[cle] is not type(kwargs[cle]):
					raise TypeError("L'argument {0} n'est pas de type"\
						"{1}".format(repr(cle), a_kwargs[cle]))
			return fonction_a_executer(*args, **kwargs)
		return fonction_modifiee
	return decorateur