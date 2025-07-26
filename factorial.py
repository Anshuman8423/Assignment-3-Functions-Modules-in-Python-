# factorial.py

def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample call
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is: {factorial(num)}")
