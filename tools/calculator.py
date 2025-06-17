import re

def calculate(prompt):
    """
    Extract numbers and operation from prompt and perform calculation.
    Supports: add, subtract, multiply, divide
    """
    prompt = prompt.lower()
    numbers = list(map(float, re.findall(r'-?\d+\.?\d*', prompt)))

    if "add" in prompt or "sum" in prompt or "+" in prompt:
        result = sum(numbers)
    elif "subtract" in prompt or "minus" in prompt or "-" in prompt:
        result = numbers[0] - numbers[1]
    elif "multiply" in prompt or "times" in prompt or "*" in prompt:
        result = numbers[0] * numbers[1]
    elif "divide" in prompt or "/" in prompt:
        if numbers[1] == 0:
            return "Cannot divide by zero."
        result = numbers[0] / numbers[1]
    else:
        return "Unsupported operation. Try 'add', 'subtract', 'multiply', or 'divide'."

    return f"The result is: {result}"
