def singleton(classe_definie):
	instances = {} # Dictionnaire de nos instances singletons
	def get_instance():
		if classe_definie not in instances:
			# On cree notre premier objet de classe_definie
			instances[classe_definie] = classe_definie()
		return instances[classe_definie]
	return get_instance