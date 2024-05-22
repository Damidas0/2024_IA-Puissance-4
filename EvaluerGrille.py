from Grille import Grille


def evaluer_grille_mais_vieux(grille:Grille, minimizer:bool, joueur_char, adv_char) -> int :
  NB_LIGNES = grille.hauteur
  NB_COLONNES = grille.largeur


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
              if (grille.grille[ligne_i][colonne_i] == joueur_char):
                  if (colonne_i < NB_COLONNES - 2) :
                      if (ligne_i > 2) :    
                          #Verification de la diagonale bas droite
                          if (grille.grille[ligne_i - 1][colonne_i+ 1] == joueur_char):
                              if (grille.grille[ligne_i-2][colonne_i+ 2] == joueur_char) : 
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
                          if (grille.grille[ligne_i + 1][colonne_i+ 1] == joueur_char):
                              if (grille.grille[ligne_i+2][colonne_i+2] == joueur_char) : 
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
                      if (grille.grille[ligne_i][colonne_i+1] == joueur_char):
                              if (grille.grille[ligne_i][colonne_i+2] == joueur_char) : 
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
                      if (grille.grille[ligne_i+ 1][colonne_i] == joueur_char):
                          if (grille.grille[ligne_i+2][colonne_i] == joueur_char) : 
                              if (grille.grille[ligne_i+3][colonne_i] == '') : 
                                  score = score + scorePourTrois
                          if (grille.grille[ligne_i+2][colonne_i] == joueur_char) :
                              score = score + scorePourDeux


      for colonne_i in range (NB_COLONNES) : 
          for ligne_i in range (NB_LIGNES) : 
              if (grille.grille[ligne_i][colonne_i] == adv_char) :

                  if (colonne_i < NB_COLONNES - 2) :
                      if (ligne_i > 2) :    
                          #Verification de la diagonale bas droite
                          if (grille.grille[ligne_i - 1][colonne_i + 1] == adv_char):
                              if (grille.grille[ligne_i-2][colonne_i+ 2] == adv_char) : 
                                  if ((colonne_i < NB_COLONNES - 3) and (ligne_i < NB_LIGNES - 3)) :
                                      if (grille.grille[ligne_i-3][colonne_i+3] == '') : 
                                          score = score - scorePourTrois
                                  elif ((colonne_i > 0) and (ligne_i < NB_LIGNES - 1)) :
                                      if (grille.grille[ligne_i+1][colonne_i-1] == '') : 
                                          score = score - scorePourTrois
                              elif (grille.grille[ligne_i-2][colonne_i+2] == '') : 
                                  if ((colonne_i > 0) and (ligne_i < NB_LIGNES - 1)) :
                                      if (grille.grille[ligne_i+1][colonne_i-1] == '') : 
                                          score = score - scorePourDeux



                      if (ligne_i < NB_LIGNES - 2) : 
                          #Verification de la diagonale haut droite
                          if (grille.grille[ligne_i + 1][colonne_i+ 1] == adv_char):
                              if (grille.grille[ligne_i+2][colonne_i+2] == adv_char) : 
                                  if ((colonne_i < NB_COLONNES - 3) and (ligne_i < NB_LIGNES - 3)) :
                                      if (grille.grille[ligne_i+3][colonne_i+3] == '') : 
                                          score = score - scorePourTrois
                                  elif ((colonne_i > 0) and (ligne_i > 0)) :
                                      if (grille.grille[ligne_i-1][colonne_i-1] == '') : 
                                          score = score - scorePourTrois
                              elif (grille.grille[ligne_i+2][colonne_i+2] == '') : 
                                  if ((colonne_i > 0) and (ligne_i > 0)) :
                                      if (grille.grille[ligne_i-1][colonne_i-1] == '') : 
                                          score = score - scorePourDeux
                      
                      #verification ligne
                      if (grille.grille[ligne_i][colonne_i+1] == adv_char):
                              if (grille.grille[ligne_i][colonne_i+2] == adv_char) : 
                                  if (colonne_i < NB_COLONNES - 3) :
                                      if (grille.grille[ligne_i][colonne_i+3] == '') : 
                                          score = score - scorePourTrois
                                  elif (colonne_i > 0) :
                                      if (grille.grille[ligne_i][colonne_i-1] == '') : 
                                          score = score - scorePourTrois
                              elif (grille.grille[ligne_i][colonne_i+2] == '') : 
                                  if (colonne_i > 0) :
                                      if (grille.grille[ligne_i][colonne_i-1] == '') : 
                                          if (colonne_i > 1) : 
                                              if (grille.grille[ligne_i][colonne_i-2] == '') :
                                                  score = score - scorePourDeuxPiege
                                          if (colonne_i < NB_COLONNES - 3) : 
                                              if (grille.grille[ligne_i][colonne_i+2] == '') :
                                                  score = score - scorePourDeuxPiege
                                          score = score - scorePourDeux
                  if (ligne_i < NB_LIGNES - 3) :
                      #verification colonne
                      if (grille.grille[ligne_i+1][colonne_i] == adv_char):
                          if (grille.grille[ligne_i+2][colonne_i] == adv_char) : 
                              if (grille.grille[ligne_i+3][colonne_i] == '') : 
                                  score = score - scorePourTrois
                          if (grille.grille[ligne_i+2][colonne_i] == adv_char) :
                              score = score - scorePourDeux
      return score




