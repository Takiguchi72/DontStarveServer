#!/usr/bin/python3
'''
Created on 28 nov. 2015

@author: takiguchi
'''
import sys
import logging
from pointentree.ArgumentException import ArgumentException
from pointentree.ArgParser import Argparser 
from pointentree.Logger import Logger
from gestionServeur.GestionServeur import Serveur

log = Logger(None, logging.DEBUG)

def checkOs():
    '''
    Si le système, sur lequel le programme est appelé, est Windows, le programme s'arrête en affichant un message d'erreur
    '''
    global log
    
    if(sys.platform == "win32"):
        log.error("Ce programme a été conçu pour ne fonctionner que sur un environnement Unix/GNU-Linux")
        sys.exit(1)

if __name__ == '__main__':
    
    # On vérifie qu'on est bien sur un système Unix/GNU-Linux
    checkOs()
      
    try:
        valeursCli = Argparser()
        log.info("Opération : {0}".format(valeursCli.operation))
        
        serveur = Serveur()
          
        if(valeursCli.operation == "start"):
            serveur.start()
            
        elif(valeursCli.operation == "stop"):
            serveur.stop()
            
        elif(valeursCli.operation == "restart"):
            serveur.restart()
            
        elif(valeursCli.operation == "install"):
            serveur.install()
            
        elif(valeursCli.operation == "update"):
            serveur.update()
            
        elif(valeursCli.operation == "save"):
            serveur.save()
            
        else:
            raise ArgumentException("L'argument \"{0}\" n'est pas encore prit en charge !".format(valeursCli.operation))
          
    except ArgumentException as err:
        log.error("Erreur d'arguments : {0}".format(err))
        sys.exit(1)
    except Exception as err:
        log.error("Erreur inconnue : {0}".format(err))
        sys.exit(1)
      
    sys.exit(0)