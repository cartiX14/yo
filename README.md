# ⚙️ Mon Portfolio Technique – ["Osama"]

Bienvenue sur mon portfolio technique. Ici, tu trouveras :
- Des projets en Python, SQL, JavaScript, HTML/CSS
- Des scripts pour l’administration système
- Des commandes utiles pour Arch Linux
- Et bien plus...

---

## 🚀 À propos de moi

Je suis passionné par l’informatique d’exploitation, le développement web, l’automatisation et les systèmes GNU/Linux.  
Mon objectif : concevoir des outils simples, efficaces et réutilisables pour automatiser, sécuriser et surveiller les systèmes.

---

## 🧠 Compétences Techniques

- 🐧 **Linux** : Arch, Debian, Systemd, Bash, kitty
- 🐍 **Python** : Scripts, automatisation, parsing, API
- 🧮 **SQL** : MySQL, PostgreSQL, requêtes avancées
- 🌐 **Web** : HTML, CSS , JavaScrip
- ⚙️ **DevOps** : Git

---

## 📂 Projets et Scripts

### 🔧 Outils Linux / Scripts

| Projet | Description | Technologies |
|--------|-------------|--------------|
| [📦 auto-backup.sh](./scripts/auto-backup.sh) | Script de sauvegarde automatique avec `rsync` | Bash |
| [🔥 service-monitor.py](./scripts/service-monitor.py) | Vérifie si un service tourne, sinon redémarre | Python + systemctl |
| [📡 arch-setup.md](./docs/arch-setup.md) | Guide d’installation et de post-install Arch Linux | Markdown |

---


## 🐧 Commandes utiles Arch Linux

```bash
# Installer un paquet
sudo pacman -S <package>

# Mettre à jour tout le système
sudo pacman -Syu

# Rechercher un paquet
pacman -Ss <mot-clé>

# Voir l’état d’un service
systemctl status sshd

# Voir les logs récents
journalctl -xe