def evaluer_grille(grille:Grille, minimizer:bool, joueur_char, adv_char) -> int :
  a = evaluer_grille_par_joueur(grille, minimizer, joueur_char, adv_char)
  b = evaluer_grille_par_joueur(grille, minimizer, adv_char, joueur_char)
  
  # print("-------------------")
  # print("nv:",a-b)
  # print("vieux:",evaluer_grille_mais_vieux(grille, minimizer, joueur_char, adv_char))
  
  return a-b
  

def evaluer_grille_par_joueur(grille:Grille, minimizer:bool, joueur_char, joueur_advs_char) -> int :
    NB_LIGNES = grille.hauteur
    NB_COLONNES = grille.largeur


    if (minimizer and grille.est_gagnant(grille.get_coup_prec()[0], grille.get_coup_prec()[1])) :
      return 1000
    if (not minimizer and grille.est_gagnant(grille.get_coup_prec()[0], grille.get_coup_prec()[1])) :
      return -1000
    
    
    # les scores sont a modifier pour que ce soit pertinent 
    scorePourTrois = 5
    scorePourDeux = 2
    scorePourUn = 0.1


    nb_jeton_par_groupe = [0,0,0] # 0: 1 jeton, 1: 2 jetons, 2: 3 jetons
    
    
    #Vérification verticale |
    for ligne_i in range (NB_LIGNES - 3) :
      for colonne_j in range (NB_COLONNES) :
          nb_jeton = 0
          
          for i in range(4):
            if grille.grille[ligne_i + i][colonne_j] == joueur_advs_char:
              nb_jeton = 0
              break
            
            if grille.grille[ligne_i + i][colonne_j] == joueur_char:
              nb_jeton += 1

          if 0 < nb_jeton and nb_jeton < 4:
            nb_jeton_par_groupe[nb_jeton - 1] += 1
          
    
    
    #Vérification horizontale -
    for ligne_i in range (NB_LIGNES) :
      for colonne_j in range (NB_COLONNES - 3) :
          nb_jeton = 0
          
          for i in range(4):
            if grille.grille[ligne_i][colonne_j + i] == joueur_advs_char:
              nb_jeton = 0
              break
        
            if grille.grille[ligne_i][colonne_j + i] == joueur_char:
              nb_jeton += 1
            
          if 0 < nb_jeton and nb_jeton < 4:
            nb_jeton_par_groupe[nb_jeton - 1] += 1
    
    #Vérification diagonale \
    for ligne_i in range (NB_LIGNES - 3) :
      for colonne_j in range (NB_COLONNES - 3) :
          nb_jeton = 0
          
          for i in range(4):
            if grille.grille[ligne_i + i][colonne_j + i] == joueur_advs_char:
              nb_jeton = 0
              break
        
            if grille.grille[ligne_i + i][colonne_j + i] == joueur_char:
              nb_jeton += 1
              
          if 0 < nb_jeton and nb_jeton < 4:
            nb_jeton_par_groupe[nb_jeton - 1] += 1

          
    #Vérification diagonale /
    for ligne_i in range (3, NB_LIGNES) :
      for colonne_j in range (NB_COLONNES - 3) :
          nb_jeton = 0
          
          for i in range(4):
            if grille.grille[ligne_i - i][colonne_j + i] == joueur_advs_char:
              nb_jeton = 0
              break
        
            if grille.grille[ligne_i - i][colonne_j + i] == joueur_char:
              nb_jeton += 1
              
          if 0 < nb_jeton and nb_jeton < 4:
            nb_jeton_par_groupe[nb_jeton - 1] += 1

    
    # print("--------------")
    # print(nb_jeton_par_groupe)
    # print(grille)
          
    return nb_jeton_par_groupe[2] * scorePourTrois + nb_jeton_par_groupe[1] * scorePourDeux + nb_jeton_par_groupe[0] * scorePourUn
  
  
  
# g = Grille(6,7)
# g.placer_jeton('x', 0)
# g.placer_jeton('x', 0)
# evaluer_grille(g, True, 'x', 'o')