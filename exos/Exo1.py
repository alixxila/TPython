from menu import *

def Exo1():

    A = int(input("Entrer A : "))
    B = int(input("Entrer B : "))
    P = float(input('Entrer P : '))
    result = 0 

    S = 0
    while(A < B):
        S += A * A * P
        A += P
        result = S

    print("Calcule de l'integrale de la fonction y = x * x avec" ,A, "<= x <" ,B, "et" ,P, " = " ,P) 
    print("Resultat : ", result)

    return A, B, P, result

