#      ____         ______       _      
#     / __ \ __  __/_  __/_____ (_)_____
#    / /_/ // / / / / /  / ___// // ___/
#   / ____// /_/ / / /  / /   / /(__  ) 
#  /_/     \__, / /_/  /_/   /_//____/  
#         /____/                   

from random import randint
grille = [[0 for i in range(10)] for j in range(20)]
def afficher_grille(grille):
    """pour afficher la grille dans l'invite de commande"""
    for ligne in grille:
        print("| ", end="")
        for char in ligne:
            print(char, end=" ")
        print("|")
afficher_grille(grille)
forme_possibles = [[[1, 1, 1, 1]],
                    [[2, 2], [2, 2]],
                    [[0, 3], [3, 3], [3, 0]],
                    [[4, 0], [4, 4], [0, 4]],
                    [[5, 0], [5, 5], [0, 5]]
                   ]
class Piece:
    """Une pièce, avec sa position en fonction de x et de y et de sa forme (différentes formes possibles)"""
    def __init__(self,x, y, forme:int):
        self.forme = forme_possibles[forme]
        self.x = x
        self.y = y
    def rotation(self):
    """Faire une rotation à la pièce"""

def main():
      """La boucle principale du jeu"""
      afficher_grille(grille)
# pour inserer une pièce en haut
def inserer_piece():
    for lignes in range(len(piece)):
        for char in range(len(piece[lignes])):
            grille[lignes][char+5] = piece[lignes][char]
