# Using This Template

This is a GitHub template repository for a code experimentation workspace with a built-in portfolio site.

## Quick Start (After Creating from Template)

### Option 1: Automated Setup (Recommended)

**Using Python (works on all platforms):**
```bash
python3 setup.py
```

**Using Bash (Mac/Linux):**
```bash
./setup.sh
```

The script will:
- Detect your repository name from git
- Prompt for your GitHub username
- Update all configuration files automatically
- Show you the next steps

### Option 2: Manual Setup

If you prefer to configure manually:

1. **Update `docs/index.html`** (around line 495-497):
   ```javascript
   const GITHUB_USER = 'your-username';
   const REPO_NAME = 'your-repo-name';
   ```

2. **Update `README.md`**:
   - Replace all instances of `https://kody-w.github.io/Nov17/` with your URL

3. **Update `docs/README.md`**:
   - Replace all instances of `https://kody-w.github.io/Nov17/` with your URL

4. **Update `docs/DEPLOYMENT.md`**:
   - Replace all instances of `https://kody-w.github.io/Nov17/` with your URL
   - Update the GitHub username and repo name examples

## Enable GitHub Pages

After configuration:

1. Go to your repository **Settings** → **Pages**
2. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
3. Click **Save**

Your site will be live at: `https://YOUR_USERNAME.github.io/YOUR_REPO/`

## What You Get

### Directory Structure
```
.
├── experiments/     # Completed experiments with documentation
├── sandbox/         # Temporary testing area (git-ignored)
├── utils/           # Reusable utilities (timer, logger, quick_test)
├── templates/       # Quick-start templates for common tasks
├── docs/            # GitHub Pages portfolio site
└── .github/         # Workspace configuration
```

### Utilities Included
- **Timer** - Benchmark code performance (`utils/timer.py`)
- **Logger** - Simple logging setup (`utils/logger.py`)
- **Quick Test** - Basic test template (`utils/quick_test.py`)

### Templates Included
- **Data Analysis** - Data science starting point
- **API Client** - API testing template
- **Algorithm Test** - Algorithm comparison template

### Portfolio Features
- Professional design with responsive layout
- Showcases your experiments online
- Links directly to code on GitHub
- Easy to update - just edit the experiments array

## Using the Workspace

### 1. Create an Experiment

Work in the `sandbox/` directory first:
```bash
cd sandbox
# Create and test your code
python my_experiment.py
```

### 2. Use Utilities

```python
from utils.timer import timer, Timer

@timer
def my_function():
    # your code here
    pass

# Or use context manager
with Timer("My operation"):
    # your code here
    pass
```

### 3. Move to Portfolio

When your experiment is complete:
```bash
mv sandbox/my_experiment.py experiments/2025-11-20_my_experiment.py
```

### 4. Update Portfolio Site

Edit `docs/index.html` and add to the `experiments` array (around line 420):
```javascript
{
    title: "Your Experiment Title",
    date: "2025-11-20",
    description: "Brief description of what this does",
    tags: ["Tag1", "Tag2", "Tag3"],
    file: "2025-11-20_your_experiment.py"
}
```

Commit and push - GitHub Pages auto-deploys!

## File Naming Convention

Use date-prefixed names for experiments:
- Format: `YYYY-MM-DD_experiment_name.py`
- Example: `2025-11-20_api_performance_test.py`

This keeps experiments organized chronologically.

## Customization

### Change Colors

Edit CSS variables in `docs/index.html`:
```css
:root {
    --primary-blue: #0078d4;
    --teal-accent: #40e0d0;
    /* ... customize other colors ... */
}
```

### Update About Section

Edit the About section content in `docs/index.html` to describe your focus areas.

### Add Custom Utilities

1. Create new utility in `utils/`
2. Add documentation to `README.md`
3. Update the Utilities section in `docs/index.html`

## Tips for Success

- Keep `sandbox/` for messy exploration
- Move polished code to `experiments/`
- Use type hints and docstrings
- Document dependencies in code comments
- Commit experiments regularly
- Update portfolio as you go

## Getting Help

- See [README.md](README.md) for full workspace documentation
- See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for portfolio customization
- See [GETTING_STARTED.md](GETTING_STARTED.md) for detailed workflows

## Cleanup

After setup, you can optionally:
- Delete or keep `setup.py` and `setup.sh`
- Delete this `TEMPLATE_USAGE.md` file
- Customize the README to your specific needs

---

**Happy experimenting!** 🚀
