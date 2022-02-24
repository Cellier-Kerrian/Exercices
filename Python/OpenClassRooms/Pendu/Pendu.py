# import de bibliotheque
import random

def charge_dictionnaire():
    '''

    Returns
    -------
    liste_mots : list
        une liste qui contient des mots (str).
        
    Description
    ------
        permet de creer une liste de mots present dans un fichier .txt (un 
        fichier externe) afin qu'il puisse etre exploiter par le programme.

    '''
    liste_mots = []
    with open("dictionnaire-francais.txt", "r") as f:
        for mot in f.readlines():
            mot = mot.strip().upper()
            liste_mots.append(mot)
    return liste_mots

# liste_mot contient la liste de tous les mots disponible
liste_mots = charge_dictionnaire()

# ---

class Users():
    '''
    class = User, creation du system de point.
    '''
    def __init__(self):
        '''
        constructeur = creer un dictionnaire.
        '''
        self.content = {}
        
    def __repr__(self):
        '''

        Returns
        -------
        str
            affiche tous les comptes des utilisateurs avec leur nombre de points.

        '''
        return f"{self.content}"
        
    def all_users(self):
        '''

        Returns
        -------
        dict
            renvois tous les comptes des utilisateurs avec leur solde.

        '''
        return self.content
    
    def add_user(self, username :str, points :float=0):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.
        monnaie : float, optional
            le nombre de points qu'il faut ajouter au compte de `username`. The default is 0.

        Returns
        -------
        bool
            True = l'initialisation du nouveau compte effectue avec succès.
            False = l'initialisation du nouveau compte n'a pas conclus puisque le compte existe deja.

        '''
        if username not in self.content:
            self.content[username] = points
            return True 
        else:
            print("\nUtilisateur existant.")
            return False
    
    def edit_username(self, old_name : str, new_name :str):
        '''

        Parameters
        ----------
        old_name : str
            l'ancien nom de l'utilisateur.
        new_name : str
            le nouveau nom de l'utilisateur.

        Returns
        -------
        None.

        '''
        self.content[new_name] = self.content.pop(old_name)
    
    def get_user(self, username :str):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.

        Returns
        -------
        str
            affiche le compte de l'utilisateur donne en parametre.

        '''
        return f"{self.content[username]} : {self.points}"
    
    def edit_points(self, username :str, new_points :float):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.
        new_monnaie : float
            le nouveau nombre de points de l'utilisateur donne en parametre.

        Returns
        -------
        None.

        '''
        self.content[username] = new_points
    
    def get_points(self, username :float):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.

        Returns
        -------
        TYPE
            renvois le nombre de points de l'utilisateur donne en parametre.

        '''
        return self.content[username]
    
    def add_points(self, username :str, add :float):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.
        add : float
            le nombre de points a ajoute au solde de l'utilisateur donne en parametre.

        Returns
        -------
        None.

        '''
        self.content[username] += add
    
    def remove_points(self, username :str, remove :float):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.
        remove : float
            le nombre de points a enleve au solde de l'utilisateur donne ne parametre.

        Returns
        -------
        None.

        '''
        self.content[username] -= remove
        
def pendu():
    '''

    Returns
    -------
    coups : int
        le nombre de coups qu'il restait au joueur, et donc son score final.
        
    Description
    -------
        c'est un jeu qui consiste a trouver un mot que mystere en un certain 
        nombre de coups maximum.

    '''
    # initialisation du jeu
    mot_mystere = random.choice(liste_mots).upper() # selection du mot mystere
    propositions = []
    coups = 8 # nombre de coups maximum que le joueur peur effectuer
    mot = genere_mot(mot_mystere, propositions) # creer le meme mot que le mot mystere mais cacher, en fonction des lettres proposer (qui sont dans proposition)
    
    while ((mot != mot_mystere) and (coups != 0)):
        
        # points de controle
        drapeau1 = False
        
        # information pour l'utilisateur
        print(f"\nMot mystere : {mot} | nombre de coups restant : {coups} { f'| Lettres proposees : {propositions}' if propositions != [] else ''}")
        
        # demande a l'utilisateur pour la lettre propose
        while drapeau1 == False:
            lettre = str(input("Quelle lettre voulez-vous proposer ?\n"))
            lettre = lettre.upper()
            if lettre == mot_mystere:
                print(f"\nWIN | Points gagnes : {coups}")
                return coups
            elif ((len(lettre) == 1) and (lettre.isalpha())):
                if lettre in propositions:
                    print('Lettre deja proposer.')
                    temoin = False
                else:
                    propositions.append(lettre)
                    propositions = sorted(propositions)
                    drapeau1 = True
                    temoin = True
                    
                if temoin == True:
                    if lettre not in mot_mystere:
                        coups -= 1
        
        # recreer le meme mot que le mot mystere mais cacher, en fonction des lettres proposer (qui sont dans proposition)
        mot = genere_mot(mot_mystere, propositions)
    
    # informe le joueur s'il a perdu ou gagner, avec son score
    if mot == mot_mystere:
        print(f"\nWIN | Points gagnes : {coups}")
    else:
        print(f"\nLOOSE | Mot mystère : {mot_mystere} | Points gagnes : {coups}")
    return coups

