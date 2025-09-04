import subprocess

# Couleurs
GREEN = "\033[32m"
RESET = "\033[0m"

# Bannière ASCII
banner = """
 _______  __   __  _______  _______  _______  ___     
|       ||  | |  ||       ||       ||       ||   |    
|    _  ||  |_|  ||_     _||   _   ||   _   ||   |    
|   |_| ||       |  |   |  |  | |  ||  | |  ||   |    
|    ___||_     _|  |   |  |  |_|  ||  |_|  ||   |___ 
|   |      |   |    |   |  |       ||       ||       |
|___|      |___|    |___|  |_______||_______||_______|
"""
print(banner)

# Installation Linux (Debian / Ubuntu)
# Si c'est vide on met "Y" par défaut
YesOrNot = input("Voulez-vous installer tous les outils disponibles ? (Y/n) : ") or "Y"

# Si la condition est "Y" ou "y" (on le met en majuscule avec .upper()) on exécute le script
if YesOrNot.upper() == "Y":
    # Mise à jour du système et instalation des dépendences
    print(GREEN + "========== Mise à jour du système et installation des dépendences ==========" + RESET)
    subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)
    subprocess.run("sudo apt install -y python3", shell=True)    

    # Installation des outils
    print(GREEN + "========== Installation de Nmap ==========" + RESET)
    subprocess.run("sudo apt install -y nmap", shell=True)

    # Affichage de la version de nmap
    print(GREEN + "========== Version de nmap : ==========" + RESET)
    subprocess.run("nmap --version", shell=True)
    
    #Instalation de shodan
    print(GREEN + "========== Installation de Shodan ==========" + RESET)
    subprocess.run("sudo apt install -y python3-shodan", shell=True)

    # Affichage de la version de Shodan
    print(GREEN + "========== Version de Shodan : ==========" + RESET)
    subprocess.run("shodan version", shell=True)

    #Instalation de Wireshark
    print(GREEN + "========== Installation de WireShark ==========" + RESET)
    subprocess.run("sudo apt install -y wireshark", shell=True)
    subprocess.run("sudo usermod -aG wireshark $USER", shell=True)

    #Version de WireShark
    print(GREEN + "========== Version de WireShark ==========" + RESET)
    subprocess.run("wireshark --version", shell=True)

    # Fin de l'installation
    print(GREEN + "========== Installation terminée ! ==========" + RESET)
