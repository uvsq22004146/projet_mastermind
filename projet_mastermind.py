import tkinter as tk


LARGEUR = 700
HAUTEUR = 700

l_case = 100

comb_secrète = []


def placer_pion(event):
    if event.y > 600 :
        '''placement d'un pion de la combinaison secrète'''
        for i in range(4):
            if i*600 < event.x < (i+1)*600:
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


racine.mainloop()