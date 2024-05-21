import copy
import random

from Grille import Grille
from EvaluerGrille import evaluer_grille

#Minmax profondeur maximum
PROFONDEUR_MAX = 4

class MinMax : 
    def __init__(self, char:str, profondeux_max:int = 5) -> None:
        self.char = char
        self.advChar = 'o' if self.char == 'x' else 'x'
        self.profondeur_max = profondeux_max 

    def jouer_coup(self, grille : Grille, char : str, inutile_mais_necessaire) -> int : 
        coup = self.minmax(copy.deepcopy(grille), self.profondeur_max, False)
        #print(coup)
        return coup[0]

    def minmax(self, grille_virtuelle : Grille, profondeur_max:int, minimizer : bool) : 
        liste_score=[]
        #Condition d'arrets  
        #Grille gagnante : 
        if grille_virtuelle.est_gagnant(grille_virtuelle.get_coup_prec()[0], grille_virtuelle.get_coup_prec()[1]) : 
            #print(profondeur_max)
            return (grille_virtuelle.coup_prec[1], (100 * profondeur_max)) if(not minimizer) else (grille_virtuelle.coup_prec[1],(-100*profondeur_max))
            
        #Profondeur maximale atteinte 
        if(profondeur_max == 0) : 
            score = evaluer_grille(grille_virtuelle, minimizer, self.char, self.advChar)
            #print(score)
            return (grille_virtuelle.coup_prec[1], score)
            #return score
        
        #Récursivité
        liste_coup = grille_virtuelle.get_liste_coups_possibles()
        for coup in liste_coup: 
            grille_tampon=copy.deepcopy(grille_virtuelle)
            
            if minimizer:
                grille_tampon.placer_jeton(self.char, coup)
                
            else :
                grille_tampon.placer_jeton(self.advChar, coup)
            
            score = self.minmax(grille_tampon, profondeur_max-1, not(minimizer))[1]
            liste_score.append((coup, score))
            #liste_score[coup] = self.minmax(grille_virtuelle, profondeur_max-1, not(minimizer)) 
            
        if ((minimizer)):
            #m = max(liste_score, key=lambda x:x[1], default=0)
            #print(m)
            return max(liste_score, key=lambda x:x[1], default=0)
        else:
            #print (liste)
            return min(liste_score, key=lambda x:x[1], default=0)


