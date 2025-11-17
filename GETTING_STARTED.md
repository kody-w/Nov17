# Getting Started with This Workspace

## Initial Setup

### 1. Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit: Claude Code experimentation workspace"
```

### 2. Create GitHub Repository
1. Go to https://github.com/new
2. Name your repository (e.g., `claude-code-experiments`)
3. Keep it **public** to share with others
4. **Don't** initialize with README, .gitignore, or license (already included)
5. Click "Create repository"

### 3. Push to GitHub
```bash
# Replace YOUR_USERNAME and REPO_NAME with your values
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

## Using This Workspace with Claude Code

### Quick Start
1. Open this workspace in VS Code with Claude Code extension
2. Use `sandbox/` for quick experiments
3. Use templates from `templates/` as starting points
4. Move successful experiments to `experiments/` with dates

### Example Workflow

**Testing an idea:**
```bash
# 1. Create a test file in sandbox
cd sandbox
touch test_idea.py

# 2. Ask Claude Code to help implement
# "Help me implement a function to parse JSON data"

# 3. Test it
python test_idea.py

# 4. If successful, move to experiments with date
mv test_idea.py ../experiments/2025-11-17_json_parser.py
```

**Using a template:**
```bash
# Copy a template to sandbox
cp templates/data_analysis.py sandbox/my_analysis.py

# Ask Claude Code to customize it
# "Modify my_analysis.py to analyze CSV data about sales"
```

### Utility Usage Examples

**Timer for performance testing:**
```python
from utils.timer import timer, Timer

@timer
def my_function():
    # Your code here
    pass

# Or use context manager
with Timer("My operation"):
    # Your code here
    pass
```

**Logger for debugging:**
```python
from utils.logger import setup_logger

log = setup_logger("my_experiment")
log.info("Starting analysis")
log.debug("Debug details here")
```

## Best Practices with Claude Code

### 1. Clear Communication
- Be specific about what you want to test
- Reference files: "modify `sandbox/test.py` to..."
- Ask for explanations: "explain how this algorithm works"

### 2. Iterative Development
- Start simple in `sandbox/`
- Test frequently with `python your_file.py`
- Use utilities to benchmark and log
- Refine before moving to `experiments/`

### 3. File Organization
```
sandbox/           → Quick tests, temporary work
experiments/       → Documented, working code
templates/         → Reusable starting points
utils/            → Helper functions (rarely modified)
```

### 4. Naming Conventions
- **Experiments**: `YYYY-MM-DD_description.py`
  - `2025-11-17_api_performance_test.py`
  - `2025-11-17_sorting_algorithm_comparison.py`

- **Sandbox**: Anything goes, but descriptive names help
  - `test_api.py`
  - `quick_sort_test.py`

## Example Claude Code Prompts

### Starting an Experiment
```
"Create a script in sandbox/ that tests different sorting algorithms 
using the timer utility to compare performance"
```

### Using Templates
```
"Copy the algorithm_test.py template and modify it to compare 
three different approaches to finding prime numbers"
```

### Debugging
```
"Help me debug sandbox/my_test.py - it's throwing an IndexError"
```

### Code Review
```
"Review experiments/2025-11-17_data_parser.py and suggest improvements 
for performance and readability"
```

### Documentation
```
"Add docstrings and comments to sandbox/working_code.py, then move it 
to experiments/ with today's date"
```

## Git Workflow

### Daily Commits
```bash
# After successful experiments
git add experiments/2025-11-17_*.py
git commit -m "Add experiment: [description]"
git push
```

### Clean Sandbox (Optional)
```bash
# Sandbox is git-ignored, so you can clean anytime
rm -rf sandbox/*

# Or keep a backup first
tar -czf sandbox_backup_$(date +%Y%m%d).tar.gz sandbox/
rm -rf sandbox/*
```

### Update Documentation
```bash
# After adding new utilities or templates
git add utils/ templates/ README.md
git commit -m "Update utilities and documentation"
git push
```

## Sharing Your Work

### Make a Great README
Update `README.md` with:
- What you're experimenting with
- Interesting findings from experiments
- Custom utilities you've added
- Links to specific experiments

### Add Topics to GitHub
On your GitHub repo page, add topics:
- `python`
- `experimentation`
- `claude-code`
- `prototyping`
- Add domain-specific tags (e.g., `data-science`, `algorithms`)

### Share Experiments
Point people to specific experiments:
```
Check out my performance comparison:
github.com/YOUR_USERNAME/REPO_NAME/blob/main/experiments/2025-11-17_string_concat_perf.py
```

## Maintenance

### Weekly Cleanup
```bash
# Review sandbox contents
ls -la sandbox/

# Remove temporary files
rm sandbox/temp_*.py

# Commit any new experiments
git add experiments/
git commit -m "Add week's experiments"
git push
```

### Monthly Review
- Review experiments and add summary comments
- Update README with findings
- Clean up old sandbox backups
- Check for utility improvements

## Tips for Success

1. **Commit often** - Each successful experiment is worth saving
2. **Document findings** - Add comments explaining what you learned
3. **Use branches** - For larger experiments: `git checkout -b feature/new-experiment`
4. **Stay organized** - Move completed work out of sandbox regularly
5. **Iterate quickly** - Don't overthink, test ideas fast

## Getting Help

### With This Workspace
- Check `README.md` for structure
- Look at example experiment: `experiments/2025-11-17_string_concat_perf.py`
- Use templates as starting points

### With Claude Code
- Ask specific questions
- Reference files explicitly
- Request explanations for generated code
- Iterate on solutions

---

**Ready to start?** Try running the example experiment:
```bash
python experiments/2025-11-17_string_concat_perf.py
```
