import copy
import numpy as np
from numba import njit

class Grille:
    def __init__(self, hauteur=6, largeur=7, grille=None, coup_prec=[0, 0]):
        self.hauteur = hauteur
        self.largeur = largeur
        self.coup_prec = coup_prec
        if grille is not None:
            self.grille = np.array(grille, dtype=str)
        else:
            self.grille = np.full((self.hauteur, self.largeur), '', dtype=str)

    def __deepcopy__(self, memo):
        return Grille(self.hauteur, self.largeur, self.grille.copy(), self.coup_prec)
    
    def vider_grille(self):
        self.grille = np.full((self.hauteur, self.largeur), '', dtype=str)
        self.coup_prec = [0, 0]

    def case_est_vide(self, ligne, colonne):
        return self.grille[ligne, colonne] == ''

    def get_case(self, ligne, colonne):
        return self.grille[ligne, colonne]

    def est_plein(self):
        return not np.any(self.grille == '')

    def get_coup_prec(self):
        return self.coup_prec
    
    def get_liste_coups_possibles(self):
        coups = []
        for j in range(self.largeur):
          if self.case_est_vide(0, j):
            coups.append(j)
        return coups
      
    def placer_jeton(self, joueur, colonne):
        if colonne < 0 or colonne >= self.largeur:
            raise ValueError('colonne invalide')

        for ligne_i in range(self.hauteur - 1, -1, -1):
            if self.case_est_vide(ligne_i, colonne):
                self.grille[ligne_i, colonne] = joueur
                self.coup_prec = [ligne_i, colonne]

                if self.est_gagnant(ligne_i, colonne):
                    return True

                if self.est_plein():
                    return True

                return False
        raise ValueError('colonne pleine')
        

    def est_gagnant(self, ligne=None, colonne=None):
      return est_gagnant_numba(self.grille, ligne, colonne)

    def get_positions_gagnantes_avec_ligne(self, ligne, colonne):
        if colonne < 0 or colonne >= self.largeur or ligne < 0 or ligne >= self.hauteur:
            raise ValueError('colonne ou ligne invalide')

        joueur = self.grille[ligne, colonne]
        positions_gagnantes = [[ligne, colonne]]  # Liste pour stocker les positions gagnantes

        # Vérification verticale
        consecutive = 1
        for ligne_i in range(ligne - 1, -1, -1):
            if self.grille[ligne_i, colonne] == joueur:
                consecutive += 1
                positions_gagnantes.append([ligne_i, colonne])
            else:
                break
        for ligne_i in range(ligne + 1, self.hauteur):
            if self.grille[ligne_i, colonne] == joueur:
                consecutive += 1
                positions_gagnantes.append([ligne_i, colonne])
            else:
                break
        if consecutive >= 4:
            return positions_gagnantes

        # Vérification horizontale
        consecutive = 1
        for colonne_j in range(colonne - 1, -1, -1):
            if self.grille[ligne, colonne_j] == joueur:
                consecutive += 1
                positions_gagnantes.append([ligne, colonne_j])
            else:
                break
        for colonne_j in range(colonne + 1, self.largeur):
            if self.grille[ligne, colonne_j] == joueur:
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
            if self.grille[ligne_i, colonne_j] == joueur:
                consecutive += 1
                positions_gagnantes.append([ligne_i, colonne_j])
            else:
                break
            ligne_i -= 1
            colonne_j -= 1
        ligne_i, colonne_j = ligne + 1, colonne + 1
        while ligne_i < self.hauteur and colonne_j < self.largeur:
            if self.grille[ligne_i, colonne_j] == joueur:
                consecutive += 1
                positions_gagnantes.append([ligne_i, colonne_j])
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
            if self.grille[ligne_i, colonne_j] == joueur:
                consecutive += 1
                positions_gagnantes.append([ligne_i, colonne_j])
            else:
                break
            ligne_i -= 1
            colonne_j += 1
        ligne_i, colonne_j = ligne + 1, colonne - 1
        while ligne_i < self.hauteur and colonne_j >= 0:
            if self.grille[ligne_i, colonne_j] == joueur:
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
        while ligne < self.hauteur - 1 and self.case_est_vide(ligne, colonne):
            ligne += 1
        return self.get_positions_gagnantes_avec_ligne(ligne, colonne)

    
    def evaluer(self, minimizer, joueur_char, adv_char):
        return evaluer_grille_par_joueur_numba(self.grille, self.get_coup_prec(), minimizer, joueur_char, adv_char) - evaluer_grille_par_joueur_numba(self.grille, self.get_coup_prec(), minimizer, adv_char, joueur_char)


