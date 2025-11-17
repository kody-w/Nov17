#!/usr/bin/env python3
"""
GitHub Template Setup Script
Configures the repository after creating it from the template
"""

import re
import subprocess
from pathlib import Path


def get_git_info():
    """Try to get current repo info from git remote"""
    try:
        remote_url = subprocess.check_output(
            ['git', 'config', '--get', 'remote.origin.url'],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        # Extract username and repo name
        # Handles both HTTPS and SSH URLs
        if 'github.com' in remote_url:
            parts = remote_url.replace('.git', '').split('/')
            repo_name = parts[-1]
            username = parts[-2].split(':')[-1]  # Handle SSH format
            return username, repo_name
    except:
        pass
    return None, None


def update_file(filepath, replacements):
    """Update a file with multiple replacements"""
    content = filepath.read_text()
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
    filepath.write_text(content)


def main():
    print("=" * 60)
    print("  GitHub Template Repository Setup")
    print("=" * 60)
    print()

    # Try to get info from git
    current_user, current_repo = get_git_info()

    # Get GitHub username
    if current_user:
        username = input(f"Enter your GitHub username [{current_user}]: ").strip() or current_user
    else:
        username = input("Enter your GitHub username: ").strip()

    # Get repository name
    if current_repo:
        repo_name = input(f"Enter your repository name [{current_repo}]: ").strip() or current_repo
    else:
        repo_name = input("Enter your repository name: ").strip()

    # Confirm
    print()
    print("Configuration:")
    print(f"  GitHub User: {username}")
    print(f"  Repository:  {repo_name}")
    print()

    confirm = input("Is this correct? (y/n) ").strip().lower()
    if confirm != 'y':
        print("Setup cancelled.")
        return

    print()
    print("Configuring repository...")

    # Define file updates
    files_to_update = {
        'docs/index.html': {
            r"const GITHUB_USER = '[^']*';": f"const GITHUB_USER = '{username}';",
            r"const REPO_NAME = '[^']*';": f"const REPO_NAME = '{repo_name}';",
        },
        'README.md': {
            r'https://kody-w\.github\.io/Nov17/': f'https://{username}.github.io/{repo_name}/',
        },
        'docs/README.md': {
            r'https://kody-w\.github\.io/Nov17/': f'https://{username}.github.io/{repo_name}/',
        },
        'docs/DEPLOYMENT.md': {
            r'https://kody-w\.github\.io/Nov17/': f'https://{username}.github.io/{repo_name}/',
            r"const GITHUB_USER = '[^']*';": f"const GITHUB_USER = '{username}';",
            r"const REPO_NAME = '[^']*';": f"const REPO_NAME = '{repo_name}';",
        },
    }

    # Update files
    base_path = Path(__file__).parent
    for filepath, replacements in files_to_update.items():
        full_path = base_path / filepath
        if full_path.exists():
            print(f"  → Updating {filepath}")
            update_file(full_path, replacements)
        else:
            print(f"  ⚠ Skipping {filepath} (not found)")

    print()
    print("✅ Configuration complete!")
    print()
    print("Next steps:")
    print("  1. Commit changes: git add . && git commit -m 'Configure repository'")
    print("  2. Push to GitHub: git push")
    print("  3. Enable GitHub Pages:")
    print(f"     - Go to https://github.com/{username}/{repo_name}/settings/pages")
    print("     - Source: Deploy from branch 'main' and '/docs' folder")
    print("     - Save")
    print()
    print("Your portfolio will be live at:")
    print(f"  https://{username}.github.io/{repo_name}/")
    print()
    print("=" * 60)


if __name__ == '__main__':
    main()
