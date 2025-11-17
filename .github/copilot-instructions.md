# Claude Code Experimentation Workspace

This workspace is optimized for rapid prototyping and experimentation with Claude Code.

## Workspace Structure
- `experiments/` - Quick experiments and proof-of-concepts
- `sandbox/` - Temporary testing area (git-ignored)
- `utils/` - Reusable helper functions and utilities
- `templates/` - Common code templates for quick starts

## Development Guidelines
- Keep experiments self-contained and well-documented
- Use descriptive filenames with dates: `YYYY-MM-DD_experiment_name.py`
- Add comments explaining the purpose of each experiment
- Clean up sandbox/ regularly - it's temporary
- Move successful experiments to experiments/ with documentation

## Quick Start Patterns
- For Python: Use utils/quick_test.py as a template
- For data work: Check templates/data_analysis.py
- For API testing: Use templates/api_client.py

## Best Practices
- Install minimal dependencies - keep it lightweight
- Document any external dependencies in comments
- Use type hints for better code completion
- Test ideas quickly, iterate rapidly
