import random
import copy
from math import sqrt, log

from Grille import Grille


C = 1.1


class Noeud:
    def __init__(self, etat: Grille, parent, joue:bool, mouvement:int):
        self.etat = copy.deepcopy(etat)
        self.mouvement = mouvement
        self.joue = joue 
        self.parent = parent
        self.enfants = []
        #Format [victoire, defaite + égalité]
        self.listeScore=[0,0]
        self.nb_visites = 1
        
    '''
    Parcours l'arbre jusqu'une feuille
    '''
    def selection(self):
        #S'il y a enfants on en choisit un selon la formule 
        if(self.enfants != []):
            poids = []
            for enfant in self.enfants:
                poids.append(int (100*enfant.calcul_valeur_noeud()))
            #Choix aléatoire pondéré
            tmp = random.choices(self.enfants, weights=poids)
            return tmp[0].selection()
        else:
            return self

    def calcul_valeur_noeud(self) : 
        if(self.joue==True):
            nbVictoire=self.listeScore[0]
        if(self.joue==False): 
            nbVictoire=self.listeScore[1] #on souhaite qu'un noeud soit perdant pour l'adversaire   
        valeurMoyenne=nbVictoire/self.nb_visites

    
        ret = valeurMoyenne + C*sqrt(log(self.parent.nb_visites)/self.nb_visites)
        #print (ret, " Valeur qui est en dessous de 0 apparement")
        return ret
        
        
    def extension (self) :
        if not (self.etat.est_gagnant()) :
            coup_possible = self.etat.get_liste_coups_possibles()
            
            for coup in coup_possible:
                grille_tampon = copy.deepcopy(self.etat)
                grille_tampon.placer_jeton('o' if grille_tampon.get_coup_prec()=='x' else 'x', coup)
                noeud_tampon = Noeud(grille_tampon, self, not(self.joue), coup)
                self.enfants.append(noeud_tampon)
                
    

    def devient_racine(self) : 
        del self.parent
        self.parent = None

    def est_racine(self) :
        return self.parent == None
    
        

    def simulation (self):
        tmp = copy.deepcopy(self.etat)
        if (tmp.get_coup_prec()=='x' and self.joue) : joueur = 'o'
        else : joueur = 'x'
        
        while not(tmp.est_gagnant()) : 
            liste_coup = tmp.get_liste_coups_possibles()
            if (len(liste_coup)>0) : 
                coup = liste_coup[random.randint(0, len(liste_coup)-1)]
                
            #jouer coup 
            tmp.placer_jeton(('o' if tmp.get_coup_prec()=='x' else 'x'), coup)
                       
            
        if tmp.est_gagnant() : 
            if self.joue and tmp.get_coup_prec() == joueur : 
                #Victoire 
                return 0 
            else : return 1 
            
                
    def propagation_resultat(self, resultat) : 
        tmp = self
        tmp.nb_visites +=1
        tmp.listeScore[resultat] += 1
        while(tmp.parent != None):
            tmp = tmp.parent
            tmp.listeScore[resultat] += 1
            tmp.nb_visites += 1
            
    def choisit_enfant(self) : 
        liste_scores = [(e.mouvement, (e.calcul_valeur_noeud())) for e in self.enfants]
        [print(ls) for ls in liste_scores]
        return max(liste_scores, key=lambda x:x[1], default=(0, 0))
        



    



