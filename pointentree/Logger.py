'''
Created on 2 déc. 2015

@author: takiguchi
'''
import logging
from pointentree.VariablesGlobales import dateExecution, pathDstConfig

class Logger(logging.Logger):
    '''
    classdocs
    '''

    def __init__(self, name, level):
        '''
        Constructor
        '''
        # On initialise l'objet comme logger root
        logging.Logger.__init__(self, name, level)
        
        # On définit le nom du fichier de logs à partir de la date et l'heure
        self.nomFichierLogs = dateExecution + ".log"
        
        # On définit un pattern pour les logs
        logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
        
        # On créer un sous logger pour écrire dans le fichier de logs
        fileHandler = logging.FileHandler("{0}/{1}.log".format(pathDstConfig,
                                                               self.nomFichierLogs)).setFormatter(logFormatter)
        self.addHandler(fileHandler)
        
        logFormatter = logging.Formatter("[%levelname) -5.5s] %(message)s")
        
        # On créer un sous logger pour écrire dans la console
        consoleHandler = logging.StreamHandler().setFormatter(logFormatter)
        self.addHandler(consoleHandler)