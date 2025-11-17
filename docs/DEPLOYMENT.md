# GitHub Pages Deployment Guide

## Initial Setup

### 1. Update Configuration

Edit `docs/index.html` and update the GitHub repository information:

```javascript
// Find this section near line 495
const GITHUB_USER = 'kody-w';
const REPO_NAME = 'Nov17';
```

This is already configured correctly for your repository.

### 2. Enable GitHub Pages

1. Go to your GitHub repository
2. Click **Settings** → **Pages** (in the left sidebar)
3. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: Select `main` and `/docs` folder
   - Click **Save**

### 3. Wait for Deployment

GitHub will build and deploy your site. This usually takes 1-2 minutes.

Your site will be available at: `https://kody-w.github.io/Nov17/`

## Adding New Experiments

The portfolio automatically discovers and displays experiments from your repository!

When you complete a new experiment:

1. **Name it with the date format**: `YYYY-MM-DD_experiment_name.py`

2. **Add a description** at the top of the file:
   ```python
   """
   Brief description of what this experiment does
   """
   ```
   or use a comment:
   ```python
   # Brief description of what this experiment does
   ```

3. **Commit and push**:
   ```bash
   git add experiments/2025-11-20_your_experiment.py
   git commit -m "Add experiment: Your Experiment Title"
   git push
   ```

The portfolio will automatically:
- Discover your new experiment
- Extract the description from your docstring/comment
- Auto-generate tags based on filename and content
- Display it on your site within 1-2 minutes

**No manual updates to HTML needed!**

## Customization

### Colors

To change the color scheme, edit the CSS variables in `docs/index.html`:

```css
:root {
    --primary-blue: #0078d4;
    --teal-accent: #40e0d0;
    --dark-blue: #005a9e;
    /* ... other colors ... */
}
```

### Header Links

Update the header links to point to your blog, GitHub, or other sites:

```html
<div class="header-links">
    <a href="https://kodyw.com" class="header-link" target="_blank">Blog</a>
    <a href="https://github.com/kody-w" class="header-link" target="_blank">GitHub</a>
    <a href="#" class="header-link" id="repo-link">View Repository</a>
</div>
```

### About Section

Edit the About section content directly in the HTML to describe your specific focus areas and goals.

## Linking from Your Blog

Once deployed, you can link to your portfolio from kodyw.com:

```markdown
Check out my [code experiments portfolio](https://kody-w.github.io/Nov17/)
```

Or add a menu item, footer link, etc.

## Troubleshooting

### Site Not Loading

1. Check GitHub Pages settings - ensure it's set to deploy from `main` branch and `/docs` folder
2. Verify the site URL in Settings → Pages
3. Check the Actions tab for any build errors
4. Ensure `index.html` is in the `docs/` folder

### Links Not Working

1. Verify `GITHUB_USER` and `REPO_NAME` are set correctly in `docs/index.html`
2. Ensure experiment file names match exactly (case-sensitive)
3. Check that files exist in the `experiments/` folder

### Styling Issues

1. Clear browser cache (Cmd+Shift+R or Ctrl+Shift+R)
2. Check browser console for errors (F12 → Console)
3. Verify CSS is correctly formatted in the `<style>` section

## Maintenance

### Regular Updates

Every time you add a new experiment:
1. Update the `experiments` array in `docs/index.html`
2. Commit and push changes
3. GitHub Pages auto-deploys

### Analytics (Optional)

To add Google Analytics or similar:
1. Add tracking code before `</head>` in `docs/index.html`
2. Commit and push

### Custom Domain (Optional)

To use a custom subdomain like `experiments.kodyw.com`:
1. Add a `CNAME` file in `docs/` with your domain
2. Configure DNS at your domain registrar
3. Update GitHub Pages settings to use the custom domain

See: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site
