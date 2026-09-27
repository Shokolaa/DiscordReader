# DiscordReader 💬

Une application locale développée en Python avec **Flask** permettant d'explorer, lire et rechercher facilement dans les archives de messages exportées depuis Discord.

---

## 🚀 Fonctionnalités

- **Exploration fluide** : Accédez facilement à vos conversations et canaux archivés.
- **Moteur de recherche** : Recherche rapide par mots-clés dans les messages archivés (`search.py`).
- **Interface web locale** : Rendu clair et lisible servi via Flask et des templates HTML.
- **Confidentialité totale** : Traitement 100 % local, aucune donnée personnelle n'est envoyée sur un serveur distant.

---

## 📁 Structure du projet

```text
DiscordReader/
├── .venv/             # Environnement virtuel Python (ignoré par Git)
├── messages/          # Dossier contenant vos archives de messages (ignoré par Git)
├── templates/         # Templates HTML Flask (index.html, ...)
├── .gitignore         # Règles d'exclusion Git
├── app.py             # Point d'entrée de l'application Flask
├── search.py          # Logique de parsing et de recherche
└── README.md          # Documentation du projet
```

---

## 🛠️ Prérequis

- **Python** (version 3.10 ou supérieure recommandée)
- Vos données d'export Discord (dossier de messages décompressé)

---

## ⚙️ Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/Shokolaa/DiscordReader.git
   cd DiscordReader
   ```

2. **Créer et activer l'environnement virtuel :**
   ```powershell
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   ```bash
   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Installer les dépendances nécessaires :**
   ```bash
   pip install flask
   ```

---

## 📥 Préparation des données

1. Décompressez l'archive de vos données Discord.
2. Copiez les dossiers de conversations et fichiers JSON directement dans le dossier `messages/` à la racine du projet.

> 🔒 **Confidentialité :** Le dossier `messages/` est configuré dans le `.gitignore` afin d'éviter tout envoi accidentel de données privées sur GitHub.

---

## ▶️ Lancement

1. Démarrez l'application Flask :
   ```bash
   python app.py
   ```
2. Ouvrez votre navigateur web à l'adresse suivante :
   ```text
   http://127.0.0.1:5000/
   ```

---

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier.