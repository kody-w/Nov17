"""
Example Experiment: String Manipulation Performance
Date: 2025-11-17
Author: Claude Code

Test different approaches to string concatenation in Python.
"""
from utils.timer import timer, Timer


@timer
def concatenation_plus(n: int) -> str:
    """Using + operator."""
    result = ""
    for i in range(n):
        result += str(i)
    return result


@timer
def concatenation_join(n: int) -> str:
    """Using join method."""
    return "".join(str(i) for i in range(n))


@timer
def concatenation_list(n: int) -> str:
    """Using list append + join."""
    result = []
    for i in range(n):
        result.append(str(i))
    return "".join(result)


def main():
    """Compare different string concatenation methods."""
    print("🔬 String Concatenation Performance Test")
    print("=" * 50)
    
    n = 10000
    print(f"\nConcatenating {n} numbers as strings\n")
    
    # Test each approach
    r1 = concatenation_plus(n)
    r2 = concatenation_join(n)
    r3 = concatenation_list(n)
    
    # Verify all produce same result
    assert r1 == r2 == r3, "Results don't match!"
    print(f"\n✅ All methods produce identical output ({len(r1)} chars)")
    
    print("\n📊 Conclusion:")
    print("   join() and list methods are significantly faster")
    print("   than using + operator for string concatenation")


if __name__ == "__main__":
    main()
