#!/usr/bin/env python3
"""
A simple calculator application that performs basic arithmetic operations.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


def get_operator():
    """Get a valid operator from user input."""
    while True:
        operator = input("Choose an operator (+, -, *, /): ").strip()
        if operator in ['+', '-', '*', '/']:
            return operator
        print("Error: Please choose a valid operator (+, -, *, /).")


def main():
    """Main calculator function."""
    print("=== Python Calculator ===\n")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operator = get_operator()

    try:
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)

        print(f"\nResult: {num1} {operator} {num2} = {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
