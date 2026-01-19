#!/usr/bin/env bash
set -euo pipefail

# Script d'assistance — initialise git, ajoute, commit.
# Ne pousse PAS automatiquement le remote — remplacez USERNAME/REPO vous-même.

ROOT_DIR="/Users/nordine/Desktop/DEPLOYEMENT PORTAIL"
cd "$ROOT_DIR"

if ! command -v git >/dev/null 2>&1; then
  echo "git n'est pas installé ou n'est pas dans le PATH. Installez git et réessayez."
  exit 1
fi

if [ ! -f .gitignore ]; then
  cat > .gitignore <<'EOF'
node_modules/
.DS_Store
.env
dist/
.vscode/
npm-debug.log
coverage/
.idea/
*.log
EOF
  echo ".gitignore créé"
fi

if [ -d .git ] ; then
  echo "Un dépôt git existe déjà — ajout des fichiers et commit"
else
  git init
  echo "Dépôt git initialisé"
fi

git add .

if git diff --cached --quiet; then
  echo "Aucun changement à committer."
else
  git commit -m "Initial commit — portail LPI" || true
  echo "Commit créé"
fi

cat <<'INSTR'
Pour pousser sur GitHub :
1) Créez un repo sur GitHub (ex : portail-lpi)
2) Remplacez USERNAME/REPO dans la commande ci-dessous puis exécutez-la :

   git remote add origin git@github.com:USERNAME/REPO.git
   git branch -M main
   git push -u origin main

Ensuite importez le repo sur Vercel via vercel.com → New Project → Import Git Repository.
INSTR

exit 0
