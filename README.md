
<p align="center">
  <img src="https://files.catbox.moe/vl8i5u.png" width="200" alt="Kyotaka Logo" />
</p>

<h1 align="center">🤖 KYOTAKA MD – BOT WHATSAPP</h1>

<p align="center">
  Un bot WhatsApp multi-sessions, rapide, sombre et puissant.
</p>

<p align="center">
  <a href="https://kyotaka-session-id.onrender.com/">
    <img src="https://img.shields.io/badge/🎯%20Obtenir%20Session%20ID-black?style=for-the-badge&logo=whatsapp" />
  </a>
</p>

---

## 🧠 Fonctionnalités

- 📱 **Multi-Sessions** – Gérez plusieurs comptes WhatsApp.  
- 🌐 **Réponses Multilingues** – Configurez `BOT_LANG` selon vos préférences.  
- ⚙️ **Automatisation Avancée** – Exécutez des actions sans intervention.  
- ⚡ **Déploiement Simplifié** – Compatible VPS, Ubuntu, Termux.

---

## 🌍 Langues Disponibles

Définissez la langue dans le fichier `config.env` :

```env
BOT_LANG=fr
```

| Code | Langue   | Code | Langue   |
|------|----------|------|----------|
| en   | Anglais  | fr   | Français |
| es   | Espagnol | ur   | Ourdou   |
| hi   | Hindi    | ru   | Russe    |
| bn   | Bengali  | ar   | Arabe    |
| id   | Indonésien | tr | Turc     |

---

## ⚡ Installation Rapide (VPS / Ubuntu)

```bash
bash <(curl -fsSL http://bit.ly/43JqREw)
```

---

## 🧾 Installation Manuelle (Ubuntu)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git ffmpeg curl -y

curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs -y

sudo npm install -g yarn
yarn global add pm2

git clone https://github.com/lyfe00011/levanter kyotaka-md
cd kyotaka-md
yarn install
```

### 🔧 Fichier `config.env`

```env
SESSION_ID=🔑 à générer ici : https://kyotaka-session-id.onrender.com/
PREFIX=.
STICKER_PACKNAME=Kyotaka
ALWAYS_ONLINE=false
BOT_LANG=fr
WARN_LIMIT=3
FORCE_LOGOUT=false
TZ=Africa/Kinshasa
```

---

## ▶️ Lancer / Stopper le Bot

```bash
pm2 start . --name kyotaka-md --attach --time
# Pour arrêter :
pm2 stop kyotaka-md
```

---

## 🔁 GitHub Actions – Workflows CI/CD

Crée un fichier `.github/workflows/nodejs.yml` avec ce contenu :

```yaml
name: Node.js CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  schedule:
    - cron: '0 */6 * * *'  # toutes les 6 heures

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [20.x]

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install

      - name: Install FFmpeg
        run: sudo apt-get install -y ffmpeg

      - name: Start application with timeout
        run: |
          timeout 21590s npm start  # Limite à 5h 59min 50s

      - name: Save state (Optionnel)
        run: |
          ./save_state.sh
```

---

## 📢 Chaîne Officielle WhatsApp

> 🔔 Reste informé des MAJ, tutos & news via la chaîne :

[👉 Rejoindre la chaîne Kyotaka MD](https://whatsapp.com/channel/0029VasZ6FaHLHQbLdUKfh33)

---

> 🧊 *KYOTAKA MD* – Développé pour dominer WhatsApp dans l’ombre...
