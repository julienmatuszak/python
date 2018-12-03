# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

from random import choice

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, chaine, robot, obstacles, sortie, taille_ligne, portes, limites,\
     autre_robot):
        self.chaine = chaine
        self.robot = robot
        self.obstacles = obstacles
        self.sortie = sortie
        self.taille_ligne = taille_ligne
        self.portes = portes
        self.limites = limites
        self.autre_robot = autre_robot
        self.message = ""
        self.message_robot = ""
        self.message_autre_robot = ""
        self.robot_passe = 0
        self.autre_robot_passe = 0

    """ Changement de la position des robots selon les 4 directions données et gestion du cas
où le mur bloque sur le passage."""

    def sud(self, position):
        position += self.taille_ligne
        if self.mur_bloque(position):
            position -= self.taille_ligne
            self.message += "Le mur vous bloque ! Vous pourrez y percer une porte au \
prochain tour avec la formule magique 'p + direction souhaitée'.\n"
        else:
            self.message += "Vous vous êtes déplacé(e) vers le sud !\n"
        return self.message, position

    def nord(self, position):
        position -= self.taille_ligne
        if self.mur_bloque(position):
            position += self.taille_ligne
            self.message += "Le mur vous bloque ! Vous pourrez y percer une porte au \
prochain tour avec la formule magique 'p + direction souhaitée'.\n"
        else:
            self.message = "Vous vous êtes déplacé(e) vers le nord !\n"
        return self.message, position

    def ouest(self, position):
        position -= 1
        if self.mur_bloque(position):
            position += 1
            self.message += "Le mur vous bloque ! Vous pourrez y percer une porte au \
prochain tour avec la formule magique 'p + direction souhaitée'.\n"
        else:
            self.message += "Vous vous êtes déplacé(e) vers l'ouest !\n"
        return self.message, position

    def est(self, position):
        position += 1
        if self.mur_bloque(position):
            position -= 1
            self.message += "Le mur vous bloque ! Vous pourrez y percer une porte au \
prochain tour avec la formule magique 'p + direction souhaitée'.\n"
        else:
            self.message += "Vous vous êtes déplacé(e) vers l'est !\n"
        return self.message, position

    def mur_bloque(self, position):
        if position in self.obstacles:
            return True
        else:
            return False

    # Modification de la chaîne selon les choix faits.
    def deplacer(self):
        liste = list(self.chaine)
        liste[self.chaine.index("X")] = " "
        liste[self.chaine.index("x")] = " "
        if self.robot_passe in self.portes:
            liste[self.robot_passe] = "."
        if self.autre_robot_passe in self.portes:
            liste[self.autre_robot_passe] = "."
        liste[self.robot] = "X"
        liste[self.autre_robot] = "x"
        self.chaine = "".join(liste)
        return self.chaine

    # Modification de la chaîne pour l'envoyer au joueur 2.
    def inverser_robots(self):
        if self.autre_robot < self.robot:
            return self.chaine[0:self.autre_robot] + "X" + self.chaine[self.autre_robot+1:\
            self.robot] + "x" + self.chaine[self.robot+1: len(self.chaine)]
        if self.autre_robot > self.robot:
            return self.chaine[0:self.robot] + "x" + self.chaine[self.robot+1: self.\
            autre_robot] + "X" + self.chaine[self.autre_robot+1: len(self.chaine)]

    """PERCER UN MUR.
Gestion du cas où la direction donne dans les limites du labyrinthe."""
    def mur_limites(self, position, direction):
        if (position + 1 in self.limites and direction == "e") or (position - 1 in \
            self.limites and direction =="o") or (position + self.taille_ligne in \
            self.limites and direction == "s") or (position - self.taille_ligne in \
            self.limites and direction == "n"):
            return True
        else:
            return False

    # Vérification de la présence d'un mur à percer dans la direction souhaitée.
    def presence_mur(self, position, direction):
        if (position + 1 in self.obstacles and position + 1 not in self.limites and \
            direction == "e") or (position - 1 in self.obstacles and position - 1 not \
            in self.limites and direction =="o") or (position + self.taille_ligne \
            in self.obstacles and position + self.taille_ligne not in self.limites and \
            direction == "s") or (position - self.taille_ligne in self.obstacles and \
            position - self.taille_ligne not in self.limites and direction == "n"):
            return True
        else:
            return False

    """ Boucle principale de la fonction: renvoi du message selon le cas et modification de
la chaîne le cas échéant."""
    def percer_mur(self, position, direction):
        if self.mur_limites(position, direction):
            self.message += "\nVous avez atteint les limites du labyrinthe et vous ne \
pouvez pas percer les murs en cet endroit. Vous perdez votre tour !\n"
        elif self.presence_mur(position, direction) is False:
            self.message += "\nVous n'avez aucun mur à détruire ! Vous perdez votre \
tour !\n"
        else:
            self.message += "\nVous avez percé un mur !\n"
            liste = list(self.chaine)
            if direction == "e":
                liste[position + 1] = "."
                self.obstacles.remove(position + 1)
                self.portes.append(position + 1)
            if direction == "n":
                liste[position - self.taille_ligne] = "."
                self.obstacles.remove(position - self.taille_ligne)
                self.portes.append(position - self.taille_ligne)
            if direction == "o":
                liste[position - 1] = "."
                self.obstacles.remove(position - 1)
                self.portes.append(position - 1)
            if direction == "s":
                liste[position + self.taille_ligne] = "."
                self.obstacles.remove(position + self.taille_ligne)
                self.portes.append(position + self.taille_ligne)
            self.chaine = "".join(liste)
        return self.message

    """MURER UNE PORTE
Vérification de la présence d'une porte à murer dans la direction souhaitée."""
    def presence_porte(self, position, direction):
        if (position + 1 in self.portes and direction == "e") or (position - 1 in \
            self.portes and direction =="o") or (position + self.taille_ligne in \
            self.portes and direction == "s") or (position - self.taille_ligne in \
            self.portes and direction == "n"):
            return True
        else:
            return False

    """ Boucle principale de la fonction: renvoi du message selon le cas et modification de 
la chaîne le cas échéant. """
    def murer_porte(self, position, direction):
        if self.presence_porte(position, direction) is False:
            self.message += "\nVous n'avez aucune porte à murer là ! Vous perdez votre\
tour !\n"
        else:
            self.message += "\nVous avez muré une porte !\n"
            liste = list(self.chaine)
            if direction == "e":
                liste[position + 1] = "O"
                self.portes.remove(position + 1)
                self.obstacles.append(position + 1)
            if direction == "n":
                liste[position - self.taille_ligne] = "O"
                self.portes.remove(position - self.taille_ligne)
                self.obstacles.append(position - self.taille_ligne)
            if direction == "o":
                liste[position - 1] = "O"
                self.portes.remove(position - 1)
                self.obstacles.append(position - 1)
            if direction == "s":
                liste[position + self.taille_ligne] = "O"
                self.portes.remove(position + self.taille_ligne)
                self.obstacles.append(position + self.taille_ligne)
            self.chaine = "".join(liste)
        return self.message
