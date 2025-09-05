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

# Liste des outils à installer (corrigée)
tools = [
    ("Nmap", "sudo apt install -y nmap", "nmap --version"),
    ("Shodan", "sudo apt install -y python3-shodan", "shodan version || echo 'Shodan installé'"),
    ("Wireshark", "sudo apt install -y wireshark", "wireshark --version", "sudo usermod -aG wireshark $USER"),
    ("Metasploit", "sudo snap install metasploit-framework", "echo 'Metasploit installé'"),
    ("Beef", "sudo apt install -y git ruby ruby-dev build-essential && git clone https://github.com/beefproject/beef.git || true && cd beef && sudo gem install bundler && sudo bundle install", "echo 'BeEF installé'"),
    ("Postman", "sudo snap install postman", "snap list postman"),
    ("Hashcat", "sudo apt install -y hashcat", "hashcat --version"),
    ("Hydra", "sudo apt install -y hydra", "hydra -h | head -1"),
    ("SqlMap", "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev && sudo ln -sf $(pwd)/sqlmap-dev/sqlmap.py /usr/local/bin/sqlmap", "sqlmap --version"),
    ("Wifite", "sudo apt install -y wifite", "wifite --version 2>/dev/null || echo 'Wifite installé - utilisez: sudo wifite'"),
    ("Burpsuite", "cd /tmp && wget -q https://portswigger.net/burp/releases/download?product=community\\&version=2023.12.1\\&type=Linux -O burpsuite_community.sh && chmod +x burpsuite_community.sh && sudo ./burpsuite_community.sh -q && sudo ln -sf /opt/BurpSuiteCommunity/BurpSuiteCommunity /usr/local/bin/burpsuite", "burpsuite --version 2>/dev/null || echo 'Burp Suite Community Edition installé'"),
]

# Installation Linux (Debian / Ubuntu)
YesOrNot = input("Voulez-vous installer tous les outils disponibles ? (Y/n) : ") or "Y"

if YesOrNot.upper() == "Y":
    # Mise à jour du système et dépendances
    print(GREEN + "========== Mise à jour du système et installation des dépendances ==========" + RESET)
    subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)
    subprocess.run("sudo apt install -y python3", shell=True)
    subprocess.run("sudo apt install -y curl", shell=True)
    subprocess.run("sudo apt install -y git ruby ruby-dev build-essential", shell=True)
    subprocess.run("sudo apt install default-jre -y", shell=True)
    
    # Installer tous les outils de la liste
    for tool in tools:
        install_tool(*tool)
    
    print(GREEN + "============== Installation terminée ! ==============" + RESET)