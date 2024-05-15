import copy
import random

from Grille import Grille

#Minmax profondeur maximum
PROFONDEUR_MAX = 4

NB_COLONNES = 7
NB_LIGNES = 6 

class MinMax : 
    def __init__(self, char:str, profondeux_max:int = 5) -> None:
        self.char = char
        self.advChar = 'o' if self.char == 'x' else 'x'
        self.profondeur_max = profondeux_max 

    def jouer_coup(self, grille : Grille, char : str, inutile_mais_necessaire) -> int : 
        coup = self.minmax(copy.deepcopy(grille), self.profondeur_max, True)
        return coup

    def minmax(self, grille_virtuelle : Grille, profondeur_max:int, minimizer : bool) : 
        liste_score=[]
        #Condition d'arrets  
        #Grille gagnante : 
        if grille_virtuelle.est_gagnant(grille_virtuelle.get_coup_prec()[0], grille_virtuelle.get_coup_prec()[1]) : 
            return 100 * profondeur_max if(minimizer) else -100*profondeur_max
            
        #Profondeur maximale atteinte 
        if(profondeur_max == 0) : 
            return self.evaluer_grille(grille_virtuelle, minimizer)
        
        #Récursivité
        liste_coup = grille_virtuelle.get_liste_coups_possibles()
        liste_score = []
        for coup in liste_coup: 
            grille_tampon=copy.deepcopy(grille_virtuelle)
            
            if minimizer:
                grille_tampon.placer_jeton(self.char, coup)
                
            else :
                grille_tampon.placer_jeton(self.advChar, coup)
            liste_score.append(self.minmax(grille_virtuelle, profondeur_max-1, not(minimizer))) 
            
        if ((minimizer)):
            #print (liste)
            return max(liste_score, default=0)
        else:
            #print (liste)
            return min(liste_score, default=0)
        
        
        
    def evaluer_grille(self, grille:Grille, minimizer:bool) -> int : 
        if (minimizer and grille.est_gagnant(grille.get_coup_prec()[0], grille.get_coup_prec()[1])) :
            return 100 
        if (not minimizer and grille.est_gagnant(grille.get_coup_prec()[0], grille.get_coup_prec()[1])) :
            return -100
        else:
            # les scores sont a modifier pour que ce soit pertinent 
            scorePourTrois = 5
            scorePourDeux = 2
            scorePourDeuxPiege = 3

            #compter le nombre de coup pour trois 
            score = 0; 

            for colonne_i in range (NB_COLONNES) : 
                for ligne_i in range (NB_LIGNES) : 
                    if (grille.grille[ligne_i][colonne_i] == self.char):
                        if (colonne_i < NB_COLONNES - 2) :
                            if (ligne_i > 2) :    
                                #Verification de la diagonale bas droite
                                if (grille.grille[ligne_i - 1][colonne_i+ 1] == self.char):
                                    if (grille.grille[ligne_i-2][colonne_i+ 2] == self.char) : 
                                        if ((colonne_i < NB_COLONNES - 3) and (ligne_i < NB_LIGNES - 3)) :
                                            if (grille.grille[ligne_i-3][colonne_i+3] == '') : 
                                                score = score + scorePourTrois
                                        elif ((colonne_i > 0) and (ligne_i < NB_LIGNES - 1)) :
                                            if (grille.grille[ligne_i+1][colonne_i-1] == '') : 
                                                score = score + scorePourTrois
                                    elif (grille.grille[ligne_i-2][colonne_i+2] == '') : 
                                        if ((colonne_i > 0) and (ligne_i < NB_LIGNES - 1)) :
                                            if (grille.grille[ligne_i+1][colonne_i-1] == '') : 
                                                score = score + scorePourDeux



                            if (ligne_i < NB_LIGNES - 2) : 
                                #Verification de la diagonale haut droite
                                if (grille.grille[ligne_i + 1][colonne_i+ 1] == self.char):
                                    if (grille.grille[ligne_i+2][colonne_i+2] == self.char) : 
                                        if ((colonne_i < NB_COLONNES - 3) and (ligne_i < NB_LIGNES - 3)) :
                                            if (grille.grille[ligne_i+3][colonne_i+3] == '') : 
                                                score = score + scorePourTrois
                                        elif ((colonne_i > 0) and (ligne_i > 0)) :
                                            if (grille.grille[ligne_i-1][colonne_i-1] == '') : 
                                                score = score + scorePourTrois
                                    elif (grille.grille[ligne_i+2][colonne_i+2] == '') : 
                                        if ((colonne_i > 0) and (ligne_i > 0)) :
                                            if (grille.grille[ligne_i-1][colonne_i-1] == '') : 
                                                score = score + scorePourDeux
                            
                            #verification ligne
                            if (grille.grille[ligne_i][colonne_i+1] == self.char):
                                    if (grille.grille[ligne_i][colonne_i+2] == self.char) : 
                                        if (colonne_i < NB_COLONNES - 3) :
                                            if (grille.grille[ligne_i][colonne_i+3] == '') : 
                                                score = score + scorePourTrois
                                        elif (colonne_i > 0) :
                                            if (grille.grille[ligne_i][colonne_i-1] == '') : 
                                                score = score + scorePourTrois
                                    elif (grille.grille[ligne_i][colonne_i+2] == '') : 
                                        if (colonne_i > 0) :
                                            if (grille.grille[ligne_i][colonne_i-1] == '') : 
                                                if (colonne_i > 1) : 
                                                    if (grille.grille[ligne_i][colonne_i-2] == '') :
                                                        score = score + scorePourDeuxPiege
                                                if (colonne_i < NB_COLONNES - 3) : 
                                                    if (grille.grille[ligne_i][colonne_i+2] == '') :
                                                        score = score + scorePourDeuxPiege
                                                score = score + scorePourDeux
                        if (ligne_i < NB_LIGNES - 3) :
                            #verification colonne
                            if (grille.grille[ligne_i+ 1][colonne_i] == self.char):
                                if (grille.grille[ligne_i+2][colonne_i] == self.char) : 
                                    if (grille.grille[ligne_i+3][colonne_i] == '') : 
                                        score = score + scorePourTrois
                                if (grille.grille[ligne_i+2][colonne_i] == self.char) :
                                    score = score + scorePourDeux


            for colonne_i in range (NB_COLONNES) : 
                for ligne_i in range (NB_LIGNES) : 
                    if (grille.grille[ligne_i][colonne_i] == self.advChar) :

                        if (colonne_i < NB_COLONNES - 2) :
                            if (ligne_i > 2) :    
                                #Verification de la diagonale bas droite
                                if (grille[ligne_i - 1][colonne_i + 1] == self.advChar):
                                    if (grille[ligne_i-2][colonne_i+ 2] == self.advChar) : 
                                        if ((colonne_i < NB_COLONNES - 3) and (ligne_i < NB_LIGNES - 3)) :
                                            if (grille[ligne_i-3][colonne_i+3] == '') : 
                                                score = score - scorePourTrois
                                        elif ((colonne_i > 0) and (ligne_i < NB_LIGNES - 1)) :
                                            if (grille[ligne_i+1][colonne_i-1] == '') : 
                                                score = score - scorePourTrois
                                    elif (grille[ligne_i-2][colonne_i+2] == '') : 
                                        if ((colonne_i > 0) and (ligne_i < NB_LIGNES - 1)) :
                                            if (grille[ligne_i+1][colonne_i-1] == '') : 
                                                score = score - scorePourDeux



                            if (ligne_i < NB_LIGNES - 2) : 
                                #Verification de la diagonale haut droite
                                if (grille[ligne_i + 1][colonne_i+ 1] == self.advChar):
                                    if (grille[ligne_i+2][colonne_i+2] == self.advChar) : 
                                        if ((colonne_i < NB_COLONNES - 3) and (ligne_i < NB_LIGNES - 3)) :
                                            if (grille[ligne_i+3][colonne_i+3] == '') : 
                                                score = score - scorePourTrois
                                        elif ((colonne_i > 0) and (ligne_i > 0)) :
                                            if (grille[ligne_i-1][colonne_i-1] == '') : 
                                                score = score - scorePourTrois
                                    elif (grille[ligne_i+2][colonne_i+2] == '') : 
                                        if ((colonne_i > 0) and (ligne_i > 0)) :
                                            if (grille[ligne_i-1][colonne_i-1] == '') : 
                                                score = score - scorePourDeux
                            
                            #verification ligne
                            if (grille[ligne_i][colonne_i+1] == self.advChar):
                                    if (grille[ligne_i][colonne_i+2] == self.advChar) : 
                                        if (colonne_i < NB_COLONNES - 3) :
                                            if (grille[ligne_i][colonne_i+3] == '') : 
                                                score = score - scorePourTrois
                                        elif (colonne_i > 0) :
                                            if (grille[ligne_i][colonne_i-1] == '') : 
                                                score = score - scorePourTrois
                                    elif (grille[ligne_i][colonne_i+2] == '') : 
                                        if (colonne_i > 0) :
                                            if (grille[ligne_i][colonne_i-1] == '') : 
                                                if (colonne_i > 1) : 
                                                    if (grille[ligne_i][colonne_i-2] == '') :
                                                        score = score - scorePourDeuxPiege
                                                if (colonne_i < NB_COLONNES - 3) : 
                                                    if (grille[ligne_i][colonne_i+2] == '') :
                                                        score = score - scorePourDeuxPiege
                                                score = score - scorePourDeux
                        if (ligne_i < NB_LIGNES - 3) :
                            #verification colonne
                            if (grille[ligne_i+1][colonne_i] == self.advChar):
                                if (grille[ligne_i+2][colonne_i] == self.advChar) : 
                                    if (grille[ligne_i+3][colonne_i] == '') : 
                                        score = score - scorePourTrois
                                if (grille[ligne_i+2][colonne_i] == self.advChar) :
                                    score = score - scorePourDeux
            return score
    #lister coup possible    
    

