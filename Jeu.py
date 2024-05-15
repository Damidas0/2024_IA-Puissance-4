import tkinter as tk

from Grille import Grille
from Joueur import JoueurHumain, JoueurAleatoire
from Minmax import MinMax
from AlphaBeta import AlphaBeta

VERBOSE = False


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
    self.joueurs = [JoueurAleatoire(), JoueurAleatoire()]
    self.positions_gagnantes = []

    self.attente_coup_humain = True
    self.colonne_coup_humain = -1
    
    self.types_de_joueur = ["Humain", "Aleatoire", "MinMax", "AlphaBeta", "MCTS"]
    
    
    # Fenetre
    
    self.multiplicateur = 80
    self.geometry(str(self.multiplicateur * self.largeur) + "x" + str(self.multiplicateur * self.hauteur))
        
    self.canvas = tk.Canvas(self, width=self.multiplicateur * self.largeur, height=self.multiplicateur * self.hauteur, bg='blue')
    self.canvas.pack()
    
    self.draw_grid()
    self.canvas.bind("<Button-1>", self.jouer_coup_humain)
    
    
    self.create_menu()
    

    

  def create_menu(self):
    self.menu = tk.Menu(self)
    self.config(menu=self.menu)
    
    self.type_joueur_x_menu = tk.Menu(self.menu, tearoff=0)
    self.type_joueur_o_menu = tk.Menu(self.menu, tearoff=0)
    
    self.type_joueur_x_menu.add_command(label="Joueur "+self.types_de_joueur[0], command=lambda: self.changer_type_joueur(0, 0))
    self.type_joueur_x_menu.add_command(label="Joueur "+self.types_de_joueur[1], command=lambda: self.changer_type_joueur(1, 0))
    self.type_joueur_x_menu.add_command(label="Joueur "+self.types_de_joueur[2], command=lambda: self.changer_type_joueur(2, 0))
    self.type_joueur_x_menu.add_command(label="Joueur "+self.types_de_joueur[3], command=lambda: self.changer_type_joueur(3, 0))
    self.type_joueur_x_menu.add_command(label="Joueur "+self.types_de_joueur[4], command=lambda: self.changer_type_joueur(4, 0))
    self.type_joueur_o_menu.add_command(label="Joueur "+self.types_de_joueur[0], command=lambda: self.changer_type_joueur(0, 1))
    self.type_joueur_o_menu.add_command(label="Joueur "+self.types_de_joueur[1], command=lambda: self.changer_type_joueur(1, 1))
    self.type_joueur_o_menu.add_command(label="Joueur "+self.types_de_joueur[2], command=lambda: self.changer_type_joueur(2, 1))
    self.type_joueur_o_menu.add_command(label="Joueur "+self.types_de_joueur[3], command=lambda: self.changer_type_joueur(3, 1))
    self.type_joueur_o_menu.add_command(label="Joueur "+self.types_de_joueur[4], command=lambda: self.changer_type_joueur(4, 1))
          
    
    joueur_par_defaut = 1
    
    self.menu.add_cascade(label="Joueur X :"+self.types_de_joueur[joueur_par_defaut], menu=self.type_joueur_x_menu)
    self.menu.add_cascade(label="Joueur O :"+self.types_de_joueur[joueur_par_defaut], menu=self.type_joueur_o_menu)
    
    
    self.menu.add_command(label="Relancer Partie", command=self.relancer_partie)

    self.menu.add_command(label="Tour du joueur : " + self.joueur_symbole[self.joueur_courant])

    self.type_joueur_o = self.types_de_joueur[joueur_par_defaut]  # Par défaut, le joueur est Aléatoire
    self.type_joueur_x = self.types_de_joueur[joueur_par_defaut]
    


  def draw_grid(self):
    for ligne_i in range(6):
      for colone_j in range(7):
        color_fill = 'white'
        if (self.grille.get_case(ligne_i,colone_j) == 'x'):
          color_fill = 'red'
        elif (self.grille.get_case(ligne_i,colone_j) == 'o'):
          color_fill = 'blue'
          
        color_outline = 'black'
        if (self.positions_gagnantes != [] and [ligne_i,colone_j] in self.positions_gagnantes):
          color_outline = 'green'
          color_fill = 'green'
        
        x0 = colone_j * self.multiplicateur
        y0 = ligne_i * self.multiplicateur
        x1 = x0 + self.multiplicateur
        y1 = y0 + self.multiplicateur
        
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_fill, outline=color_outline)
        self.canvas.create_text(x0 + self.multiplicateur/2, y0 + self.multiplicateur/2, text=self.grille.get_case(ligne_i,colone_j), font=('Arial', 20))

  def jouer_coup_humain(self, event):
    if self.attente_coup_humain:
      self.colonne_coup_humain = event.x // self.multiplicateur
      self.attente_coup_humain = False
        
  def changer_type_joueur(self, type_joueur, joueur):
    if VERBOSE:
      print("Changement de joueur :",type_joueur, joueur)
    
    if joueur == 0:
      self.type_joueur_o = type_joueur
      self.menu.entryconfig(joueur+1, label="Joueur X : " + self.types_de_joueur[type_joueur])
    else:
      self.type_joueur_x = type_joueur
      self.menu.entryconfig(joueur+1, label="Joueur O : " + self.types_de_joueur[type_joueur])
      
    if (type_joueur == 0) : self.joueurs[joueur] = JoueurHumain()
    elif (type_joueur == 1) : self.joueurs[joueur] = JoueurAleatoire()
    elif (type_joueur == 2) : self.joueurs[joueur] = MinMax( 'x' if joueur == 0 else 'o')
    elif (type_joueur == 3) : self.joueurs[joueur] = AlphaBeta()
    elif (type_joueur == 4) : self.joueurs[joueur] = JoueurAleatoire()
    else : self.joueurs[joueur] = JoueurAleatoire()

  def relancer_partie(self):
    if VERBOSE:
      print("Relancer Partie")
    
    self.grille.vider_grille()
    self.positions_gagnantes = []
    
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
        print(self.joueur_symbole[self.joueur_courant] + ' a gagne')
        
        self.positions_gagnantes = self.grille.get_positions_gagnantes(colonne)
        print(self.positions_gagnantes)
        self.draw_grid()
        return
      
      self.draw_grid()
    except ValueError as e:
      print(e)
    
    self.changer_joueur()
    
    self.after(1, self.jouer_coup)
    

if __name__ == "__main__":
  app = Puissance4()
  app.mainloop()
