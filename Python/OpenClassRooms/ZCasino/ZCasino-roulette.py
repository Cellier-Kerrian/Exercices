# import de bibliotheque
import random

def roulette(case :int, mise :float=0):
    '''

    Parameters
    ----------
    case : int
        le nombre qui correspond a la case voulue.

    Returns
    -------
    bool
        True = Gagner.
        False = Perdu.
        
    Description
    -------
        un jeu de casino propose par OpenClassRooms.

    '''
    # creation des cases disponible
    cases = [i for i in range(1,50+1)]
    
    # tirage de la case gagnante
    case_gagnante = random.choice(cases)
    
    # informe l'utilisateur + renvois les gains
    if case_gagnante == case :
        print(f"Case Gagnante : {case_gagnante} | !!! WIN !!! | Gain : {mise*3}")
        return False
    elif (case%2 == 0) == (case_gagnante%2 == 0):
        print(f"Case Gagnante : {case_gagnante} | WIN | Gain : {mise*1.5}")
        return True
    else:
        print(f"Case Gagnante : {case_gagnante} | LOOSE | Gain : {mise*0}")
        return False