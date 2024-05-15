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

    def jouer_coup(self, grille : Grille, char : str) -> int : 
        coup = self.minmax(copy.deepcopy(grille), self.profondeur_max, True)
        return coup

    def minmax(self, grille_virtuelle : Grille, profondeur_max:int, minimizer : bool) : 
        liste_score=[]
        #Condition d'arrets  
        #Grille gagnante : 
        if grille_virtuelle.est_gagnant() : 
            return 100 * profondeur_max if(minimizer) else -100*profondeur_max
            
        #Profondeur maximale atteinte 
        if(profondeur_max == 0) : 
            return self.evaluer_grille(grille_virtuelle)
        
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
        if (minimizer and grille.est_gagnant()) :
            return 100 
        if (not minimizer and grille.est_gagnant()) :
            return -100
        else:
            # les scores sont a modifier pour que ce soit pertinent 
            scorePourTrois = 5
            scorePourDeux = 2
            scorePourDeuxPiege = 3

            #compter le nombre de coup pour trois 
            score = 0; 

            for c in range (NB_COLONNES) : 
                for l in range (NB_LIGNES) : 
                    if (grille.grille[c][l] == self.char):

                        if (c < NB_COLONNES - 2) :
                            if (l > 2) :    
                                #Verification de la diagonale bas droite
                                if (grille.grille[c + 1][l - 1] == self.char):
                                    if (grille.grille[c+2][l - 2] == self.char) : 
                                        if ((c < NB_COLONNES - 3) and (l < NB_LIGNES - 3)) :
                                            if (grille.grille[c+3][l-3] == " ") : 
                                                score = score + scorePourTrois
                                        elif ((c > 0) and (l < NB_LIGNES - 1)) :
                                            if (grille.grille[c-1][l+1] == " ") : 
                                                score = score + scorePourTrois
                                    elif (grille.grille[c+2][l-2] == " ") : 
                                        if ((c > 0) and (l < NB_LIGNES - 1)) :
                                            if (grille.grille[c-1][l+1] == " ") : 
                                                score = score + scorePourDeux



                            if (l < NB_LIGNES - 2) : 
                                #Verification de la diagonale haut droite
                                if (grille.grille[c + 1][l + 1] == self.char):
                                    if (grille.grille[c+2][l+2] == self.char) : 
                                        if ((c < NB_COLONNES - 3) and (l < NB_LIGNES - 3)) :
                                            if (grille.grille[c+3][l+3] == " ") : 
                                                score = score + scorePourTrois
                                        elif ((c > 0) and (l > 0)) :
                                            if (grille.grille[c-1][l-1] == " ") : 
                                                score = score + scorePourTrois
                                    elif (grille.grille[c+2][l+2] == " ") : 
                                        if ((c > 0) and (l > 0)) :
                                            if (grille.grille[c-1][l-1] == " ") : 
                                                score = score + scorePourDeux
                            
                            #verification ligne
                            if (grille.grille[c + 1][l] == self.char):
                                    if (grille.grille[c+2][l] == self.char) : 
                                        if (c < NB_COLONNES - 3) :
                                            if (grille.grille[c+3][l] == " ") : 
                                                score = score + scorePourTrois
                                        elif (c > 0) :
                                            if (grille.grille[c-1][l] == " ") : 
                                                score = score + scorePourTrois
                                    elif (grille.grille[c+2][l] == " ") : 
                                        if (c > 0) :
                                            if (grille.grille[c-1][l] == " ") : 
                                                if (c > 1) : 
                                                    if (grille.grille[c-2][l] == " ") :
                                                        score = score + scorePourDeuxPiege
                                                if (c < NB_COLONNES - 3) : 
                                                    if (grille.grille[c+2][l] == " ") :
                                                        score = score + scorePourDeuxPiege
                                                score = score + scorePourDeux
                        if (l < NB_LIGNES - 3) :
                            #verification colonne
                            if (grille.grille[c][l + 1] == self.char):
                                if (grille.grille[c][l+2] == self.char) : 
                                    if (grille.grille[c][l+3] == " ") : 
                                        score = score + scorePourTrois
                                if (grille.grille[c][l+2] == self.char) :
                                    score = score + scorePourDeux


            for c in range (NB_COLONNES) : 
                for l in range (NB_LIGNES) : 
                    if (grille.grille[c][l] == self.advChar) :

                        if (c < NB_COLONNES - 2) :
                            if (l > 2) :    
                                #Verification de la diagonale bas droite
                                if (grille[c + 1][l - 1] == self.advChar):
                                    if (grille[c+2][l - 2] == self.advChar) : 
                                        if ((c < NB_COLONNES - 3) and (l < NB_LIGNES - 3)) :
                                            if (grille[c+3][l-3] == " ") : 
                                                score = score - scorePourTrois
                                        elif ((c > 0) and (l < NB_LIGNES - 1)) :
                                            if (grille[c-1][l+1] == " ") : 
                                                score = score - scorePourTrois
                                    elif (grille[c+2][l-2] == " ") : 
                                        if ((c > 0) and (l < NB_LIGNES - 1)) :
                                            if (grille[c-1][l+1] == " ") : 
                                                score = score - scorePourDeux



                            if (l < NB_LIGNES - 2) : 
                                #Verification de la diagonale haut droite
                                if (grille[c + 1][l + 1] == self.advChar):
                                    if (grille[c+2][l+2] == self.advChar) : 
                                        if ((c < NB_COLONNES - 3) and (l < NB_LIGNES - 3)) :
                                            if (grille[c+3][l+3] == " ") : 
                                                score = score - scorePourTrois
                                        elif ((c > 0) and (l > 0)) :
                                            if (grille[c-1][l-1] == " ") : 
                                                score = score - scorePourTrois
                                    elif (grille[c+2][l+2] == " ") : 
                                        if ((c > 0) and (l > 0)) :
                                            if (grille[c-1][l-1] == " ") : 
                                                score = score - scorePourDeux
                            
                            #verification ligne
                            if (grille[c + 1][l] == self.advChar):
                                    if (grille[c+2][l] == self.advChar) : 
                                        if (c < NB_COLONNES - 3) :
                                            if (grille[c+3][l] == " ") : 
                                                score = score - scorePourTrois
                                        elif (c > 0) :
                                            if (grille[c-1][l] == " ") : 
                                                score = score - scorePourTrois
                                    elif (grille[c+2][l] == " ") : 
                                        if (c > 0) :
                                            if (grille[c-1][l] == " ") : 
                                                if (c > 1) : 
                                                    if (grille[c-2][l] == " ") :
                                                        score = score - scorePourDeuxPiege
                                                if (c < NB_COLONNES - 3) : 
                                                    if (grille[c+2][l] == " ") :
                                                        score = score - scorePourDeuxPiege
                                                score = score - scorePourDeux
                        if (l < NB_LIGNES - 3) :
                            #verification colonne
                            if (grille[c][l + 1] == self.advChar):
                                if (grille[c][l+2] == self.advChar) : 
                                    if (grille[c][l+3] == " ") : 
                                        score = score - scorePourTrois
                                if (grille[c][l+2] == self.advChar) :
                                    score = score - scorePourDeux
            return score
    #lister coup possible    
    

