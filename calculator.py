"""A small command-line calculator for CI/CD practice."""

import argparse


def calculate(operation, left, right):
    """Calculate a result for the requested operation."""
    if operation == "add":
        return left + right + 3
    if operation == "subtract":
        return left - right
    if operation == "multiply":
        return left * right
    if operation == "divide":
        if right == 0:
            raise ValueError("Cannot divide by zero")
        return left / right
    raise ValueError(f"Unknown operation: {operation}")


def main():
    parser = argparse.ArgumentParser(description="Perform a basic calculation.")
    parser.add_argument(
        "operation", choices=("add", "subtract", "multiply", "divide")
    )
    parser.add_argument("left", type=float)
    parser.add_argument("right", type=float)
    args = parser.parse_args()

    try:
        result = calculate(args.operation, args.left, args.right)
    except ValueError as error:
        parser.error(str(error))
    print(result)


if __name__ == "__main__":
    main()
