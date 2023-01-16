
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

    