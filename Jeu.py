# grille 6*7
# 'x','o',''

import copy
import tkinter as tk


class Grille :
  def __init__(self, hauteur = 6, largeur = 7, grille = [], coup_prec=[0,0]):
    self.hauteur = hauteur
    self.largeur = largeur
    self.coup_prec = coup_prec
    if (grille!=[]):
        self.grille = copy.deepcopy(grille)
    else :
        self.grille = [['' for i in range(self.largeur)] for j in range(self.hauteur)]
    
      
  def __deepcopy__() :
      return Grille(self.hauteur, self.largeur, self.grille, self.coup_prec) 
      

  def vider_grille(self):
    self.grille = [['' for i in range(self.largeur)] for j in range(self.hauteur)]
    
  def __str__(self):
    s = ''
    for i in range(self.hauteur):
      for j in range(self.largeur):
        s += self.grille[i][j] + ' '
      s += '\n'
    return s
  

  def case_est_vide(self, ligne, colone):
    return self.grille[ligne][colone] == ''
  
  def get_case(self, ligne, colone):
    return self.grille[ligne][colone]

  def placer_jeton(self, joueur, colonne):
    if colonne < 0 or colonne > self.largeur-1:
      raise ValueError('colonne invalide')
      return False
    
    for i in range(self.hauteur-1, -1, -1):
      if self.case_est_vide(i, colonne):
        self.grille[i][colonne] = joueur
        
        if self.est_gagnant(colonne, i):
          print(joueur + ' a gagne')
          return True

        if self.est_plein():
          print('Match nul')
          return True
        
        return True
    raise ValueError('colonne pleine')
    return False

  def est_plein(self):
    for i in range(self.hauteur):
      for j in range(self.largeur):
        if self.case_est_vide(i, j):
          return False
    return True
  
  def est_gagnant(self, colonne, ligne):
    if colonne < 0 or colonne > self.largeur-1 or ligne < 0 or ligne > self.hauteur-1:
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

    
  def get_liste_coups_possibles(self):
    coups = []
    for j in range(self.largeur):
      if self.case_est_vide(0, j):
        coups.append(j)
    return coups



class Puissance4(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Puissance 4")
        
        self.hauteur = 6
        self.largeur = 7
        self.grille = Grille( self.hauteur, self.largeur)
        
        self.multiplicateur = 40
        self.geometry(str(self.multiplicateur * self.largeur) + "x" + str(self.multiplicateur * self.hauteur))
            
        self.canvas = tk.Canvas(self, width=self.multiplicateur * self.largeur, height=self.multiplicateur * self.hauteur, bg='blue')
        self.canvas.pack()
        
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.jouer_coup)

    def draw_grid(self):
        for i in range(6):
            for j in range(7):
                x0 = j * self.multiplicateur
                y0 = i * self.multiplicateur
                x1 = x0 + self.multiplicateur
                y1 = y0 + self.multiplicateur
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='white', outline='black')
                self.canvas.create_text(x0 + self.multiplicateur/2, y0 + self.multiplicateur/2, text=self.grille.get_case(i,j), font=('Arial', 20))

    def jouer_coup(self, event):
        colonne = event.x // self.multiplicateur
        try:
            self.grille.placer_jeton('x', colonne)
            self.draw_grid()
        except ValueError as e:
            print(e)




if __name__ == "__main__":
  app = Puissance4()
  app.mainloop()
