class Temp:
    """Classe contenant plusieurs attributs, dont un temporaire"""

    def __init__(self):
        """Le constructeur"""
        self.attribut_1 = "une valeur"
        self.attribut_2 = "une autre valeur"
        self.attribut_temporaire = 5

    def __getstate__(self):
        """Cette methode speciale renvoie le dictionnaire d'attributs\
        a serialiser"""
        dict_attr = dict(self.__dict__)
        dict_attr["attribut_temporaire"] = 0
        print(dict_attr)
        return dict_attr

    def __setstate__(self, dict_attr):
        """Methode appelee lors de la deserialisation de l'objet"""
        dict_attr["attribut_temporaire"] = 0
        self.__dict__ = dict_attr
        print(self.__dict__, dict_attr)
