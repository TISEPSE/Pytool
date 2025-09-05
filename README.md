# 🛠️ PyTool - Installateur d'Outils de Sécurité

Un script Python simple et automatisé pour installer rapidement les outils de sécurité les plus populaires sur les systèmes Debian/Ubuntu.

## 📋 Outils Inclus

| Outil | Description |
|-------|-------------|
| **Nmap** | Scanner de ports et découverte réseau |
| **Shodan** | Moteur de recherche pour devices connectés |
| **Wireshark** | Analyseur de protocoles réseau |
| **Metasploit** | Framework de test de pénétration |
| **BeEF** | Framework d'exploitation de navigateurs |
| **Postman** | Client API pour tests |
| **Hashcat** | Outil de récupération de mots de passe |
| **Hydra** | Attaque par force brute |
| **SqlMap** | Outil d'injection SQL automatisé |
| **Wifite** | Audit de sécurité WiFi |
| **Burp Suite** | Proxy d'interception web |

## 🚀 Installation Rapide

```bash
# Cloner le projet
git clone <url-du-repo>
cd Pytool

# Lancer le script
python3 main.py
```

## 📖 Utilisation

1. **Exécuter le script** :
   ```bash
   python3 main.py
   ```

2. **Choisir l'installation** :
   - Appuyez sur `Y` ou `Entrée` pour installer tous les outils
   - Appuyez sur `n` pour annuler

3. **Attendre la fin** :
   - Le script met à jour le système
   - Installe les dépendances nécessaires
   - Installe chaque outil avec vérification de version

## ⚠️ Prérequis

- **Système** : Ubuntu/Debian (testé sur Ubuntu 20.04+)
- **Permissions** : Accès sudo requis
- **Python** : Python 3.x installé
- **Internet** : Connexion stable pour les téléchargements

## 🔧 Fonctionnalités

- ✅ Installation automatisée de 11 outils de sécurité
- ✅ Mise à jour automatique du système
- ✅ Vérification des versions après installation
- ✅ Gestion des groupes utilisateurs (ex: wireshark)
- ✅ Interface colorée et conviviale
- ✅ Gestion d'erreurs basique

## 📝 Notes Importantes

- **Temps d'installation** : 15-30 minutes selon la connexion
- **Espace disque** : ~2-3 GB requis
- **Burp Suite** : Version Community Edition (gratuite)
- **Wifite** : Nécessite `sudo` pour l'utilisation
- **BeEF** : Installation via Git + Ruby gems

## 🐛 Résolution de Problèmes

### Erreur de permissions
```bash
sudo chmod +x main.py
```

### Erreur snap (Metasploit/Postman)
```bash
sudo apt install snapd
sudo systemctl enable --now snapd
```

### Erreur Ruby (BeEF)
```bash
sudo apt install ruby-full ruby-bundler
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouveaux outils
- Améliorer le script

## ⚖️ Licence

Ce projet est destiné à des fins éducatives et de test de sécurité légitimes uniquement.

---
*Développé avec ❤️ pour la communauté cybersécurité*