class DictionnaireOrdonne:
    """Notre dictionnaire ordonne. L'ordre des donnees est maintenu et il peut \
    donc, contrairement aux dictionnaires usuels, etre trie ou voir l'ordre de \
    ses donnees inversees"""

    def __init__(self, base={}, **donnees):
        """Constructeur de notre objet. Il peut ne prendre aucun parametre, \
        (dans ce cas, le dictionnaire sera vide) ou construire un dictionnaire \
        rempli grace :
        - au dictionnaire 'base' passe en premier parametre ;
        - aux valeurs que l'on retrouve dans 'donnees'."""

        self._cles = [] # Liste contenant nos cles
        self._valeurs = [] # Liste contenant les valeurs correspondantes

        #On verifie que 'base' est un dictionnaire exploitable
        if type(base) not in (dict, DictionnaireOrdonne):
            raise TypeError ( "Le type attendu est un dictionnaire (usuel ou \
                ordonne")

        # On recupere les donnees de 'base'
        for cle in base:
            self[cle] = base[cle]

        # On recupere les donnees de 'donnees'
        for cle in donnees:
            self[cle] = donnees[cle]

    def __repr__(self):
        """Representation de notre objet. C'est cette chaine qui sera affichee \
        quand on saisit directement le dictionnaire dans l'interpreteur, ou en \
        utilisant la fonction 'repr' """
        chaine = "{"
        premier_passage = True
        for cle, valeur in self.items():
            if not premier_passage:
                chaine += ", " # On ajoute la virgule comme separateur
            else:
                premier_passage = False
            chaine += repr(cle) + ": " + repr(valeur)
        chaine += "}"
        return chaine

    def items(self):
        """Renvoie un generateur contenant les couples (cle, valeur)"""
        for i, cle in enumerate(self._cles):
            valeur = self._valeurs[i]
            yield (cle, valeur)

    def keys(self):
        """Cette methode renvoie la liste des cles"""
        return list(self._cles)

    def values(self):
        """Cette methode renvoie la liste des valeurs"""
        return list(self._valeurs)

    def __setitem__(self, cle, valeur):
        """Methode speciale appelee quand on cherche a modifier une cle presente\
        dans le dictionnaire. SI la cle n'est pas presente, on l'ajoute a la fin 
        du dictionnaire"""

        if cle in self._cles:
            indice = self._cles.index(cle)
            self._valeurs[indice] = valeur
        else:
            self._cles.append(cle)
            self._valeurs.append(valeur)

    def __str__(self):
        """Fonction appelee quand on souhaite afficher le dictionnaire grace a la\
        fonction 'print' ou le convertir en chaine grace au constructeur 'str'.
        On redirige sur __repr__"""

        return repr(self)

    def __contains__(self, cle):
        """Renvoie True si la cle est dans la liste des cles, False sinon"""
        return cle in self._cles

    def sort(self):
        """Methode permettant de trier le dictionnaire en fonction de ses cles"""
        # On trie les cles
        cles_triees = sorted(self._cles)
        # On cree une liste de valeurs, encore vide
        valeurs = []
        # On parcourt ensuite la liste des cles triees
        for cle in cles_triees:
            valeur = self[cle]
            valeurs.append(valeur)
        # Enfin, on met a jour notre liste de cles et de valeurs
        self._cles = cles_triees
        self._valeurs = valeurs

    def __getitem__(self, cle):
        """Renvoie la valeur correspondant a la cle si elle existe, leve\
        une exception KeyError sinon"""

        if cle not in self._cles:
            raise KeyError( "La cle {0} ne se trouve pas dans le diction\
                naire".format(cle))
        else:
            indice = self._cles.index(cle)
            return self._valeurs[indice]

    def __iter__(self):
        """Methode de parcours de l'objet. On renvoie l'iterateur des cles."""
        return iter(self._cles)

    def __delitem__(self, cle):
        """Methode appelee quand on souhaite supprimer un cle"""
        if cle not in self._cles:
            raise KeyError("La cle {0} ne se trouve pas dans le diction\
naire".format(cle))
        else:
            indice = self._cles.index(cle)
            del self._cles[indice]
            del self._valeurs[indice]

    def __len__(self):
        """Renvoie la taille du dictionnaire"""
        return len(self._cles)

    def reverse(self):
        """Inversion du dictionnaire"""
        # On cree deux listes vides qui contiendront le nouvel ordre des cles
        # et valeurs
        cles = []
        valeurs = []
        for cle, valeur in self.items():
            # On ajoute les cles et valeurs au debut de la liste
            cles.insert(0, cle)
            valeurs.insert(0, valeur)
        # On met ensuite a jour nos listes
        self._cles = cles
        self._valeurs = valeurs

    def __add__(self, autre_objet):
        """On renvoie un nouveau dictionnaire contenant les deux dictionnaire mis \
        bout a bout (d'abord self puis autre_objet)"""

        if type(autre_objet) is not type(self):
            raise TypeError("Impossible de concatener {0} et {1}".format\
                (type(self), type(autre_objet)))
        else:
            nouveau = DictionnaireOrdonne()

            # On commence par copier self dans le dictionnaire
            for cle, valeur in self.items():
                nouveau[cle] = valeur

            # On copie ensuite notre objet
            for cle, valeur in autre_objet.items():
                nouveau[cle] = valeur
            return nouveau
