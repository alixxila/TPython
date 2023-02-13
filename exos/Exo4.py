from menu import *

def Exo4():
    
    class Livre:
        def __init__(self, nom, auteur, maison_edition, code_barre):
            self.nom = nom
            self.auteur = auteur
            self.maison_edition = maison_edition
            self.code_barre = code_barre

        def modify_book(self, nom=None, auteur=None, maison_edition=None, code_barre=None):
            if nom:
                self.nom = nom
            if auteur:
                self.auteur = auteur
            if maison_edition:
                self.maison_edition = maison_edition
            if code_barre:
                self.code_barre = code_barre

        def display_book_info(self):
            print("Nom du livre :", self.nom)
            print("Auteur :", self.auteur)
            print("Maison d'édition :", self.maison_edition)
            print("Code barre :", self.code_barre)

    # créer un livre
    book = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "Gallimard", "1234567890")

    # afficher les informations sur le livre
    print("Informations sur le livre avant modification :")
    book.display_book_info()

    # modifier le livre
    book.modify_book(maison_edition="Larousse")

    # afficher les informations sur le livre après modification
    print("\nInformations sur le livre après modification :")
    book.display_book_info()