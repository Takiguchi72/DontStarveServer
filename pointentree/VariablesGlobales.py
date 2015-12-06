'''
Created on 1 déc. 2015

@author: takiguchi
'''
from time import time
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     Variables
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
''' Liste des opérations que peut exécuter le serveur DST '''
listeOperations = ["start", "stop", "restart", "install", "update", "save"]

''' Format de date pour le nom du fichier de log qui sera créé '''
logFormatDate = '%d-%m-%y_%H-%M'

''' Date au format définit précédamment afin de créer le fichier de logs '''
dateExecution = str(time.strftime(logFormatDate, time.localtime()))

''' Le nom du screen qui sera lancé pour démarrer le serveur DontStarveTogether '''
valDstScreen = "DontStarveServer"

''' Le chemin du dossier contenant la configration et la partie du serveur, seulement 
    à partir du chemin "/home/steam/.klei" '''
valDstConfDir = "configs/server"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     Chemins
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
''' Le chemin du dossier contenant les fichiers du serveur DST '''
pathDst = "/home/steam/steamapps/DST"

''' Le chemin du dossier contenant l'exécutable permettant de démarrer le serveur DST '''
pathDstBin = pathDst + "/bin"

''' Le chemin du dossier contenant la configuration et la partie du serveur '''
pathDstConfig = "/home/steam/.klei/{0}".format(valDstConfDir)

''' Le chemin du dossier contenant l'installateur de steam '''
pathSteamInstallerDir = "/home/steam/steaminstaller/"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     Commandes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
''' Définit le répertoire contenant l'exécutable du serveur DST comme répertoire courrant '''
cmdCdDstPath = "cd {0}".format(pathDstBin)

''' Définit le répertoire contenant la configuration du serveur DST comme répertoire courrant '''
cmdCdDstConfigPath = "cd {0}".format(pathDstConfig)

''' Démarre le serveur DST dans un nouveau screen '''
cmdStartDst = "{0} ; screen -dmS {1} ./dontstarve_dedicated_server_nullrenderer -port 10999 -conf_dir {3}".format(
                        cmdCdDstPath, valDstScreen, valDstConfDir)
                
''' Arrête le screen dans lequel fonctionne le serveur DST '''
cmdStopDst = "{0} ; screen -dr {1} -X -S quit".format(cmdCdDstPath, valDstScreen)

''' Télécharge et décompresse l'archive d'installation de steam dans le répertoire courrant, avant de la supprimer '''
cmdDownloadSteamTar = "wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz"
              
''' Décompresse l'archive d'installation de Steam dans le répertoire courrant '''      
cmdUnarchiveSteamTar = "tar -xvzf steamcmd_linux.tar.gz"

''' Supprime l'archive contenant l'installation de Steam '''
cmdRemoveSteamTar = "rm steamcmd_linux.tar.gz"

''' Exécute le script d'installation de steam '''
cmdInstallSteam = "STEAMEXE=steamcmd ./steam.sh +login anonymous +force_install_dir " + pathDst + " +app_update " + \
                    "343050 validate +quit"

''' Créer une archive du dossier contenant la partie du serveur DST '''
cmdTarSaveDst = "tar -cvf " + pathDstConfig + "/sauvegardes/" + dateExecution +".tar save"

''' Compresse l'archive de sauvegarde '''
cmdBz2SaveDst = "bzip2 -vv {0}/sauvegardes/{1}".format(pathDstConfig, dateExecution + ".tar")