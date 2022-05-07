"""import tkinter as tk


LARGEUR = 700
HAUTEUR = 700

l_case = 100

comb_secrète = []


def placer_pion(event):
    if event.y > 600 :
        '''placement d'un pion de la combinaison secrète'''
        for i in range(4):
            if i*l_case < event.x < (i+1)*l_case:
                if len(comb_secrète) < 4:
                    couleur = input("Placer un pion")
                    pion = plateau.create_oval((i*l_case + 10, HAUTEUR-l_case + 10), 
                                                ((i+1)*l_case - 10, HAUTEUR-10), fill=couleur)
    elif event.y < 500:
        '''placement d'un pion d'une combinaison d'essai'''





racine = tk.Tk()
plateau = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)
plateau.grid()
racine.grid()

for i in range(4):
    case = plateau.create_rectangle((i*l_case, HAUTEUR-l_case), ((i+1)*l_case, HAUTEUR))

racine.bind("<Button-1>", placer_pion)


racine.mainloop()"""

########################################################
# GROUPE 4 MI TD3                                      #
# MENNOUR THOMAS                                       #
# ABALIL YASMINE                                       #
# ELIES ROMAIN                                         #
# PEMBELE GAEL                                         #
# https://github.com/uvsq22004146/projet_mastermind.git#
########################################################

#IMPORT DES BIBLIOTHEQUES
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
import random
from functools import partial
from tkinter.messagebox import showerror, showinfo

from matplotlib import colors

#CREATION DES VARIABLES GLOBALES


code_secret = []
nb_essai = 0
code_essai = []
col = ""
button_pressed = True

#FONCTIONS

#Cette fonction génère aléatoirement un code secret
def aletoire_code_secret() :
    list_colors = ["yellow", "red", "green", "blue"]
    while len(code_secret) < 4:
        code_secret.append(random.choice(list_colors))
        print(code_secret)

#Cette fonction permet au joueur 2 de saisir un code et vérifie si celui ci correspond au code secret
def essai_joueur():
    global nb_essai
    nb_essai += 1
    if verification_code():
        return True
    else:
        print("Nouvelle tentative")
        return False
    #On vérifie que le code saisi correspond au code secret
    nb_essai = nb_essai + 1

#Fonction qui verifie si la combinaison entré est la bonne
def verification_code():
    if pions_bien_places()==4 and pions_mal_places() == 0:
        return True
        print("Gagné")
    else:
        print(pions_bien_places())
        print(pions_mal_places())
        print("Mal placé")
        return False

#Fontion qui renvoie le nombre de pions bien placés
def pions_bien_places():
    global correct_colors
    correct_colors = 0
    for couleur in code_secret:
        for couleur_essai in code_essai:
            if couleur == couleur_essai:
                correct_colors += 1
    return correct_colors

"""
Cette méthode permet de compter combien de pions sont mal placés 
On parcourt le code saisi par l'utilisateur 2
Pour chaque couleur, on vérifie si la couleur existe dans le code secret (saisi par l'utilisateur 1)
Si elle existe on récupère son index/position
Si les positions sont différentes alors le pion est mal placé
"""
#Fonction qui permet de savoir le nombre de pions mal placé
def pions_mal_places():
    global incorrects_pions
    incorrects_pions = 0
    for idx,couleur_essai in code_essai:
        if couleur_essai in code_secret:
            print("la couleur existe")
            index = code_secret.index(couleur_essai)
            if idx != index:
                print("Pion mal placé")
                incorrects_pions += 1
    return incorrects_pions

#Fonction qui verrouille le code du Joueur 1 et qui fait passer la main au Joueur 2
def validation_du_code():
    if len(code_secret) < 4:
        showinfo(title="NOT COMPLETE", message="Votre code secret n'est pas complet, veuillez saisir quatres couleurs pour votre code")
    else:
        showinfo(title="THE GAME BEGIN",message=" Le Joueur 1 a validé la combinaison de son code secret!"
                                                " C'est au tour du joueur 2 de faire son entrée et d'essayer"
                                                " de trouver cette combinaison.")

        for c in racine.winfo_children():
            c.destroy()
        racine.geometry("1250x630")
        canvas = tk.Canvas(racine, height=630, width=1250)
        canvas.grid()
        zonejaune= canvas.create_oval(1240,5,1100,120, fill="yellow", outline="yellow")
        zonerouge = canvas.create_oval(1240,125,1100,240, fill="red", outline="red")
        zonevert = canvas.create_oval(1240,245,1100,360, fill="green", outline="green")
        zonebleue = canvas.create_oval(1240,365,1100,480,fill="blue", outline="blue")


def placer_pion(event):
    global list_colors, code_essai
    list_colors = ["yellow", "red", "green", "blue"]
    nb_pions_places = len(code_essai)
    if event.x > 1100 :
            for i in range(3):
                if 5 + 120*i < event.y < 5 + 120*(i+1):
                    color = list_colors[i]
                    code_essai.append(color)
                    pion = canvas.create_oval(10+120*(nb_essai), 5+120*(nb_pions_places), 
                                                130*(nb_essai), 125+120*(nb_pions_places+1), fill=color)
                    print(code_essai)

def affichage_nb_pions_bien_mal_places():
    for i in range(incorrects_pions):
        pion_rouge = canvas.create_oval(120*(nb_essai), 630-20*i, 120*(nb_essai)+20, 630)
    for i in range(correct_colors):
        pion_blanc = canvas.create_oval(120*(nb_essai)+40, 630-20*i, 120*(nb_essai)+60, 630)


