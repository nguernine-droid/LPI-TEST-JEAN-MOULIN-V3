# Déploiement — portail LPI

Ce fichier explique comment préparer le dépôt Git local et importer le projet sur Vercel (méthode web import).

Prérequis
- Avoir un compte GitHub.
- Avoir un compte Vercel (ou s'inscrire sur https://vercel.com).

Étapes rapides (exécutez ces commandes dans un terminal) :

```bash
cd "/Users/nordine/Desktop/DEPLOYEMENT PORTAIL"
# Initialiser le dépôt local
git init
# Créer .gitignore si nécessaire (contient node_modules, .DS_Store, etc.)
# Ajouter les fichiers et valider
git add .
git commit -m "Initial commit — portail LPI"
```

Créer le repo GitHub
- Ouvrez https://github.com/new
- Donnez un nom (par ex. `portail-lpi`) et créez le repo (public ou privé selon votre choix).

Connecter le dépôt local au remote (remplacez USERNAME/REPO) :

```bash
git remote add origin git@github.com:USERNAME/REPO.git
git branch -M main
git push -u origin main
```

Importer sur Vercel (web)
1. Allez sur https://vercel.com
2. Cliquez sur "New Project" → "Import Git Repository" → sélectionnez le repo GitHub que vous venez de pousser.
3. Pour la plupart des sites statiques, laissez les réglages par défaut ; si besoin, définissez le `Root Directory` sur `/` et `Framework Preset` sur "Other".
4. Cliquez sur "Deploy".

Importer sur Vercel via CLI (optionnel — nécessite Node/npm)
```bash
npm i -g vercel
cd "/Users/nordine/Desktop/DEPLOYEMENT PORTAIL"
vercel login
vercel --prod
```

Notes et bonnes pratiques
- Assurez-vous que `index.html` est présent à la racine du dossier (déjà copié ici).
- Si vous avez des assets externes, vérifiez qu'ils sont référencés par chemin relatif ou via CDN.
- Configurez un `README.md` et une licence si vous comptez partager le repo.

Si vous voulez, je peux :
- Initialiser git localement et faire le premier commit pour vous.
- Générer une commande `gh` (GitHub CLI) ou `curl` pour créer le repo automatiquement (nécessite token).
