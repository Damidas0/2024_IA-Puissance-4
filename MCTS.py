import random
import copy
import Node
from math import sqrt, log
from Grille import Grille
from Node import Node


C = 1.1


class MCTS : 
    def __init__(self, c_param:float, etat: Grille, iteration:int) -> None:
        C = c_param
        self.racine = Node(etat, None, True, None)
        self.iteration = iteration
        
    def joue_coup(self, grille : Grille, char : str, inutile_mais_necessaire) -> int :
        for i in range(self.iteration) : 
            self.racine.selection()
            self.racine.extension()
            self.racine.simulation()
            self.racine
        
    
    
        
    
    
