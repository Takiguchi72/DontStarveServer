'''
Created on 3 déc. 2015

@author: takiguchi
'''

class ExecutionCommandeException(Exception):
    '''
    Exception se levant lors de l'echec d'exécution d'une commande
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