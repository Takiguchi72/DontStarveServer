'''
Created on 3 déc. 2015

@author: takiguchi
'''
import os
from pointentree.VariablesGlobales import valDstScreen
from pointentree.ExecutionCommandeException import ExecutionCommandeException

def codeRetourZero(pCodeRetour):
    '''
    Indique si le code retour est '0'
    
    @param pCodeRetour: Le code retour à tester
    
    @return True si le code retour est '0', False si non
    '''
    return True if pCodeRetour == 0 else False

def screenEnFonctionnement():
    '''
    Indique si un screen portant le nom du screen du serveur DST est en fonctionnement
    
    @return True si le dit screen est en fonctionnement, False si non 
    '''
    return True if len(os.popen("screen -ls | grep {0}".format(valDstScreen)).read()) > 0 else False

def executerCommande(pCommande, pMessageSiEchec):
    '''
    Exécute la commande passée en paramètre, et lève une exception si le code retour n'est pas '0'
    
    @param pCommande: La commande à exécuter
    
    @param pMessageSiEchec: Le message de l'exception si la commande échoue
    
    @raise ExecutionCommandeException: Si le code retour de la commande est différent de '0'
    '''
    codeRetour = os.system(pCommande)
    
    if(codeRetourZero(codeRetour)):
        raise ExecutionCommandeException(pMessageSiEchec)