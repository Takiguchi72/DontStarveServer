'''
Created on 2 déc. 2015

@author: takiguchi
'''

class GestionServeurException(Exception):
    '''
    Exception se levant lors de la manipulation du serveur
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