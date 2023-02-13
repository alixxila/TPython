from exos import *

def menu():
    
    print("========================================= Menu du TP1 =========================================")
    
    print("""Liste des exos : 
                - 1 -> Calcul de la surface.
                - 2 -> Jeu des allumettes.
                - 3 -> Les fichiers.
                - 4 -> Classe livre.
                - 5 -> Classe Roman.
    """)
    
    clavier = int(input("Faite votre choix entre les différents exos : "))
    match clavier:
        case 1:
            Exo1()
        case 2:
            Exo2()
        case 3:
            Exo3()
        case 4:
            Exo4()
        case 5:
            Exo5()
        case _:
            print("\n /!\ Commande non valide, arrêt du programme /!\ \n")



