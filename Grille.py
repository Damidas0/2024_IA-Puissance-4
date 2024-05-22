import copy

#grille[ligne][colone]

class Grille :
  def __init__(self, hauteur = 6, largeur = 7, grille = [], coup_prec=[0,0]):
    self.hauteur = hauteur
    self.largeur = largeur
    self.coup_prec = coup_prec
    if (grille!=[]):
        self.grille = copy.deepcopy(grille)
    else :
        self.grille = [['' for i in range(self.largeur)] for j in range(self.hauteur)]

      
  def __deepcopy__(self, memo) :
      return Grille(self.hauteur, self.largeur, self.grille, self.coup_prec) 
      

  def vider_grille(self):
    self.grille = [['' for i in range(self.largeur)] for j in range(self.hauteur)]
    self.coup_prec = [0,0]
    
  def __str__(self):
    s = ''
    for ligne_i in range(self.hauteur):
      for colone_j in range(self.largeur):
        s += self.grille[ligne_i][colone_j] if self.grille[ligne_i][colone_j]!='' else ' ' 
        s += '|'
      s += '\n'
    return s
  
  def case_est_vide(self, ligne, colonne):
    return self.grille[ligne][colonne] == ''
  
  def get_case(self, ligne, colonne):
    return self.grille[ligne][colonne]

  def placer_jeton(self, joueur, colonne):
    if colonne < 0 or colonne > self.largeur-1:
      raise ValueError('colonne invalide')
      return False
    
    for ligne_i in range(self.hauteur-1, -1, -1):
      if self.case_est_vide(ligne_i, colonne):
        self.grille[ligne_i][colonne] = joueur
        self.coup_prec = [ligne_i, colonne]
        
        if self.est_gagnant(ligne_i, colonne):
          return True

        if self.est_plein():
          return True
        
        return False
    raise ValueError('colonne pleine')
    return False

  def est_plein(self):
    for ligne_i in range(self.hauteur):
      for colonne_j in range(self.largeur):
        if self.case_est_vide(ligne_i, colonne_j):
          return False
    return True
  
  def get_coup_prec(self):
    return self.coup_prec
  
  def est_gagnant(self, ligne = None, colonne = None):
    if ligne == None : 
      ligne = self.coup_prec[0] 
      colonne = self.coup_prec[1]
      
    if colonne < 0 or colonne > self.largeur-1 or ligne < 0 or ligne > self.hauteur-1:
      raise ValueError('colonne ou ligne invalide')
      return False
  
    if self.case_est_vide(ligne, colonne):
      return False
    
    joueur = self.grille[ligne][colonne]

    # Vérification verticale 
    consecutive = 0
    for ligne_i in range(ligne, -1, -1):
        if self.grille[ligne_i][colonne] == joueur:
            consecutive += 1
        else:
            break
    for ligne_i in range(ligne + 1, self.hauteur):
        if self.grille[ligne_i][colonne] == joueur:
            consecutive += 1
        else:
            break
    if consecutive >= 4:
        return True
    
    # Vérification horizontale -
    consecutive = 0
    for colonne_j in range(self.largeur):
        if self.grille[ligne][colonne_j] == joueur:
            consecutive += 1
        else:
            consecutive = 0
        if consecutive >= 4:
            return True

    # Vérification diagonale \
    consecutive = 0
    ligne_i, colonne_j = ligne, colonne
    while ligne_i < self.hauteur and colonne_j < self.largeur:
        if self.grille[ligne_i][colonne_j] == joueur:
            consecutive += 1
        else:
            break
        ligne_i += 1
        colonne_j += 1
    ligne_i, colonne_j = ligne - 1, colonne - 1
    while ligne_i >= 0 and colonne_j >= 0:
        if self.grille[ligne_i][colonne_j] == joueur:
            consecutive += 1
        else:
            break
        ligne_i -= 1
        colonne_j -= 1
    if consecutive >= 4:
        return True

    # Vérification diagonale /
    consecutive = 0
    ligne_i, colonne_j = ligne, colonne
    while ligne_i < self.hauteur and colonne_j >= 0:
        if self.grille[ligne_i][colonne_j] == joueur:
            consecutive += 1
        else:
            break
        ligne_i += 1
        colonne_j -= 1
    ligne_i, colonne_j = ligne - 1, colonne + 1
    while ligne_i >= 0 and colonne_j < self.largeur:
        if self.grille[ligne_i][colonne_j] == joueur:
            consecutive += 1
        else:
            break
        ligne_i -= 1
        colonne_j += 1
    if consecutive >= 4:
        return True

    return False

  def get_positions_gagnantes_avec_ligne(self, ligne, colonne):
    if colonne < 0 or colonne > self.largeur - 1 or ligne < 0 or ligne > self.hauteur - 1:
        raise ValueError('colonne ou ligne invalide')

    joueur = self.grille[ligne][colonne]
    positions_gagnantes = [[ligne, colonne]]  # Liste pour stocker les positions gagnantes

    # Vérification verticale
    consecutive = 1
    for ligne_i in range(ligne - 1, -1, -1):
        if self.grille[ligne_i][colonne] == joueur:
            consecutive += 1
            positions_gagnantes.append([ligne_i, colonne])
        else:
            break
    for ligne_i in range(ligne + 1, self.hauteur):
        if self.grille[ligne_i][colonne] == joueur:
            consecutive += 1
            positions_gagnantes.append([ligne_i, colonne])
        else:
            break
    if consecutive >= 4:
        return positions_gagnantes

    # Vérification horizontale
    consecutive = 1
    for colonne_j in range(colonne - 1, -1, -1):
        if self.grille[ligne][colonne_j] == joueur:
            consecutive += 1
            positions_gagnantes.append([ligne, colonne_j])
        else:
            break
    for colonne_j in range(colonne + 1, self.largeur):
        if self.grille[ligne][colonne_j] == joueur:
            consecutive += 1
            positions_gagnantes.append([ligne, colonne_j])
        else:
            break
    if consecutive >= 4:
        return positions_gagnantes

    # Vérification diagonale \
    consecutive = 1
    ligne_i, colonne_j = ligne - 1, colonne - 1
    while ligne_i >= 0 and colonne_j >= 0:
        if self.grille[ligne_i][colonne_j] == joueur:
            consecutive += 1
            positions_gagnantes.append([ligne_i, colonne_j])
        else:
            break
        ligne_i -= 1
        colonne_j -= 1
    ligne_i, colonne_j = ligne + 1, colonne + 1
    while ligne_i < self.hauteur and colonne_j < self.largeur:
        if self.grille[ligne_i][colonne_j] == joueur:
            consecutive += 1
            positions_gagnantes.append([ ligne_i, colonne_j])
        else:
            break
        ligne_i += 1
        colonne_j += 1
    if consecutive >= 4:
        return positions_gagnantes

    # Vérification diagonale /
    consecutive = 1
    ligne_i, colonne_j = ligne - 1, colonne + 1
    while ligne_i >= 0 and colonne_j < self.largeur:
        if self.grille[ligne_i][colonne_j] == joueur:
            consecutive += 1
            positions_gagnantes.append([ligne_i, colonne_j])
        else:
            break
        ligne_i -= 1
        colonne_j += 1
    ligne_i, colonne_j = ligne + 1, colonne - 1
    while ligne_i < self.hauteur and colonne_j >= 0:
        if self.grille[ligne_i][colonne_j] == joueur:
            consecutive += 1
            positions_gagnantes.append([ligne_i, colonne_j])
        else:
            break
        ligne_i += 1
        colonne_j -= 1
    if consecutive >= 4:
        return positions_gagnantes

    # Si aucune séquence gagnante n'est trouvée, retourne une liste vide
    return []

  def get_positions_gagnantes(self, colonne):
    ligne = 0
    
    while ligne < self.hauteur-1 and self.case_est_vide(ligne, colonne):
      ligne += 1
    return self.get_positions_gagnantes_avec_ligne(ligne, colonne)
    
  def get_liste_coups_possibles(self):
    coups = []
    for j in range(self.largeur):
      if self.case_est_vide(0, j):
        coups.append(j)
    return coups


