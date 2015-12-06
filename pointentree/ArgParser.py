'''
Created on 28 nov. 2015

@author: takiguchi
'''
import argparse
# from ArgumentException import ArgumentException
# from VariablesGlobales import listeOperations
from pointentree.ArgumentException import ArgumentException
from pointentree.VariablesGlobales import listeOperations

class Argparser(object):
    '''
    Objet permettant d'analyser la ligne de commande lors de l'appel du programme.
    '''
    
    def __init__(self):
        '''
        Initialise l'objet à partir de la ligne de commande 
        lors de l'appel du programme.
        
        @raise ArgumentException: Si la valeur de l'argument positionnel 
                            "operation" n'est pas présente dans la liste
                            "listeOperation".
        '''
        # Initialisation des arguments à l'objet
        self.arguments = argparse.Namespace()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("operation",
                                 help = "L'opération que le serveur doit exécuter")
        
        # Récupération des valeurs de la CLI pour les stocker dans l'objet 'valeurs'
        self.valeurs = self.parser.parse_args()
        
        # Vérification de l'opération demandée
        self.__checkArgues__()
        
    def __checkArgues__(self):
        '''
        Vérifie que l'argument renseigné fait partie d'une commande prise en charge
        
        @raise ArgumentException: Si la valeur de l'argument positionnel 
                            "operation" n'est pas présente dans la liste
                            "listeOperation".
        '''
        if(not self.valeurs.operation in listeOperations):
            raise ArgumentException("L'instruction demandée n'est pas prise en charge ! ({0})".format(self.valeurs.operation))