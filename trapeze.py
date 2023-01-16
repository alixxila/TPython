def mon_calc():

    #Entrée au clavier convertie en INT pour le calcul
    A = int(input("Rentrer A (en M) : "))
    B = int(input("Rentrer B (en M) : "))
    C = int(input("Rentrer C (en M) : ")) 

    #Formule Calcul trapeze
    return (A + B) * C * 0.5

print("Le resultat est : ", mon_calc())

