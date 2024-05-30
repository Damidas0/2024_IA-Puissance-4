import random
import copy
from math import sqrt, log
from Grille import Grille

from Noeud import Noeud, C



class MCTS : 
    def __init__(self, c_param:float, char:str, iteration:int = 100000) -> None:
        C = c_param
        self.racine = Noeud(Grille(), None, True, 0)
        self.char = char
        self.advChar = 'o' if self.char == 'x' else 'x'

        self.iteration = iteration
        
    def jouer_coup(self, grille : Grille, char : str, inutile_mais_necessaire) -> int :
        #if (self.racine.enfants !=[]) : 
        #    for enfant in self.racine.enfants : 
        #        for e in enfant.enfants : 
        #            if e.etat.coup_prec == grille.coup_prec : 
        #                del self.racine
        #                self.racine = e
        #else : 
        self.racine = Noeud(grille, None, True, 0)
        for _ in range(self.iteration) : 
            tmp = self.racine.selection()
            tmp.extension()
            tmp.propagation_resultat(tmp.simulation())
        coup = self.racine.choisit_enfant()
        return coup[0]
        
    
    
        
    
    
