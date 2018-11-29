"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text='Salut les zéros !')

# On affiche le label dans la fenetre
champ_label.pack()

# Bouton pour quitter la fenetre
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()

# Bouton pour creer du champ de texte
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()

# Cases a cocher
var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()

# Controler l'etat de la case a cocher
var_case.get()

# Boutons radio
var_choix = StringVar()

choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_bleu.pack()
choix_vert.pack()

var_choix.get()

# Listes deroulantes
liste = Listbox(fenetre)
liste.pack()
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")

# Pour afficher la selection
liste.curselection()

# Widgets apparaissant dans un cadre
cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenetre")
message.pack(side="top", fill=X)

# On démarre la boule Tkinter qui s'interrompt quand on ferme la fenêtre
fenetre.mainloop()
