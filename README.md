# Python Calculator

A simple, beginner-friendly Python calculator application that performs basic arithmetic operations.

## Features

- **Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), and Division (/)
- **Input Validation**: Validates numeric inputs and operator selection
- **Error Handling**: 
  - Prevents division by zero
  - Rejects non-numeric inputs with helpful error messages
  - Rejects unsupported operators
- **User-Friendly Interface**: Clear prompts and formatted output

## Requirements

- Python 3.6 or higher

## Usage

Run the calculator:

```bash
python3 calculator.py
```

### Example Session

```
=== Python Calculator ===

Enter the first number: 10
Enter the second number: 5
Choose an operator (+, -, *, /): +

Result: 10.0 + 5.0 = 15.0
```

## Operations

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | 10 + 5 = 15 |
| `-` | Subtraction | 10 - 5 = 5 |
| `*` | Multiplication | 10 * 5 = 50 |
| `/` | Division | 10 / 5 = 2 |

## Error Handling

The calculator handles the following error cases:

1. **Non-numeric input**: Prompts user to enter a valid number
2. **Division by zero**: Displays error message and prevents calculation
3. **Invalid operator**: Prompts user to choose from supported operators

## Code Structure

- `add(a, b)` - Adds two numbers
- `subtract(a, b)` - Subtracts two numbers
- `multiply(a, b)` - Multiplies two numbers
- `divide(a, b)` - Divides two numbers with zero-check
- `get_number(prompt)` - Validates and retrieves numeric input
- `get_operator()` - Validates and retrieves operator selection
- `main()` - Main calculator function

## Implementation Notes

- Single-file implementation in `calculator.py`
- Uses functions for all operations and input validation
- Fully commented and beginner-friendly
- No external dependencies required

## License

Open source - feel free to use and modify as needed.
