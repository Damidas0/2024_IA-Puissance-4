import copy

from EvaluerGrille import evaluer_grille


class AlphaBeta:
    def __init__(self, profondeur=6):
        self.profondeur = profondeur

    def jouer_coup(self, grille, joueur, inutile_mais_necessaire):
        meilleur_coup = None
        meilleur_score = float('-inf')

        for coup in grille.get_liste_coups_possibles():
            copie_grille = copy.deepcopy(grille)
            copie_grille.placer_jeton(joueur, coup)
            score = self.alpha_beta(copie_grille, self.profondeur, float('-inf'), float('inf'), joueur, False)
            
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = coup

        return meilleur_coup

    def alpha_beta(self, grille, profondeur, alpha, beta, joueur, est_maximisant):
        if profondeur == 0 or grille.est_gagnant(grille.get_coup_prec()[0], grille.get_coup_prec()[1]) or grille.est_plein():
            return evaluer_grille(grille, not(est_maximisant), joueur, 'o' if joueur == 'x' else 'x')

        if est_maximisant:
            valeur_max = float('-inf')
            for coup in grille.get_liste_coups_possibles():
                copie_grille = copy.deepcopy(grille)
                copie_grille.placer_jeton(joueur, coup)
                valeur_max = max(valeur_max, self.alpha_beta(copie_grille, profondeur - 1, alpha, beta, joueur, False))
                alpha = max(alpha, valeur_max)
                if alpha >= beta:
                    break
            return valeur_max
        else:
            valeur_min = float('inf')
            adversaire = 'o' if joueur == 'x' else 'x'
            for coup in grille.get_liste_coups_possibles():
                copie_grille = copy.deepcopy(grille)
                copie_grille.placer_jeton(adversaire, coup)
                valeur_min = min(valeur_min, self.alpha_beta(copie_grille, profondeur - 1, alpha, beta, joueur, True))
                beta = min(beta, valeur_min)
                if alpha >= beta:
                    break
            return valeur_min