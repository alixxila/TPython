from menu import *

def Exo5():
    
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

    class Roman(Livre):
        def __init__(self, nom, auteur, maison_edition, code_barre, type_roman, description_type):
            Livre.__init__(self, nom, auteur, maison_edition, code_barre)
            self.type_roman = type_roman
            self.description_type = description_type

        def display_book_info(self):
            Livre.display_book_info(self)
            print("Type de roman :", self.type_roman)
            print("Description du type de roman :", self.description_type)

    # créer un roman
    roman = Roman("Les Misérables", "Victor Hugo", "Hachette", "2345678901", "Drame", "Un roman sur la révolution française")

    # afficher les informations sur le roman
    print("Informations sur le roman :")
    roman.display_book_info()