@njit(cache=True)
def est_gagnant_numba(grille, ligne, colonne):
    hauteur, largeur = grille.shape

    if colonne < 0 or colonne >= largeur or ligne < 0 or ligne >= hauteur:
        raise ValueError('colonne ou ligne invalide')

    joueur = grille[ligne, colonne]
    if joueur == 0:
        return False

    def count_consecutive(arr, joueur):
        max_count = count = 0
        for element in arr:
            if element == joueur:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count

    # Vérification verticale |
    colonne_array = grille[:, colonne]
    if count_consecutive(colonne_array, joueur) >= 4:
        return True

    # Vérification horizontale -
    ligne_array = grille[ligne, :]
    if count_consecutive(ligne_array, joueur) >= 4:
        return True

    # Vérification diagonale \
    diag_offset = min(colonne, ligne)
    start_row = ligne - diag_offset
    start_col = colonne - diag_offset
    diag_elements = [grille[start_row + i, start_col + i] for i in range(min(hauteur - start_row, largeur - start_col))]
    if count_consecutive(diag_elements, joueur) >= 4:
        return True

    # Vérification diagonale /
    anti_diag_offset = min(largeur - colonne - 1, ligne)
    start_row = ligne - anti_diag_offset
    start_col = colonne + anti_diag_offset
    anti_diag_elements = [grille[start_row + i, start_col - i] for i in range(min(hauteur - start_row, start_col + 1))]
    if count_consecutive(anti_diag_elements, joueur) >= 4:
        return True

    return False



@njit
def evaluer_grille_par_joueur_numba(grille, couprec, minimizer, joueur_char, joueur_advs_char):
    NB_LIGNES, NB_COLONNES = grille.shape

    if (minimizer and est_gagnant_numba(grille, couprec[0], couprec[1])) :
        return 1000
    if (not minimizer and est_gagnant_numba(grille, couprec[0], couprec[1])) :
        return -1000

    scorePourTrois = 5
    scorePourDeux = 2
    scorePourUn = 0.1

    nb_jeton_par_groupe = [0, 0, 0]  # 0: 1 jeton, 1: 2 jetons, 2: 3 jetons

    # Vérification verticale |
    for colonne_j in range(NB_COLONNES):
        for ligne_i in range(NB_LIGNES - 3):
            segment = grille[ligne_i:ligne_i + 4, colonne_j]
            count_joueur_char = 0
            for element in segment:
                if element == joueur_char:
                    count_joueur_char += 1
            if 0 < count_joueur_char < 4 and joueur_advs_char not in segment:
                nb_jeton_par_groupe[count_joueur_char - 1] += 1

    # Vérification horizontale -
    for ligne_i in range(NB_LIGNES):
        for colonne_j in range(NB_COLONNES - 3):
            segment = grille[ligne_i, colonne_j:colonne_j + 4]
            count_joueur_char = 0
            for element in segment:
                if element == joueur_char:
                    count_joueur_char += 1
            if 0 < count_joueur_char < 4 and joueur_advs_char not in segment:
                nb_jeton_par_groupe[count_joueur_char - 1] += 1

    # Vérification diagonale \
    for ligne_i in range(NB_LIGNES - 3):
        for colonne_j in range(NB_COLONNES - 3):
            segment = np.array([grille[ligne_i + k, colonne_j + k] for k in range(4)])
            count_joueur_char = 0
            for element in segment:
                if element == joueur_char:
                    count_joueur_char += 1
            if 0 < count_joueur_char < 4 and joueur_advs_char not in segment:
                nb_jeton_par_groupe[count_joueur_char - 1] += 1

    # Vérification diagonale /
    for ligne_i in range(3, NB_LIGNES):
        for colonne_j in range(NB_COLONNES - 3):
            segment = np.array([grille[ligne_i - k, colonne_j + k] for k in range(4)])
            count_joueur_char = 0
            for element in segment:
                if element == joueur_char:
                    count_joueur_char += 1
            if 0 < count_joueur_char < 4 and joueur_advs_char not in segment:
                nb_jeton_par_groupe[count_joueur_char - 1] += 1

    return nb_jeton_par_groupe[2] * scorePourTrois + nb_jeton_par_groupe[1] * scorePourDeux + nb_jeton_par_groupe[0] * scorePourUn
  
  

# g = Grille(6,7)
# g.placer_jeton('x', 0)
# g.placer_jeton('x', 0)
# print(g.evaluer(True, 'x', 'o'))
