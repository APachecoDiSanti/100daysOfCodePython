def add(n1, n2):
    """Returns n1 + n2"""
    return n1 + n2


def subtract(n1, n2):
    """Returns n1 - n2"""
    return n1 - n2


def multiply(n1, n2):
    """Returns n1 * n2"""
    return n1 * n2


def divide(n1, n2):
    """Returns n1 / n2"""
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("What's the first number?: "))

for key in operations:
    print(key)
operation_symbol = input("Pick an operation from above: ")
operation = operations[operation_symbol]

num2 = int(input("What's the second number?: "))

answer = operation(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
