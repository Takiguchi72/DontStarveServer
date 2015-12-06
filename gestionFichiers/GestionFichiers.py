'''
Created on 1 déc. 2015

@author: takiguchi
'''

import os
from gestionFichiers.GestionFichierException import GestionFichierException

def creerDossier(pChemin):
    '''
    Créer un dossier au chemin spécifié en paramètre
    
    @param pChemin: Le chemin où il faut créer le dossier.
                    Seul le dossier le plus à droite sera créé
                    
    @raise GestionFichierException: Si le dossier à créer existe déjà
    '''
    try:
        os.mkdir(pChemin, mode=0o777)
    except OSError as err:
        raise GestionFichierException(err)
    
def creerArborescence(pArborescence):
    '''
    Créer le dossier spécifié en paramètre, ainsi que ses dossiers parents s'ils n'existent pas
    
    @param pArborescence: Le chemin où il faut créer le dossier
    
    @raise GestionFichierException: Si le dossier à créer existe déjà
    '''
    try:
        os.makedirs(pArborescence, mode=0o777)
    except OSError as err:
        raise GestionFichierException(err)

def isDossierVide(pChemin):
    '''
    Indique si le dossier en paramètre est vide ou non
    '''
    return not len(os.popen("ls " + pChemin).read().split("\n")) > 1