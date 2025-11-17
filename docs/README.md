# GitHub Pages Portfolio

This folder contains the GitHub Pages site for showcasing experiments from this workspace.

## Quick Start

1. **Update Configuration**
   - Edit `index.html` (lines 400-402)
   - Set `GITHUB_USER` and `REPO_NAME` to match your repository

2. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` and `/docs` folder
   - Save

3. **Access Your Site**
   - URL: `https://kody-w.github.io/Nov17/`
   - Usually deploys in 1-2 minutes

## Adding Experiments

When you create a new experiment in `experiments/`:

1. Open `index.html`
2. Find the `experiments` array (around line 415)
3. Add your experiment:

```javascript
{
    title: "Your Experiment Title",
    date: "2025-11-20",
    description: "Brief description",
    tags: ["Tag1", "Tag2"],
    file: "2025-11-20_your_experiment.py"
}
```

4. Commit and push - GitHub Pages auto-deploys

## Files

- `index.html` - Main portfolio page (single-file site)
- `DEPLOYMENT.md` - Detailed deployment and customization guide
- `README.md` - This file

## Customization

See [DEPLOYMENT.md](DEPLOYMENT.md) for details on:
- Changing colors and styling
- Adding analytics
- Using custom domains
- Troubleshooting

## Linking from Your Blog

Once deployed, link from kodyw.com:

```markdown
Check out my [code experiments](https://kody-w.github.io/Nov17/)
```

Or add to your blog's navigation menu.
