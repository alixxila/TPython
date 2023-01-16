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
    print("   ", "*")
    print("  ", "***", end="")

hauteur_arbre()
