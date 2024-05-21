from Grille import Grille

def evaluer_grille(grille:Grille, minimizer:bool, joueur_char, adv_char) -> int :
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