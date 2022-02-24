# import de bibliotheque
import random
import time

# creation des cases disponible
cases = [i for i in range(1,50+1)]

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
            affiche tous les comptes des utilisateurs avec leur solde.

        '''
        return f"{self.content}"
    
    def all_users(self):
        '''

        Returns
        -------
        dict
            renvoie tous les comptes des utilisateurs avec leur solde.

        '''
        return self.content
    
    def add_user(self, username :str, monnaie :float=0):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.
        monnaie : float, optional
            le nombre de monnaie qu'il faut ajouter au compte de `username`. The default is 0.

        Returns
        -------
        bool
            True = l'initialisation du nouveau compte effectue avec succès.
            False = l'initialisation du nouveau compte n'a pas conclus puisque le compte existe deja.

        '''
        if username not in self.content:
            self.content[username] = monnaie
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
        return f"{username} : {self.content[username]}"
    
    def edit_monnaie(self, username :str, new_monnaie :float):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.
        new_monnaie : float
            la nouvelle valeur du solde de l'utilisateur donne en parametre.

        Returns
        -------
        None.

        '''
        self.content[username] = new_monnaie
    
    def get_monnaie(self, username :str):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.

        Returns
        -------
        TYPE
            renvois le solde de l'utilisateur donne en parametre.

        '''
        return self.content[username]
    
    def add_monnaie(self, username :str, add :float):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.
        add : float
            le nombre de monnaie a ajoute au solde de l'utilisateur donne en parametre.

        Returns
        -------
        None.

        '''
        self.content[username] += add
    
    def remove_monnaie(self, username :str, remove :float):
        '''

        Parameters
        ----------
        username : str
            le nom d'un utilisateur.
        remove : float
            le nombre de monnaie a enleve au solde de l'utilisateur donne ne parametre.

        Returns
        -------
        None.

        '''
        self.content[username] -= remove

def roulette(case :int, mise :float=0):
    '''

    Parameters
    ----------
    case : int
        la case choisie par l'utilisateur.
    mise : float, optional
        monnaie mis en jeu. The default is 0.

    Returns
    -------
    float
        gains.

    '''
    
    # tirage de la case gagnante
    case_gagnante = random.choice(cases)
    
    # suspense
    time.sleep(1)
    print('\n3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1\n')
    time.sleep(1)
    
    # informe l'utilisateur + renvois les gains
    if case_gagnante == case :
        print(f"Case Gagnante : {case_gagnante} | !!! WIN !!! | Gain : {mise*3}")
        return mise*3
    elif (case%2 == 0) == (case_gagnante%2 == 0):
        print(f"Case Gagnante : {case_gagnante} | WIN | Gain : {mise*1.5}")
        return mise*1.5
    else:
        print(f"Case Gagnante : {case_gagnante} | LOOSE | Gain : {mise*0}")
        return mise*0
    
def launch_roulette(nbr :int=0, username :str=''):
    '''

    Parameters
    ----------
    nbr : int, optional
        nombre de parties joue. The default is 0.
    username : str, optional
        le nom de l'utilisateur precedemment  utilise (si relance). The default is ''.

    Returns
    -------
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
    drapeau6 = False
    drapeau7 = False
    drapeau8 = False
    drapeau9 = False
    
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
            new_user = str(input('Quel est votre nom ?\n'))
            temoin1 = users.add_user(new_user.lower())
            if temoin1 == False:
                drapeau4 = True
                pass
            if drapeau4 == False:
                try:
                    add_monnaie = float(input('Combien, voulez-vous donner de monnaie ?\n'))
                    drapeau4 = True
                except:
                    drapeau4 = False 
            if temoin1 == True:
                users.add_monnaie(new_user, add_monnaie)
            username = new_user
        # lancement d'un compte existant
        else:
            while drapeau5 == False:
                username = str(input('Quel est votre nom ?\n'))
                if username.lower() == 'exit':
                    return launch_roulette()
                elif username.lower() in users.all_users():
                    drapeau5 = True
    
    # lancement de la partie    
    
    # case mis en jeu
    while drapeau6 == False:
        case = int(input(f"Sur quelle case voulez-vous miser ?\n(Couleurs disponibles : {cases})\n"))
        if case in cases:
            drapeau6 = True
    
    # somme mise en jeux + ajout de monnaie
    while drapeau7 == False:
        # demmande de la somme mis en jeux
        if users.get_monnaie(username) == 0:
            print(f"\nVotre solde est a {users.get_monnaie(username)}.")
            add_monnaie(username)
        mise = input('Combien, voulez-vous miser ?\n(Vous pouvez faire la commande `solde` pour voir votre solde)\n')
        try:
            if mise == '':
                drapeau7 = False
            elif mise == 'solde':
                drapeau7 = False
                print(users.get_monnaie(username))
            elif float(mise) <= users.get_monnaie(username):
                users.remove_monnaie(username, float(mise))
                drapeau7 = True
            # ajout de monnaie
            else:
                print("Il n'y a pas assez de monnaie.")
                while drapeau8 == False:
                    temoin2 = str(input('Voulez-vous ajouter de la monnaie ?\n(Reponses attendu : O/N)\n'))
                    if temoin2 == 'O' or temoin2 == 'o':
                        add_monnaie(username)
                        drapeau8 = True
                    elif temoin2 == 'N' or temoin2 == 'n':
                        drapeau8 = True
                drapeau7 = False
        except:
            drapeau7 = False
    
    # tirage au sort de la case gagnante + resultat
    resultat = roulette(case, float(mise))
    
    # ajout des gains
    users.add_monnaie(username, resultat)
    
    # demande de relance
    while drapeau9 == False:
        retry = str(input('Voulez-vous continuer a jouer ?\n(Reponses attendu : O/N)\n'))
        if retry == 'O' or retry == 'o':
            drapeau9 = True
            return launch_roulette(1, username)
        elif retry == 'N' or retry == 'n':
            drapeau9 = True
            return

def add_monnaie(username :str):
    '''

    Parameters
    ----------
    username : str
        le nom d'un utilisateur.

    Returns
    -------
    None.
    
    Description
    -------
        cette fonction permet d'ajouter de la monnaie a un utilisateur 
        renseigner en parametre.

    '''
    drapeau10 = False
    
    while drapeau10 == False:
        try:
            add_monnaie = float(input('Combien, voulez-vous ajouter de monnaie ?\n'))
            drapeau10 = True
        except:
            drapeau10 = False 
    users.add_monnaie(username, add_monnaie)
    return 

# ---

# Initialisation
users = Users()

# Lancement
launch_roulette()