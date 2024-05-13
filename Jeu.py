# grille 6*7
# 'x','o',''

import random
import tkinter as tk


VERBOSE = False

class Grille :
  def __init__(self, hauteur = 6, largeur = 7):
    self.hauteur = hauteur
    self.largeur = largeur
    self.grille = [['' for i in range(self.largeur)] for j in range(self.hauteur)]

  def vider_grille(self):
    self.grille = [['' for i in range(self.largeur)] for j in range(self.hauteur)]
    
  def __str__(self):
    s = ''
    for i in range(self.hauteur):
      for j in range(self.largeur):
        s += self.grille[i][j] + ' '
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
    
    for i in range(self.hauteur-1, -1, -1):
      if self.case_est_vide(i, colonne):
        self.grille[i][colonne] = joueur
        
        if self.est_gagnant(colonne, i):
          print(joueur + ' a gagne')
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
  
  def est_gagnant(self, colonne, ligne):
    if colonne < 0 or colonne > self.largeur-1 or ligne < 0 or ligne > self.hauteur-1:
      raise ValueError('colonne ou ligne invalide')
      return False
    
    joueur = self.grille[ligne][colonne]

    # Vérification verticale |
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



class JoueurHumain:
  def jouer_coup(self, grille, joueur, colonne_joueur):
    return colonne_joueur
  
class JoueurAleatoire:
  def jouer_coup(self, grille, joueur, colonne_joueur):
    coups_possible = grille.get_liste_coups_possibles()
    return coups_possible[random.randint(0, len(coups_possible)-1)]

class Puissance4(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Puissance 4")
    
    # Jeu
    self.hauteur = 6
    self.largeur = 7
    self.grille = Grille(self.hauteur, self.largeur)
    self.joueur_courant = 0
    self.joueur_symbole = ['x', 'o']
    self.joueurs = [JoueurHumain(), JoueurHumain()]

    self.attente_coup_humain = True
    self.colonne_coup_humain = -1
    
    # Fenetre
    
    self.multiplicateur = 80
    self.geometry(str(self.multiplicateur * self.largeur) + "x" + str(self.multiplicateur * self.hauteur))
        
    self.canvas = tk.Canvas(self, width=self.multiplicateur * self.largeur, height=self.multiplicateur * self.hauteur, bg='blue')
    self.canvas.pack()
    
    self.draw_grid()
    self.canvas.bind("<Button-1>", self.jouer_coup_humain)
    
    
    # Menu
    
    self.menu = tk.Menu(self)
    self.config(menu=self.menu)

    self.type_joueur_x_menu = tk.Menu(self.menu, tearoff=0)
    self.type_joueur_x_menu.add_command(label="Joueur Humain", command=lambda: self.changer_type_joueur("Humain", 0))
    self.type_joueur_x_menu.add_command(label="Joueur Aléatoire", command=lambda: self.changer_type_joueur("Aleatoire", 0))
    self.menu.add_cascade(label="Joueur X : Humain", menu=self.type_joueur_x_menu)
    
    self.type_joueur_o_menu = tk.Menu(self.menu, tearoff=0)
    self.type_joueur_o_menu.add_command(label="Joueur Humain", command=lambda: self.changer_type_joueur("Humain", 1))
    self.type_joueur_o_menu.add_command(label="Joueur Aléatoire", command=lambda: self.changer_type_joueur("Aleatoire", 1))
    self.menu.add_cascade(label="Joueur O : Humain", menu=self.type_joueur_o_menu)
    
    self.menu.add_command(label="Relancer Partie", command=self.relancer_partie)

    self.menu.add_command(label="Tour du joueur : " + self.joueur_symbole[self.joueur_courant])

    self.type_joueur_o = "Humain"  # Par défaut, le joueur est un joueur humain
    self.type_joueur_x = "Humain"
    
    

    


  def draw_grid(self):
    for i in range(6):
      for j in range(7):
        x0 = j * self.multiplicateur
        y0 = i * self.multiplicateur
        x1 = x0 + self.multiplicateur
        y1 = y0 + self.multiplicateur
        self.canvas.create_rectangle(x0, y0, x1, y1, fill='white', outline='black')
        self.canvas.create_text(x0 + self.multiplicateur/2, y0 + self.multiplicateur/2, text=self.grille.get_case(i,j), font=('Arial', 20))

  def jouer_coup_humain(self, event):
    if self.attente_coup_humain:
      self.colonne_coup_humain = event.x // self.multiplicateur
      self.attente_coup_humain = False
        
  def changer_type_joueur(self, type_joueur, joueur):
    if joueur == 0:
      self.type_joueur_o = type_joueur
      self.menu.entryconfig(joueur+1, label="Joueur X : " + type_joueur)
    else:
      self.type_joueur_x = type_joueur
      self.menu.entryconfig(joueur+1, label="Joueur O : " + type_joueur)
      
    switcher = {
      "Humain": JoueurHumain(),
      "Aleatoire": JoueurAleatoire()
    }
    
    self.joueurs[joueur] = switcher.get(type_joueur)

  def relancer_partie(self):
    if VERBOSE:
      print("Relancer Partie")
    
    self.grille.vider_grille()
    
    self.joueur_courant = 1
    self.changer_joueur() # Pour que le joueur 0 commence
    
    self.attente_coup_humain = self.type_joueur_x == "Humain"
    
    self.draw_grid()
    
    self.jouer_coup()
    
    


  def changer_joueur(self):
    self.joueur_courant = (self.joueur_courant + 1) % 2
    self.menu.entryconfig(4, label="Tour du joueur : " + self.joueur_symbole[self.joueur_courant])

  def jouer_coup(self):    
    if self.joueurs[self.joueur_courant].__class__.__name__ == 'JoueurHumain':
      self.attente_coup_humain = True
      while self.attente_coup_humain:
        self.update()
        self.update_idletasks()
    colonne = self.joueurs[self.joueur_courant].jouer_coup(self.grille, self.joueur_symbole[self.joueur_courant], self.colonne_coup_humain)
    
    
    if VERBOSE:
      print("Joueur " + self.joueur_symbole[self.joueur_courant] + " joue en colonne " + str(colonne))
  
    try:
      if self.grille.placer_jeton(self.joueur_symbole[self.joueur_courant], colonne) == True :
        self.draw_grid()
        return
      self.draw_grid()
    except ValueError as e:
      print(e)
    
    self.changer_joueur()
    self.jouer_coup()
    

if __name__ == "__main__":
  app = Puissance4()
  app.mainloop()
