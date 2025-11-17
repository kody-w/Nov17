"""
Timer utility for benchmarking code performance.
"""
import time
from functools import wraps
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    Decorator to measure function execution time.
    
    Usage:
        @timer
        def my_function():
            # your code here
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️  {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


class Timer:
    """
    Context manager for timing code blocks.
    
    Usage:
        with Timer("my operation"):
            # your code here
    """
    def __init__(self, name: str = "Operation"):
        self.name = name
        self.start_time = None
        
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
        
    def __exit__(self, *args):
        elapsed = time.perf_counter() - self.start_time
        print(f"⏱️  {self.name} took {elapsed:.4f} seconds")


if __name__ == "__main__":
    # Example usage
    @timer
    def slow_function():
        time.sleep(0.1)
        return "Done"
    
    print(slow_function())
    
    with Timer("Code block"):
        time.sleep(0.05)
