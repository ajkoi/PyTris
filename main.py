from random import randint
print("""    ____       ______     _     
   / __ \__  _/_  __/____(_)____
  / /_/ / / / // / / ___/ / ___/
 / ____/ /_/ // / / /  / (__  ) 
/_/    \__, //_/ /_/  /_/____/  
      /____/                    

""")
grille = [[0 for i in range(10)] for j in range(20)]
def afficher_grille(grille):
    """pour afficher la grille dans l'invite de commande"""
    for ligne in grille:
        print(ligne)


afficher_grille(grille)
forme_possibles = [[[1, 1, 1, 1]],
                    [[2, 2], [2, 2]],
                    [[0, 3], [3, 3], [3, 0]],
                    [[0, 4], [4, 4], [0, 4]],
                    [[5, 0], [5, 5], [0, 5]]
                   ]
class Piece:
    """la classe correspondant à une pièce"""
    def __init__(self,x, y, forme:int):
        self.forme = forme_possibles[forme]
        self.x = x
        self.y = y
a = Piece(1)
