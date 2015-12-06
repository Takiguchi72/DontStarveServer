'''
Created on 01 dec. 2015

@author: takiguchi
'''

class GestionFichierException(Exception):
    '''
    Exception se levant lors de l'analyse de la ligne de commande
    '''

    def __init__(self, pValue):
        '''
        Constructor
        '''
        self.value = pValue
        
    def __str__(self):
        '''
        Retourne le message de l'exception
        @return Le message de l'exception
        '''
        return repr(self.value)