def genere_mot(mot_mystere,propositions):
    '''

    Parameters
    ----------
    mot_mystere : str
        le mot mystere que le joueur doit trouver.
    propositions : list
        liste de lettre proposee par le joueur.

    Returns
    -------
    motif : str
        un mot qui contient un symbole pour les lettres qu'il n'a pas trouve 
        et les lettres clairement affichees pour celle qu'il a trouve.
        
    Description
    -------
        genere une chaine de caractere qui represente les lettres que le 
        joueur n'a pas encore trouvees.

    '''
    motif = ""
    for i in range (0,len(mot_mystere)):
        if mot_mystere[i] in propositions:
            motif = motif+mot_mystere[i]
        else:
            motif = motif + '*'
    return motif

def launch_pendu(nbr :int=0, username :str=''):
    '''

    Parameters
    ----------
    nbr : int, optional
        nombre de parties joue. The default is 0.
    username : str, optional
        le nom de l'utilisateur precedemment utiliser (si relance). The default is ''.

    Returns
    -------
    TYPE
    None.
    
    Description
    -------
        lanceur du jeu et gerant du systeme de point en fonction des 
        utilisateurs.

    '''
    
    # points de controle
    drapeau1 = False
    drapeau2 = False
    drapeau3 = False
    drapeau4 = False
    drapeau5 = False
    
    # initialisation de l'utilisateur qui joue
    
    # nouvelle partie sans changer de compte
    if nbr > 0:
        while drapeau1 == False:
            retry_account = str(input('Voulez-vous utiliser le meme utilisateur ?\n(Reponses attendu : O/N)\n'))
            if retry_account == 'O' or retry_account == 'o':
                drapeau1 = True
                drapeau2 = True
                drapeau3 = True
            elif retry_account == 'N' or retry_account == 'n':
                drapeau1 = True
    
    # compte existant ?
    while drapeau2 == False:
        new = str(input('Avez-vous deja un compte ?\n(Reponses attendu : O/N)\n'))
        if new == 'O' or new == 'o':
            new = False
            drapeau2 = True
        elif new == 'N' or new == 'n':
            new = True
            drapeau2 = True
          
    # creation d'un nouveau compte ou lancement d'un compte existant
    if drapeau3 == False:
        # creation d'un nouveau compte + initialisation
        if new == True:
            username = str(input('Quel est votre nom ?\n'))
            temoin = users.add_user(username.lower())
            if temoin == True:
                print(f"\nCompte creer sous le nom : {username} !")
                # lancement d'un compte existant
        else:
            while drapeau4 == False:
                username = str(input('Quel est votre nom ?\n'))
                if username.lower() == 'exit':
                    return launch_pendu()
                elif username.lower() in users.all_users():
                    drapeau4 = True
    
    # lancement du jeu + score obtenu
    resultat = pendu()
    
    # ajout du score que le joueur a obtenu
    users.add_points(username, resultat)
    
    # demande de relance
    while not drapeau5:
        retry = str(input('Voulez-vous continuer a jouer ?\n(Reponses attendu : O/N)\n'))
        if retry == 'O' or retry == 'o':
            drapeau5 = True
            return launch_pendu(1, username)
        elif retry == 'N' or retry == 'n':
            drapeau5 = True
            return

# ---

# Initialisation
users = Users()

# Lancement
launch_pendu()