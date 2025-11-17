"""
Algorithm Testing Template

Template for testing and benchmarking algorithms.
"""
from typing import List, Callable, Any
from utils.timer import timer, Timer
import random


# Example algorithms to compare
def approach_1(data: List[int]) -> int:
    """
    First approach - replace with your algorithm.
    """
    return sum(data)


def approach_2(data: List[int]) -> int:
    """
    Second approach - replace with your algorithm.
    """
    result = 0
    for item in data:
        result += item
    return result


def generate_test_data(size: int = 1000) -> List[int]:
    """
    Generate test data for benchmarking.
    
    Modify this to match your use case.
    """
    return [random.randint(1, 100) for _ in range(size)]


def run_benchmark(
    func: Callable,
    test_data: Any,
    iterations: int = 100
) -> None:
    """
    Run benchmark for a function.
    
    Args:
        func: Function to benchmark
        test_data: Input data
        iterations: Number of runs
    """
    print(f"\n🔬 Testing: {func.__name__}")
    
    with Timer(f"{func.__name__} ({iterations} iterations)"):
        for _ in range(iterations):
            result = func(test_data)
    
    print(f"   Result: {result}")


def verify_correctness(
    functions: List[Callable],
    test_cases: List[tuple]
) -> None:
    """
    Verify all functions produce correct results.
    
    Args:
        functions: List of functions to test
        test_cases: List of (input, expected_output) tuples
    """
    print("\n✅ Correctness Verification")
    print("-" * 40)
    
    for func in functions:
        all_passed = True
        for i, (input_data, expected) in enumerate(test_cases, 1):
            result = func(input_data)
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} {func.__name__} - Test {i}: {passed}")
        
        print(f"  {func.__name__}: {'PASS' if all_passed else 'FAIL'}")


def main():
    """Main execution."""
    print("🧪 Algorithm Testing & Benchmarking")
    print("=" * 50)
    
    # 1. Generate test data
    test_data = generate_test_data(size=10000)
    print(f"📊 Test data size: {len(test_data)} items")
    
    # 2. Verify correctness
    functions = [approach_1, approach_2]
    test_cases = [
        ([1, 2, 3], 6),
        ([10, 20, 30], 60),
        ([], 0),
    ]
    verify_correctness(functions, test_cases)
    
    # 3. Benchmark performance
    print("\n⏱️  Performance Benchmark")
    print("-" * 40)
    for func in functions:
        run_benchmark(func, test_data, iterations=1000)
    
    print("\n" + "=" * 50)
    print("✨ Complete!")


if __name__ == "__main__":
    main()
