import random

class JoueurHumain:
  def jouer_coup(self, grille, joueur, colonne_joueur):
    return colonne_joueur
  
class JoueurAleatoire:
  def jouer_coup(self, grille, joueur, colonne_joueur):
    coups_possible = grille.get_liste_coups_possibles()
    return coups_possible[random.randint(0, len(coups_possible)-1)]