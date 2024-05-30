import random
import copy
from math import sqrt, log

from Grille import Grille


C = 1.1


class Noeud:
    def __init__(self, etat: Grille, parent, joue:bool, mouvement:int):
        self.etat = etat
        self.mouvement = mouvement
        self.joue = joue 
        self.parent = parent
        self.enfants = []
        #Format [victoire, defaite + égalité]
        self.listeScore=[0,0,0]
        self.nb_visites = 1
        
    '''
    Parcours l'arbre jusqu'une feuille
    '''
    def selection(self):
        #S'il y a enfants on en choisit un selon la formule 
        if(self.enfants != []):
            poids = [enfant.calcul_valeur_noeud() for enfant in self.enfants]
            
            # Trouver l'index de l'enfant avec le poids maximal
            index_max = poids.index(max(poids))
            #choix max
            #tmp = random.choices(self.enfants, weights=poids)
            return self.enfants[index_max].selection()
        else:
            return self

    def calcul_valeur_noeud(self) : 
        if(not self.joue):
            nbVictoire=self.listeScore[0]
        else : 
            nbVictoire=self.listeScore[1] #on souhaite qu'un noeud soit perdant pour l'adversaire   
        valeurMoyenne=nbVictoire/self.nb_visites
        #TODO : regarder si que win.

    
        ret = valeurMoyenne + C*sqrt(log(self.parent.nb_visites)/self.nb_visites)
        #print (ret, " Valeur qui est en dessous de 0 apparement")
        return ret
        
        
    def extension (self) :
        if not (self.etat.est_gagnant()) :
            coup_possible = self.etat.get_liste_coups_possibles()
            
            for coup in coup_possible:
                grille_tampon = copy.deepcopy(self.etat)
                grille_tampon.placer_jeton('o' if grille_tampon.get_case()=='x' else 'x', coup)
                noeud_tampon = Noeud(grille_tampon, self, not(self.joue), coup)
                self.enfants.append(noeud_tampon)
                
    

    def devient_racine(self) : 
        del self.parent
        self.parent = None

    def est_racine(self) :
        return self.parent == None
    
        

    def simulation (self):
        tmp = copy.deepcopy(self.etat)
        if (tmp.get_case()=='x' and self.joue) : joueur = 'o'
        else : joueur = 'x'
        
        while not(tmp.est_pleine() or tmp.est_gagnant()) : 
            liste_coup = tmp.get_liste_coups_possibles()
            if (len(liste_coup)>0) : 
                coup = liste_coup[random.randint(0, len(liste_coup)-1)]
                
            #jouer coup 
            tmp.placer_jeton(('o' if tmp.get_case()=='x' else 'x'), coup)
                       
            
        if tmp.est_gagnant() : 
            if (not self.joue) : 
                #print('aaaaaaa')

                #Victoire 
                return 0 
            else : return 1 
        return 2
            
                
    def propagation_resultat(self, resultat) : 
        tmp = self
        tmp.nb_visites +=1
        tmp.listeScore[resultat] += 1
        while(tmp.parent != None):
            tmp = tmp.parent
            tmp.listeScore[resultat] += 1
            tmp.nb_visites += 1
    
    def calcul_score_noeud(self) : 
        #print(self.listeScore[0])
        return self.listeScore[0]/self.nb_visites    
        
    def choisit_enfant(self) : 
        liste_scores = [(e.mouvement, (e.calcul_score_noeud())) for e in self.enfants]
        for e in self.enfants:
            print("Visites  : " + str(e.nb_visites) + " - Vicroite, défait, églité : " + str(e.listeScore))
        print("-------------------------------------")
        return max(liste_scores, key=lambda x:x[1], default=(0, 0))
    
    def devient_racine(self) : 
        del self.parent
        self.parent = None




    



