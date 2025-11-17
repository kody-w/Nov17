#!/bin/bash

# GitHub Template Setup Script
# This script configures the repository after creating it from the template

set -e

echo "================================================"
echo "  GitHub Template Repository Setup"
echo "================================================"
echo ""

# Get current repository name from git remote (if available)
CURRENT_REPO=$(git config --get remote.origin.url 2>/dev/null | sed -n 's#.*/\([^.]*\)\.git#\1#p')
CURRENT_USER=$(git config --get remote.origin.url 2>/dev/null | sed -n 's#.*/\([^/]*\)/.*#\1#p' | sed 's/.*://')

# Prompt for GitHub username
if [ -z "$CURRENT_USER" ]; then
    read -p "Enter your GitHub username: " GITHUB_USER
else
    read -p "Enter your GitHub username [$CURRENT_USER]: " GITHUB_USER
    GITHUB_USER=${GITHUB_USER:-$CURRENT_USER}
fi

# Prompt for repository name
if [ -z "$CURRENT_REPO" ]; then
    read -p "Enter your repository name: " REPO_NAME
else
    read -p "Enter your repository name [$CURRENT_REPO]: " REPO_NAME
    REPO_NAME=${REPO_NAME:-$CURRENT_REPO}
fi

echo ""
echo "Configuration:"
echo "  GitHub User: $GITHUB_USER"
echo "  Repository:  $REPO_NAME"
echo ""
read -p "Is this correct? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Setup cancelled."
    exit 1
fi

echo ""
echo "Configuring repository..."

# Update docs/index.html
echo "  → Updating docs/index.html"
sed -i.bak "s/const GITHUB_USER = '.*';/const GITHUB_USER = '$GITHUB_USER';/" docs/index.html
sed -i.bak "s/const REPO_NAME = '.*';/const REPO_NAME = '$REPO_NAME';/" docs/index.html
rm docs/index.html.bak

# Update README.md
echo "  → Updating README.md"
sed -i.bak "s|https://kody-w.github.io/Nov17/|https://$GITHUB_USER.github.io/$REPO_NAME/|g" README.md
rm README.md.bak

# Update docs/README.md
echo "  → Updating docs/README.md"
sed -i.bak "s|https://kody-w.github.io/Nov17/|https://$GITHUB_USER.github.io/$REPO_NAME/|g" docs/README.md
rm docs/README.md.bak

# Update docs/DEPLOYMENT.md
echo "  → Updating docs/DEPLOYMENT.md"
sed -i.bak "s|https://kody-w.github.io/Nov17/|https://$GITHUB_USER.github.io/$REPO_NAME/|g" docs/DEPLOYMENT.md
sed -i.bak "s/const GITHUB_USER = '.*';/const GITHUB_USER = '$GITHUB_USER';/" docs/DEPLOYMENT.md
sed -i.bak "s/const REPO_NAME = '.*';/const REPO_NAME = '$REPO_NAME';/" docs/DEPLOYMENT.md
rm docs/DEPLOYMENT.md.bak

echo ""
echo "✅ Configuration complete!"
echo ""
echo "Next steps:"
echo "  1. Commit changes: git add . && git commit -m 'Configure repository'"
echo "  2. Push to GitHub: git push"
echo "  3. Enable GitHub Pages:"
echo "     - Go to https://github.com/$GITHUB_USER/$REPO_NAME/settings/pages"
echo "     - Source: Deploy from branch 'main' and '/docs' folder"
echo "     - Save"
echo ""
echo "Your portfolio will be live at:"
echo "  https://$GITHUB_USER.github.io/$REPO_NAME/"
echo ""
echo "================================================"
