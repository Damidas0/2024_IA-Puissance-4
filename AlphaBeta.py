import copy
import random

from Grille import Grille
from EvaluerGrille import *
from Minmax import max_avec_aleatoire, min_avec_aleatoire

class AlphaBeta : 
    def __init__(self, char:str, profondeux_max:int = 3, fonction_eval = 1) -> None:
        self.char = char
        self.advChar = 'o' if self.char == 'x' else 'x'
        self.profondeur_max = profondeux_max 
        self.fonction_eval = fonction_eval


    def jouer_coup(self, grille : Grille, char : str, inutile_mais_necessaire) -> int : 
        coup = self.alpha_beta(copy.deepcopy(grille), self.profondeur_max, float('-inf'), float('inf'), False, self.fonction_eval)
        return coup[0]


    def alpha_beta(self, grille_virtuelle : Grille, profondeur_max:int, alpha, beta, minimizer : bool, fonction_eval) : 
        liste_score=[]
        #Condition d'arrets  
        #Grille gagnante : 
        if grille_virtuelle.est_gagnant(grille_virtuelle.get_coup_prec()[0], grille_virtuelle.get_coup_prec()[1]) : 
            #if profondeur_max>2 : print(str(profondeur_max) +"  -  " + str(grille_virtuelle.coup_prec[1]))
            return (grille_virtuelle.coup_prec[1], (100 * profondeur_max)) if(not minimizer) else (grille_virtuelle.coup_prec[1],(-100*profondeur_max))
            
        #Profondeur maximale atteinte 
        if(profondeur_max == 0) : 
            if (fonction_eval == 1) : 
                score = evaluer_grille_mais_vieux(grille_virtuelle, minimizer, self.char, self.advChar)
            else :
                score = evaluer_grille(grille_virtuelle, minimizer, self.char, self.advChar)
            return (grille_virtuelle.coup_prec[1], score)
        
        #Récursivité
        liste_coup = grille_virtuelle.get_liste_coups_possibles()
        alpha_p = float('-inf')
        beta_p = float('inf')
        
        if (minimizer):
            valeur_max = (0, float('-inf'))
            for coup in liste_coup: 
                grille_tampon=copy.deepcopy(grille_virtuelle)
                grille_tampon.placer_jeton(self.char, coup)
                
                score = self.alpha_beta(grille_tampon, profondeur_max-1, max(alpha, alpha_p), beta, not(minimizer), fonction_eval)[1]
                liste_score.append((coup, score))
                
                valeur_max = max_avec_aleatoire(liste_score)
                alpha_p = max(alpha_p, valeur_max[1])
                if alpha_p >= beta:
                    break 
        
            return valeur_max
        
        else:
            valeur_min = (0, float('inf'))
            for coup in liste_coup: 
                grille_tampon=copy.deepcopy(grille_virtuelle)
                grille_tampon.placer_jeton(self.advChar, coup)
                
                score = self.alpha_beta(grille_tampon, profondeur_max-1, alpha, min(beta, beta_p), not(minimizer), fonction_eval)[1]
                liste_score.append((coup, score))
                
                valeur_min = min_avec_aleatoire(liste_score)
                beta_p = min(beta_p, valeur_min[1])
                if alpha >= beta_p:
                    break 
        
            return valeur_min