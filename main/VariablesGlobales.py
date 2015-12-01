'''
Created on 1 déc. 2015

@author: takiguchi
'''
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     Variables
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
''' Liste des opérations que peut exécuter le serveur DST '''
listeOperations = ["start", "stop", "restart", "install", "update", "save"]

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
pathDstConfig = "/home/steam/.klei/" + valDstConfDir

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     Commandes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
''' Définit le répertoire contenant l'exécutable du serveur DST comme répertoire courrant '''
cmdCdDstPath = "cd " + pathDstBin

''' Démarre le serveur DST dans un nouveau screen '''
cmdStartDst = cmdCdDstPath + " ; screen -dmS " + valDstScreen + \
                " ./dontstarve_dedicated_server_nullrenderer -port 10999 -conf_dir " + valDstConfDir
                
''' Arrête le screen dans lequel fonctionne le serveur DST '''
cmdStopDst = cmdCdDstPath + " ; screeb -dr " + valDstScreen + " -X -S quit"

''' Télécharge et décompresse l'archive d'installation de steam dans le répertoire courrant, avant de la supprimer '''
cmdDownloadSteamTar = "wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz"
              
''' Décompresse l'archive d'installation de Steam dans le répertoire courrant '''      
cmdUnarchiveSteamTar = "tar -xvzf steamcmd_linux.tar.gz"

''' Supprime l'archive contenant l'installation de Steam '''
cmdRemoveSteamTar = "rm steamcmd_linux.tar.gz"

''' Exécute le script d'installation de steam '''
cmdInstallSteam = "STEAMEXE=steamcmd ./steam.sh +login anonymous +force_install_dir " + pathDst + " +app_update " + \
                    "343050 validate +quit"

