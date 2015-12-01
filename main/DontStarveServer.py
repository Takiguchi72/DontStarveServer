'''
Created on 28 nov. 2015

@author: takiguchi
'''
import sys
from main.ArgumentException import ArgumentException
from main import ArgParser

def printerr(message):
    '''
    Affiche le paramètre de la fonction comme message d'erreur
    
    @param message: Le message à afficher comme erreur
    '''
    sys.stderr.write(message)

def checkOs():
    '''
    Si le système, sur lequel le programme est appelé, est Windows, le programme s'arrête en affichant un message d'erreur
    '''
    if(sys.platform == "win32"):
        printerr("Ce programme a été conçu pour ne fonctionner que sur un environnement Unix/GNU-Linux")
        sys.exit(1)


if __name__ == '__main__':
    # On vérifie qu'on est bien sur un système Unix/GNU-Linux
    checkOs()
    
    try:
        valeursCli = ArgParser.Argparser()
        print(valeursCli.valeurs.operation)
    except ArgumentException as err:
        printerr("Erreur d'arguments : {0}".format(err))
        sys.exit(1)
    except Exception as err:
        printerr("Erreur inconnue : {0}".format(err))
        sys.exit(1)
    
    sys.exit(0)