#Cette fonction permet de choisir entre une partie à 2 ou une partie à 1
def choix_type_partie(valeur):
    global code_secret
    #Suppresion de l'ancien canvas
    #Si on choisit la partie à 2 utilisateurs
    if valeur == 1:

        showinfo(title=" MASTERMIND'S RULES", message="Bienvenue sur le jeu Mastermind le but du jeu est que le JOUEUR 2 trouve la combinaison secrète que le JOUEUR 1 a entré en premier lieu "
                                                      "avec un nombre limité d'essai. Des boutons de couleurs s'afficheront pres de la combinaison entrée pour qu'il puisse savoir lesquelles de "
                                                      "ses couleurs sont dans la combinaison et lesquelles sont placés correctement")
        showinfo(title=" PLAYER 1", message="C'est au tour du joueur 1 d'entrer sa combinaison secrète !")
        for c in racine.winfo_children():
            c.destroy()
        racine.geometry("450x400")

        label_choix_couleur = tk.Label(racine, text="Choissisez une couleur").grid(row = 1, column=0)
        mon_choix1 = Combobox(racine,value=("rouge","vert", "jaune", "bleu"), textvariable=selected_color,state="readonly").grid(row = 1, column= 1)
        boutoncouleur = tk.Button(racine, text = "Ok", command=partial(saisi_code_secret, code_secret)).grid(row=1, column=2)
        bouton_valider = tk.Button(racine, text= "Valider votre combinaison", command= validation_du_code).grid(row=2, column=1)
        bouton_annuler =tk.Button(racine, text="Annuler", command=annuler_code).grid(row=3, column=1)
        label_code_secret = tk.Label(racine, textvariable = selected_code_secret).grid(row =5, column=1)
        #Si on choisit la partie à 1 utilisateur
    else:
        aletoire_code_secret()
    #showinfo(title="PLAYER 2", message=" Maintenant, c'est au tour du joueur 2 d'entrer la combinaison qui pourrait être la bonne !")
    """while nb_essai < 10 and essai_joueur() != True:
        essai_joueur()"""

#fonction: annulation du code pour en generer un nouveau si l'utilisateur se trompe
def annuler_code():
    global code_secret
    code_secret.clear()
    showinfo(title="RETRY", message="Joueur 1, veuillez entrez un nouveau code secret")

#Cette fonction récupère le code secret saisi par l'utilisateur
def saisi_code_secret(code):
    if len(code) < 4 :
        if selected_color.get():
            #On récupère la valeur saisie par l'utilisateur et on l'enregistre
            code.append(selected_color.get())
            print(code)
            selected_code_secret.set(code)
        else:
            #Affichage d'un message d'erreur
            print("Aucune valeur n'a été saisie ")
            showerror(title= "Code secret", message = "Aucune valeur n'a été saisie")
    #L'utilisateur a fini de saisir son code secret
    else:
        #Appel de la fonction qui permet à l'utilisateur 2 de jouer
        showerror(title="NO MORE SPACE", message= "Vous avez atteint la limite de couleurs dans votre combinaison")
        print("Tableau plein")
        #Suppression du bouton OK
        boutoncouleur(state=DISABLED)
        #Création du bouton "Vérifier votre combinaison"
    #while nb_essai < 10:
    #showinfo(title="PLAYER 2", message=" Maintenant, c'est au tour du joueur 2 d'entrer la combinaison qui pourrait être la bonne !")
    #essai_joueur()

"""def affiche_couleur_joueur1():
    canvas.config(height=450, width=540)
    if "rouge" in code_secret:
        diam=70
        A=(a,b)=(50, 80)
        B=(a+diam, b+diam)
        canvas.create_oval(A, B, fill='red')"""


######    CREATION DE LA FENETRE DU JEU     ######



racine=tk.Tk()
racine.title("Mastermind")
canvas = tk.Canvas(racine)

#INTERFACE CODE SECRET
selected_color = tk.StringVar()
selected_code_secret = tk.StringVar()

#LABELS
label_choix_couleur = tk.Label(racine, text="Choissisez une couleur")
label_interface_debut = tk.Label(racine, text = "MASTERMIND", font =("Broadway", "58")).grid(row = 0, column= 2)
label_bienvenue_debut = tk.Label(racine, text="Bienvenue sur le jeu MASTERMIND. Choisissez le mode de joueur de votre choix! ", font=("Sitka Banner","12")).grid(row =1, column = 2)
label_code_secret = tk.Label(racine, textvariable=selected_code_secret)

#DEROULEUR CHOIX COULEUR
mon_choix1 = Combobox(racine,value=("rouge","vert", "jaune", "bleu"), textvariable=selected_color,state="readonly")

#BOUTONS
bouton_partie_1 = tk.Button(racine, text="Mode 2 joueurs",font=("Broadway","20"), command=partial(choix_type_partie, 1)).grid(row = 5, column=3)
bouton_partie_2 = tk.Button(racine, text="Mode 1 joueur",font=("Broadway","20"), command=partial(choix_type_partie, 2)).grid(row = 5, column= 0)
boutoncouleur = tk.Button(racine, text = "Ok", command=partial(saisi_code_secret, code_secret))
bouton_valider = tk.Button(racine, text= "Valider votre combinaison", command= validation_du_code)
bouton_annuler = tk.Button(racine, text="Annuler", command=annuler_code)

racine.bind("<Button-1>", placer_pion)

#LANCEMENT DE LA FENETRE
racine.mainloop()