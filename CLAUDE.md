# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a rapid experimentation workspace for prototyping and testing ideas without full project setup overhead. Perfect for proof-of-concepts, algorithm testing, data exploration, and API experimentation.

## Directory Structure

```
experiments/     # Completed experiments with documentation
sandbox/         # Temporary testing area (git-ignored)
utils/           # Reusable utilities (timer, logger, quick_test)
templates/       # Quick-start templates for common tasks
```

## Key Workflow Patterns

### Experiment Development Flow
1. Create files in `sandbox/` for initial testing and iteration
2. Test frequently with `python <file>.py`
3. Once successful, move to `experiments/` with date-prefixed filename: `YYYY-MM-DD_description.py`
4. The `sandbox/` directory is git-ignored and meant for messy exploration

### Naming Convention
- **Experiments**: `YYYY-MM-DD_experiment_name.py` (e.g., `2025-11-17_api_performance_test.py`)
- **Sandbox**: Any descriptive name works (temporary files)

## Available Utilities

### Timer (`utils/timer.py`)
Benchmark code performance with decorator or context manager:
```python
from utils.timer import timer, Timer

@timer
def my_function():
    pass

with Timer("operation name"):
    # code here
```

### Logger (`utils/logger.py`)
Simple logging with file and console output:
```python
from utils.logger import setup_logger

log = setup_logger("experiment_name")
log.info("message")
log.debug("debug details")
```

### Quick Test (`utils/quick_test.py`)
Basic test template to run with `python utils/quick_test.py`

## Templates

Located in `templates/` directory:
- `data_analysis.py` - Data analysis starting point
- `api_client.py` - API testing template
- `algorithm_test.py` - Algorithm comparison template

Copy templates to sandbox for customization: `cp templates/data_analysis.py sandbox/my_analysis.py`

## Development Principles

- **Keep it lightweight** - Minimal dependencies, document requirements in comments
- **Self-contained experiments** - Each experiment should be runnable independently
- **Iterate quickly** - Use sandbox for rapid testing, don't over-engineer
- **Document as you go** - Add comments explaining thought process and findings
- **Clean regularly** - Move successful work from sandbox to experiments, clean up temporary files

## Common Commands

```bash
# Run an experiment
python experiments/2025-11-17_experiment_name.py

# Test in sandbox
cd sandbox
python test_file.py

# Use a template
cp templates/algorithm_test.py sandbox/my_test.py

# Clean sandbox (it's git-ignored)
rm -rf sandbox/*
```

## Python Style

- Use type hints for clarity
- Document dependencies in file comments: `# Required: requests, pandas`
- Add docstrings for non-trivial functions
- Use the timer utility to benchmark performance-sensitive code
