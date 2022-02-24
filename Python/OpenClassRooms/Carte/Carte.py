# import de bibliotheque
import random

# initialisation des valeurs afin de creer les cartes
valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi', 'as']
enseignes = ['pique', 'coeur', 'carreau', 'trefle']
couleurs = {'pique': 'noir', 'coeur': 'rouge', 'carreau': 'rouge', 'trefle': 'noir'}

class Carte:
    '''
    class = Carte, creation de carte.
    '''
    def __init__(self, valeur : str, enseigne :str):
        '''
        constructeur = creer une carte.
        '''
        # erreur - si la valeur renseignee est etrangere aux valeurs prevue
        if valeur not in valeurs:
            raise ValueError(f"valeur inconnue : {valeur}")
        
        # erreur - si l'enseigne renseigner est etrangere aux enseignes prevue
        if enseigne not in enseignes:
            raise ValueError(f"enseigne inconnue : {enseigne}")
            
        self.valeur = valeur
        self.enseigne = enseigne
        
    def __repr__(self):
        '''

        Returns
        -------
        str
            affiche une carte.

        '''
        return f"<Carte(valeur={self.valeur}, enseigne={self.enseigne}"
    
    def __str__(self):
        '''

        Returns
        -------
        str
            permet d'afficher ce que contient une carte (haut niveau).

        '''
        return f"{self.valeur} de {self.enseigne}"
    
    def couleur(self):
        '''

        Returns
        -------
        str
            renvois la couleur de la carte.

        '''
        return couleurs[self.enseigne]
    
class Jeu52Cartes(Carte):
    '''
    class = Jeu52Cartes, creer un jeu de 52 Carte.
    heritage = Carte, creation de carte.
    '''
    def __init__(self):
        '''
        constructeur = creer un jeu de cartes vide, sous forme d'une liste.
        '''
        self.paquet = []
        
        for i in enseignes:
            for j in valeurs:
                carte = Carte(j, i)
                self.paquet.append(carte)
    
    def __str__(self):
        '''

        Returns
        -------
        str
            permet d'afficher le jeu de cartes (haut niveau).

        '''
        return f"{self.paquet}"
    
    def __len__(self):
        '''

        Returns
        -------
        int
            renvois la taille du jeu de cartes.

        '''
        return len(self.paquet)
    
    def __contains__(self, carte):
        '''

        Parameters
        ----------
        carte : Carte
            une carte.

        Returns
        -------
        bool
            True = la carte est presente dans le jeu de carte.
            False = la carte n'est pas presente dans le jeu de carte.

        '''
        return carte in self.paquet
    
    def melanger(self):
        '''

        Returns
        -------
        None.
        
        Description
        -------
            melange la jeu de cartes.

        '''
        random.shuffle(self.paquet)
    
    def pioche(self):
        '''

        Returns
        -------
        Carte
            renvois une carte.

        '''
        if self.paquet == []:
            return "Le jeu de cartes ne contient plus de carte."
        return self.paquet.pop(0)   