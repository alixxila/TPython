import math
from decimal import Decimal 

def menu():

    print("========================================= Menu du TP1 =========================================")
    
    clavier = int(input("Faite votre choix entre les différents TP : "))

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
        case 6:
            Exo6()
        case 7:
            Exo7() 

##################################################################################################################

def Exo1():

    while 1 :

        FirstInput = input('Rentrer un caractere : ')
        SecondInput = input('Rentrer un entier : ')

        #Conversation en int pour le passer dans la fonction chr()
        SecondInputChange = int(SecondInput)

        #Conversation de notre entier en char
        value = ord(FirstInput)

        #Affichage
        print('--------------------------------------------------------')
        print(FirstInput, 'vaut ', value)
        print(SecondInput, ' vaut ', chr(SecondInputChange))
        print('--------------------------------------------------------')

        #Demande de continuer ou non
        RestartProg = input('/!\ Souhaitez-vous recommencer ? /!\  (y) ou (n) : ')

        if RestartProg == 'n':
            print('Merci a bientot !')
            break
        else:
            continue

##################################################################################################################

def mon_calc():

    #Entrée au clavier convertie en INT pour le calcul
    A = int(input("Rentrer A (en M) : "))
    B = int(input("Rentrer B (en M) : "))
    C = int(input("Rentrer C (en M) : ")) 

    #Formule Calcul trapeze
    return (A + B) * C * 0.5


def Exo2():

    print("Le resultat est : ", mon_calc())

##################################################################################################################

def somme_et_facto():
    
    A = int(input("Entrer un entier positif : "))

def Exo3():

    somme_et_facto()

##################################################################################################################

def hauteur_arbre():

    A = int(input("Hauteur de l'arbre : "))
    
    for i in range(1, A + 1):
        # Imprimer les espaces avant les astérisques sur chaque ligne
        for j in range(A - i):
          print(" ", end="")
        # Imprimer les astérisques sur chaque ligne
        for j in range(2 * i - 1):
          print("*", end="")
        # Passer à la ligne suivante
        print()

def Exo4():

    hauteur_arbre()

##################################################################################################################

def fonctions_math():
    
    A = int(input("Entrez un entier : "))

    if A <= 0:
        print("Ce n'est pas une entree valable")
        exit(0)
    else:
        print("Le logarithme neperien de l'entier ", A, " est : ", math.log(A))
        print("Le sinus de l'entier ", A, " est : ", math.sin(A))
        print("Le cosinus de l'entier ", A, " est : ", math.cos(A))

def Exo5():

    fonctions_math()

##################################################################################################################

def F1(x,n):
    resultatF1 = x**n / Decimal(facto(n))
    return(resultatF1)

def facto(valeur):
    ch = 1
    valeurt= []
    for i in range(1, valeur+1) : 
        ch = ch*i
    return(ch)

def Exo6():

    valeur = int(input("Veuillez rentrer une valeur pour n : "))
    
    resultat1 = facto(valeur-1)
    resultat2 = facto(valeur)
    resultat = resultat1*resultat2
    
    print("factoriel(",valeur,") est : ",resultat)
    
    x  = int(input("Saisir la valeur de x : "))
    n  = int(input("Saisir une valeur pour n : "))
    print(F1(x,n))
    
    
    print("Fonction Res(X,i)")
    x = Decimal(input("Saisir une valeur pour X : "))
    n = int(input("Saisir une valeur pour n : "))

    somme += F1(x)
    print(somme)

##################################################################################################################

def Exo7():

    valeur = (int(input("Entrez une valeur pour n : ")))
    U0 = 1
    Un = U0

    for i in range(1, valeur+1) :

        Vn = Un + 1/(valeur * facto(i))
        Un = Un + (1 / facto(i))

        print("Valeur de la suite Un avec n = ",valeur,"= ",Un)
        print("Valeur de la suite Vn avec n = ",valeur,"= ",Vn)

menu()
