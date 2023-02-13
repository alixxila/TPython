from menu import *
import struct

def Exo3():

    # saisir les deux entiers
    n1 = int(input("Entrer le premier nombre : "))
    n2 = int(input("Entrer le second nombre : "))

    # créer un fichier binaire contenant les deux entiers
    with open("BDD.bin", "wb") as f:
        data = struct.pack("ii", n1, n2)
        f.write(data)

    # créer un fichier texte contenant les deux entiers
    with open("BDD.txt", "w") as f:
        f.write(str(n1) + "\n")
        f.write(str(n2) + "\n")

    # lire les données du fichier binaire
    with open("BDD.bin", "rb") as f:
        data = f.read()
        n1, n2 = struct.unpack("ii", data)
        print("Les entiers lus à partir de BDD.bin :", n1, n2)

    # lire les données du fichier texte
    with open("BDD.txt", "r") as f:
        n1 = int(f.readline().strip())
        n2 = int(f.readline().strip())
        print("Les entiers lus à partir de BDD.txt :", n1, n2)


