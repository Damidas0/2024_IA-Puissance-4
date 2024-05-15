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
      
    print(self.grille)
    
      
  def __deepcopy__(self, memo) :
      return Grille(self.hauteur, self.largeur, self.grille, self.coup_prec) 
      

  def vider_grille(self):
    self.grille = [['' for i in range(self.largeur)] for j in range(self.hauteur)]
    
  def __str__(self):
    s = ''
    for ligne_i in range(self.hauteur):
      for colone_j in range(self.largeur):
        s += self.grille[ligne_i][colone_j] + ' '
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
        
        if self.est_gagnant(colonne, i):
          print(joueur + ' a gagne')
          print(self.get_positions_gagnantes_avec_ligne(colonne, i))
          return True

        if self.est_plein():
          print('Match nul')
          return True
        
        return False
    raise ValueError('colonne pleine')
    return False

  def est_plein(self):
    for i in range(self.hauteur):
      for j in range(self.largeur):
        if self.case_est_vide(i, j):
          return False
    return True
  
  def get_coup_prec(self):
    return self.coup_prec
  
  def est_gagnant(self, colonne, ligne):
    if colonne < 0 or colonne > self.largeur-1 or ligne < 0 or ligne > self.hauteur-1:
      print(colonne, ligne)
      raise ValueError('colonne ou ligne invalide')
      return False
    
    joueur = self.grille[ligne][colonne]

    # Vérification verticale 
    consecutive = 0
    for i in range(ligne, -1, -1):
        if self.grille[i][colonne] == joueur:
            consecutive += 1
        else:
            break
    for i in range(ligne + 1, self.hauteur):
        if self.grille[i][colonne] == joueur:
            consecutive += 1
        else:
            break
    if consecutive >= 4:
        return True
    
    # Vérification horizontale -
    consecutive = 0
    for j in range(self.largeur):
        if self.grille[ligne][j] == joueur:
            consecutive += 1
        else:
            consecutive = 0
        if consecutive >= 4:
            return True

    # Vérification diagonale \
    consecutive = 0
    i, j = ligne, colonne
    while i < self.hauteur and j < self.largeur:
        if self.grille[i][j] == joueur:
            consecutive += 1
        else:
            break
        i += 1
        j += 1
    i, j = ligne - 1, colonne - 1
    while i >= 0 and j >= 0:
        if self.grille[i][j] == joueur:
            consecutive += 1
        else:
            break
        i -= 1
        j -= 1
    if consecutive >= 4:
        return True

    # Vérification diagonale /
    consecutive = 0
    i, j = ligne, colonne
    while i < self.hauteur and j >= 0:
        if self.grille[i][j] == joueur:
            consecutive += 1
        else:
            break
        i += 1
        j -= 1
    i, j = ligne - 1, colonne + 1
    while i >= 0 and j < self.largeur:
        if self.grille[i][j] == joueur:
            consecutive += 1
        else:
            break
        i -= 1
        j += 1
    if consecutive >= 4:
        return True

    return False


  def get_positions_gagnantes_avec_ligne(self, colonne, ligne):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # Verticale, Horizontale, Diagonale descendante, Diagonale ascendante
    token = self.grille[ligne][colonne]
    if not token:
        return []

    positions_gagnantes = [[colonne, ligne]]

    for direction in directions:
        dx, dy = direction
        count = 1
        for i in range(1, 4):  # Vérification dans les deux sens à partir de la position donnée
            nx, ny = colonne + dx * i, ligne + dy * i
            if 0 <= nx < self.largeur and 0 <= ny < self.hauteur and self.grille[ny][nx] == token:
                positions_gagnantes.append([nx, ny])
                count += 1
            else:
                break
        for i in range(1, 4):
            nx, ny = colonne - dx * i, ligne - dy * i
            if 0 <= nx < self.largeur and 0 <= ny < self.hauteur and self.grille[ny][nx] == token:
                positions_gagnantes.append([nx, ny])
                count += 1
            else:
                break
        if count >= 4:
            return positions_gagnantes
        positions_gagnantes = [[colonne, ligne]]  # Réinitialisation pour chaque direction

    return []

  def get_positions_gagnantes(self, colonne):
    ligne = self.hauteur - 1
    while ligne >= 0 and not self.case_est_vide(ligne, colonne):
      ligne -= 1
    return self.get_positions_gagnantes_avec_ligne(colonne, ligne)
    
  def get_liste_coups_possibles(self):
    coups = []
    for j in range(self.largeur):
      if self.case_est_vide(0, j):
        coups.append(j)
    return coups


