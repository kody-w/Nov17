"""
Data Analysis Template

Quick-start template for data analysis experiments.
Modify sections as needed for your specific use case.
"""
from typing import Any, Dict, List
from pathlib import Path
import json


def load_data(filepath: str) -> Any:
    """
    Load data from file.
    
    Supported formats: JSON, CSV (add more as needed)
    """
    path = Path(filepath)
    
    if path.suffix == '.json':
        with open(path, 'r') as f:
            return json.load(f)
    elif path.suffix == '.csv':
        # Uncomment if you install pandas
        # import pandas as pd
        # return pd.read_csv(path)
        raise NotImplementedError("CSV support requires pandas: pip install pandas")
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")


def analyze(data: Any) -> Dict[str, Any]:
    """
    Perform analysis on data.
    
    Replace this with your analysis logic.
    """
    results = {
        'summary': 'Analysis complete',
        'data_type': type(data).__name__,
        # Add your analysis results here
    }
    
    return results


def visualize(results: Dict[str, Any]) -> None:
    """
    Create visualizations.
    
    Use matplotlib, seaborn, or other viz libraries.
    """
    print("\n📊 Results:")
    print("-" * 40)
    for key, value in results.items():
        print(f"{key}: {value}")
    print("-" * 40)


def main():
    """Main analysis pipeline."""
    print("🔬 Starting Data Analysis")
    print("=" * 40)
    
    # 1. Load data
    # data = load_data('your_data_file.json')
    data = {'example': 'data'}  # Replace with actual data loading
    print(f"✅ Data loaded: {type(data).__name__}")
    
    # 2. Analyze
    results = analyze(data)
    print(f"✅ Analysis complete")
    
    # 3. Visualize
    visualize(results)
    
    print("\n✨ Done!")


if __name__ == "__main__":
    main()
