'''
Created on 2 déc. 2015

@author: takiguchi
'''
from pointentree.VariablesGlobales import pathSteamInstallerDir, cmdDownloadSteamTar, cmdUnarchiveSteamTar, \
                                    cmdRemoveSteamTar, cmdInstallSteam, pathDst, pathDstConfig, cmdStartDst, cmdStopDst, \
                                    cmdCdDstConfigPath, valDstConfDir, cmdTarSaveDst, cmdBz2SaveDst
from pointentree.DontStarveServer import log
from pointentree.Fonctions import screenEnFonctionnement, executerCommande
from pointentree.ExecutionCommandeException import ExecutionCommandeException
from gestionFichiers.GestionFichierException import GestionFichierException
from gestionFichiers.GestionFichiers import creerArborescence, creerDossier

class Serveur(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def start(self):
        '''
        Démarre le serveur
        '''
        log.info("Démarrage du serveur")
        
        try:
            executerCommande(cmdStartDst, "Le démarrage du serveur a échoué !")
            
            log.info("Serveur démarré")
            
        except ExecutionCommandeException as err:
            log.error(err)
    
    def stop(self):
        '''
        Arrête le serveur
        '''
        log.info("Arrêt du serveur")
        
        try:
            executerCommande(cmdStopDst, "L'arrêt du serveur a échoué !")
        
            log.info("Serveur arrêté")
            
        except ExecutionCommandeException as err:
            log.error(err)
    
    def restart(self):
        '''
        Redémarre le serveur
        '''
        log.info("Redémarrage du serveur")
        
        # Si le screen est lancé, on arrête le serveur
        self.stop() if screenEnFonctionnement else log.info("Le serveur n'était pas en fonctionnement")
        
        # On lance le serveur
        self.start()
    
    def save(self):
        '''
        Créer une sauvegarde archivée et compressée de la carte du serveur
        '''
        log.info("Sauvergarde du serveur")
        
        try:
            # On se déplace dans le répertoire 
            executerCommande(cmdCdDstConfigPath,
                             "Impossible de se déplacer dans le répertoire \"{0}\" !".format(valDstConfDir))
            
            # On créer une archive du dossier de la partie
            executerCommande(cmdTarSaveDst, "La création de l'archive a échoué !")
            
            log.info("Archive créée")
            
            # On compresse l'archive
            executerCommande(cmdBz2SaveDst, "La compression de l'archive a échoué !")
            
            log.info("Archive compressée")
            
            log.info("La sauvegarde du serveur a été créée avec succès")
            
        except ExecutionCommandeException as err:
            log.error(err)
    
    def install(self):
        # Création des différents dossiers
        try:
            # Création du dossier d'installation de steam
            creerArborescence(pathSteamInstallerDir)
            
            # On définit le dossier d'installation de steam comme le répertoire courrant
            executerCommande(pathSteamInstallerDir, "Impossible de se déplacer dans le répertoire d'installation de steam !")
            
            # On télécharge l'installateur de steam
            executerCommande(cmdDownloadSteamTar, "Le téléchargement de l'installeur de steam a échoué !")
            
            # On désarchive l'installeur de steam
            executerCommande(cmdUnarchiveSteamTar, "La décompression de l'archive a échoué !")
            
            # On supprimer l'arcihve
            executerCommande(cmdRemoveSteamTar, "La suppression de l'archive a échoué !")
            
            # On créer les répertoires de DST
            creerDossier(pathDst)
            creerDossier(pathDstConfig)
            
            # On exécute l'installation de steam et de DST
            executerCommande(cmdInstallSteam, "L'installation de steam a échoué !")
            
        except GestionFichierException as err:
            log.error(err)
            
        except ExecutionCommandeException as err:
            log.error(err)
        
        except Exception as err:
            log.error("Une erreur inconnue est survenue :\n{0}".format(err))