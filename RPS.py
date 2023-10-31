import tkinter as tk 
import random
from PIL import Image, ImageTk

# création de la fenetre principal
fenetre = tk.Tk()
fenetre.title("Shi, Fu, Mi!")
fenetre.geometry("625x408")


# Fonction qui choisit au hasard pour l'ordi
def computer_choice():
    choices = ["Pierre", "Feuille", "Ciseaux"]
    return random.choice(choices)




#fonction qui permet de lancer le jeu
def play(user_choice):
    computer = computer_choice()

    # Condition qui determine le gagnant
    if user_choice == computer:
        result_var.set("Egalité!")
    elif (
        (user_choice == "Pierre" and computer == "Ciseaux")
        or (user_choice == "Feuille" and computer == "Pierre")
        or (user_choice == "Ciseaux" and computer == "Feuille")
        ):
        result_var.set("Vous avez gagné!")
        player_score_var.set(player_score_var.get() + 1)

    else:
        result_var.set("Vous avez perdu!")
        comp_score_var.set(comp_score_var.get() + 1)



    # Charger les images
    user_img_label.config(image=get_image(user_choice))
    computer_img_label.config(image=get_image(computer))

    # Ajouter les choix a l'historique (du plus racent au plus anciens)
    history_listbox.insert(0, f"Vous: {user_choice} - Ordi: {computer}")

    final_score()


# Permet de determiner un gagnant et de stopper la partie
def final_score():
    
    if player_score_var.get() >= 10:
        victoire.config(text="Victoire!")
        img_victoire.config(image=victoire_gif)

        rock_button.config(state=tk.DISABLED)
        paper_button.config(state=tk.DISABLED)
        scissor_button.config(state=tk.DISABLED)
    elif comp_score_var.get() >= 10:
        victoire.config(text="Défaite!")    
        img_victoire.config(image=defaite_gif)

        rock_button.config(state=tk.DISABLED)
        paper_button.config(state=tk.DISABLED)
        scissor_button.config(state=tk.DISABLED)


# Afficher une image en fonction du choix
def get_image(choice):
    if choice == "Pierre":
        return pierre_png
    elif choice == "Feuille":
        return feuille_png
    else:
        return ciseaux_png 
    



# Liaison des boutons au touche du clavier
def key_press(e):
    # Si joueur < 10 ET computer < 10
    if player_score_var.get() < 10 and comp_score_var.get() < 10:
        if e.char.lower() == "p":
            play("Pierre")
        elif e.char.lower() == "f":
            play("Feuille")
        elif e.char.lower() == "c":
            play("Ciseaux")

fenetre.bind('<Key>', key_press)



# Définition des variables
result_var = tk.StringVar()
player_score_var = tk.IntVar()
comp_score_var = tk.IntVar()


# Charger les images
pierre_png = ImageTk.PhotoImage(Image.open("./images/pierre.png"))
feuille_png = ImageTk.PhotoImage(Image.open("./images/feuille.png"))
ciseaux_png = ImageTk.PhotoImage(Image.open("./images/ciseaux.png"))
chargement_png = ImageTk.PhotoImage(Image.open("./images/chargement.png"))
victoire_gif = ImageTk.PhotoImage(Image.open("./images/victoire.png"))
defaite_gif = ImageTk.PhotoImage(Image.open("./images/defaite.png"))







# Création des widget avec les images
titre = tk.Label(fenetre, text="SHI, FU, MI", font=("arial", 30))
titre.place(x=80, y=10)
user_label = tk.Label(fenetre, text="Choisissez")
user_label.place(x=153, y=240)

rock_button = tk.Button(fenetre, image=pierre_png, command=lambda : play("Pierre")) # lambda transmet le paramettre
rock_button.place(x=10, y=260)

paper_button = tk.Button(fenetre, image=feuille_png, command=lambda : play("Feuille")) # lambda transmet le paramettre
paper_button.place(x=130, y=290)

scissor_button = tk.Button(fenetre, image=ciseaux_png, command=lambda : play("Ciseaux")) # lambda transmet le paramettre
scissor_button.place(x=250, y=260)








# Etiquette pour afficher les images joué
user_img_label = tk.Label(fenetre, image=None) # Pas d'image
user_img_label.place(x=70, y=110)

computer_img_label = tk.Label(fenetre, image=None)
computer_img_label.place(x=200, y=110)

result_label = tk.Label(fenetre, textvariable=result_var, font=("arial", 15))
result_label.place(x=380, y=10,)

# Création d'une frame pour les scores
score_frame = tk.Frame(fenetre)
score_frame.place(x=400, y=365)

player_score_label = tk.Label(score_frame, text="Score J1: ")
player_score_label.pack(side=tk.LEFT, pady=5)
player_score_display = tk.Label(score_frame, textvariable=player_score_var)
player_score_display.pack(side=tk.LEFT, pady=5)

comp_score_label = tk.Label(score_frame, text="| Score COMP: ")
comp_score_label.pack(side=tk.LEFT, pady=5)
comp_score_display = tk.Label(score_frame, textvariable=comp_score_var)
comp_score_display.pack(side=tk.LEFT, pady=5)

historique_label = tk.Label(fenetre, text="Historique des coups: ")
historique_label.place(x=400, y=183)

history_listbox = tk.Listbox(fenetre, width=40, height=10)
history_listbox.place(x=370, y=203)


# Affichage de victoire ou de défaite.
img_victoire = tk.Label(fenetre, image=chargement_png)
img_victoire.place(x=410, y=75)
victoire = tk.Label(fenetre, text="Jeu en cours...", font=("arial", 18))
victoire.place(x=380, y=40)



# Stylisation
fenetre.config(background="#b0acc2")
titre.config(background="#9688a8", foreground="#392142")
historique_label.config(background="#9688a8", foreground="#392142")
score_frame.config(background="#9688a8")
comp_score_display.config(background="#9688a8", foreground="#392142")
comp_score_label.config(background="#9688a8", foreground="#392142")
player_score_display.config(background="#9688a8", foreground="#392142")
player_score_label.config(background="#9688a8", foreground="#392142")
user_label.config(background="#9688a8", foreground="#392142")
result_label.config(background="#b0acc2", foreground="#392142")
victoire.config(background="#b0acc2", foreground="#392142")
img_victoire.config(background="#b0acc2")
user_img_label.config(background="#b0acc2")
computer_img_label.config(background="#b0acc2")
history_listbox.config(background="#c1c4d9", foreground="#392142")



fenetre.mainloop()