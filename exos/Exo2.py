from menu import *
import random

def Exo2():

    player_name = input("Entrez votre nom : ")
    nb_allumettes = int(input("Choisir le nombre d'allumettes de départ : "))
    turn = random.choice(["joueur", "computer"])

    while nb_allumettes > 0:
        if turn == "joueur":
            print("| " * nb_allumettes)
            move = int(input("Combien d'allumettes souhaitez-vous retirer (1, 2 ou 3) ? "))
            while move not in [1, 2, 3] or move > nb_allumettes:
                move = int(input("Choix non valide. Combien d'allumettes souhaitez-vous retirer (1, 2 ou 3) ? "))
            nb_allumettes -= move
            turn = "computer"
        else:
            if nb_allumettes == 1:
                remove = 1
            elif nb_allumettes == 2:
                remove = 2
            else:
                remove = random.choice([1, 2, 3])
            print("L’ordinateur enlève : ", remove)
            nb_allumettes -= remove
            turn = "joueur"
    print("{} a perdu :-(".format(player_name) if turn == "joueur" else "l’ordinateur a gagné :-)")