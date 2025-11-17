# Claude Code Experimentation Workspace

A streamlined workspace for rapid prototyping and experimentation with Claude Code.

## 🎯 Using This Template

**Just created this from the template?** Run the setup script:
```bash
python3 setup.py
```
Then see [TEMPLATE_USAGE.md](TEMPLATE_USAGE.md) for complete instructions.

---

> **New to this workspace?** Check out [GETTING_STARTED.md](GETTING_STARTED.md) for setup instructions and Claude Code usage tips!

> **Portfolio Site**: View experiments online at the [GitHub Pages portfolio](https://kody-w.github.io/Nov17/)

## 📖 Purpose

This workspace is designed for quick iterations and testing ideas without the overhead of full project setup. Perfect for proof-of-concepts, algorithm testing, data exploration, and API experimentation.

## 📁 Structure

```
.
├── experiments/     # Completed experiments with documentation
├── sandbox/         # Temporary testing area (git-ignored)
├── utils/           # Reusable utilities and helpers
├── templates/       # Quick-start templates
├── docs/            # GitHub Pages portfolio site
└── .github/         # Workspace configuration
```

### Folder Details

- **`experiments/`**: Store your successful experiments here with clear documentation
- **`sandbox/`**: Temporary workspace for quick tests (automatically git-ignored)
- **`utils/`**: Common utilities like timers, loggers, and test helpers
- **`templates/`**: Pre-configured templates for common tasks
- **`docs/`**: GitHub Pages portfolio website showcasing experiments

## 🚀 Quick Start

### 1. Simple Python Script
```bash
cd sandbox
python -c "print('Hello, Claude Code!')"
```

### 2. Use a Template
```bash
cp templates/data_analysis.py experiments/2025-11-17_my_experiment.py
```

### 3. Time Your Code
```python
from utils.timer import timer, Timer

@timer
def my_function():
    # your code here
    pass
```

### 4. Quick Test
```bash
python utils/quick_test.py
```

## 📝 Naming Convention

For experiments, use descriptive filenames with dates:
- `YYYY-MM-DD_experiment_name.py`
- Example: `2025-11-17_api_performance_test.py`

## 🛠️ Available Utilities

| Utility | Purpose | Usage |
|---------|---------|-------|
| `quick_test.py` | Basic test template | `python utils/quick_test.py` |
| `timer.py` | Benchmark code performance | Import `@timer` decorator or `Timer` context manager |
| `logger.py` | Simple logging setup | Import `setup_logger()` function |

## 💡 Best Practices

1. **Keep it lightweight** - Install only what you need
2. **Document as you go** - Add comments explaining your thought process
3. **Clean up regularly** - Move successful experiments from sandbox to experiments/
4. **Use type hints** - Better IDE support and code clarity
5. **Test ideas fast** - Don't over-engineer, iterate quickly

## 🔧 Common Workflows

### Testing an Algorithm
1. Create file in sandbox: `sandbox/test_algorithm.py`
2. Import timer: `from utils.timer import timer`
3. Test and iterate
4. Move to experiments when complete

### Data Analysis
1. Copy template: `cp templates/data_analysis.py sandbox/analyze.py`
2. Add your data source
3. Run analysis
4. Document findings and move to experiments/

### API Testing
1. Copy template: `cp templates/api_client.py sandbox/test_api.py`
2. Configure endpoint
3. Test requests
4. Document results

## 📦 Dependencies

Keep dependencies minimal. Document any required packages:

```python
# Required: requests, pandas
# Install: pip install requests pandas
```

## 🧹 Cleanup

The `sandbox/` directory is git-ignored. Clean it regularly:
```bash
rm -rf sandbox/*
```

## 🌐 Portfolio Site

This workspace includes a GitHub Pages portfolio to showcase your experiments online.

### Quick Setup
1. Update `docs/index.html` with your GitHub username and repo name
2. Enable GitHub Pages in repository Settings → Pages
3. Deploy from `main` branch and `/docs` folder

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

### Adding Experiments
When you create a new experiment, add it to the portfolio by updating the `experiments` array in `docs/index.html`.

## 📚 Tips

- Use `sandbox/` for messy exploration
- Move polished code to `experiments/`
- Add dates to experiment files
- Keep experiments self-contained
- Comment liberally - your future self will thank you

---

**Happy experimenting!** 🚀
