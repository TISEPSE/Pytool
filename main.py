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
print(GREEN + banner + RESET)

# Fonction pour installer un outil et afficher sa version
def install_tool(name, install_cmd, version_cmd=None, add_group_cmd=None):
    print(GREEN + f"========== Installation de {name} ==========" + RESET)
    subprocess.run(install_cmd, shell=True)
    if add_group_cmd:
        subprocess.run(add_group_cmd, shell=True)
    if version_cmd:
        print(GREEN + f"========== Version de {name} ==========" + RESET)
        subprocess.run(version_cmd, shell=True)

# Liste des outils à installer
tools = [
    ("Nmap", "sudo apt install -y nmap", "nmap --version"),
    ("Shodan", "sudo apt install -y python3-shodan", "shodan version"),
    ("Wireshark", "sudo apt install -y wireshark", "wireshark --version", "sudo usermod -aG wireshark $USER")
]

# Installation Linux (Debian / Ubuntu)
YesOrNot = input("Voulez-vous installer tous les outils disponibles ? (Y/n) : ") or "Y"

if YesOrNot.upper() == "Y":
    # Mise à jour du système et dépendances
    print(GREEN + "========== Mise à jour du système et installation de python3 ==========" + RESET)
    subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)
    subprocess.run("sudo apt install -y python3", shell=True)

    # Installer tous les outils de la liste
    for tool in tools:
        install_tool(*tool)

    print(GREEN + "============== Installation terminée ! ==============" + RESET)
