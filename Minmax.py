import copy
import random

from Grille import Grille
from EvaluerGrille import *

#Minmax profondeur maximum
PROFONDEUR_MAX = 4

class MinMax : 
    def __init__(self, char:str, profondeux_max:int = 5, fonction_eval = 1) -> None:
        self.char = char
        self.advChar = 'o' if self.char == 'x' else 'x'
        self.profondeur_max = profondeux_max 
        self.fonction_eval = fonction_eval

    def jouer_coup(self, grille : Grille, char : str, inutile_mais_necessaire) -> int : 
        coup = self.minmax(copy.deepcopy(grille), self.profondeur_max, False, self.fonction_eval)
        #print(coup)
        return coup[0]

    def minmax(self, grille_virtuelle : Grille, profondeur_max:int, minimizer : bool, fonction_eval) : 
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
            
            score = self.minmax(grille_tampon, profondeur_max-1, not(minimizer), fonction_eval)[1]
            liste_score.append((coup, score))
            #liste_score[coup] = self.minmax(grille_virtuelle, profondeur_max-1, not(minimizer)) 
            
        if ((minimizer)):
            #m = max(liste_score, key=lambda x:x[1], default=0)
            #print(m)
            return max_avec_aleatoire(liste_score)
        else:
            #print (liste)
            return min_avec_aleatoire(liste_score)


def max_avec_aleatoire(liste_score):
    max_score = float('-inf')
    coups_max = []
    
    for i in range(len(liste_score)):
        if liste_score[i][1] > max_score:
            max_score = liste_score[i][1]
            coups_max = [liste_score[i][0]]
        elif liste_score[i][1] == max_score:
            coups_max.append(liste_score[i][0])
    
    return random.choice(coups_max), max_score

def min_avec_aleatoire(liste_score):
    min_score = float('inf')
    coups_min = []
    
    for i in range(len(liste_score)):
        if liste_score[i][1] < min_score:
            min_score = liste_score[i][1]
            coups_min = [liste_score[i][0]]
        elif liste_score[i][1] == min_score:
            coups_min.append(liste_score[i][0])

    return random.choice(coups_min), min_score