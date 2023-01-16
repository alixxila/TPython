import math

def fonctions_math():
    
    A = int(input("Entrez un entier : "))

    if A <= 0:
        print("Ce n'est pas une entree valable")
        exit(0)
    else:
        print("Le logarithme neperien de l'entier ", A, " est : ", math.log(A))
        print("Le sinus de l'entier ", A, " est : ", math.sin(A))
        print("Le cosinus de l'entier ", A, " est : ", math.cos(A))

fonctions_math()