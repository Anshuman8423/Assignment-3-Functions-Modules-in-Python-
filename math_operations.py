# math_operations.py

import math

def main():
    num = float(input("Enter a number: "))

    sqrt_value = math.sqrt(num)
    log_value = math.log(num)
    sine_value = math.sin(num)

    print(f"Square root of {num}: {sqrt_value}")
    print(f"Natural logarithm of {num}: {log_value}")
    print(f"Sine of {num} radians: {sine_value}")

if __name__ == "__main__":
    main()
