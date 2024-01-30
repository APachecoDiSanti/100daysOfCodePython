from art import logo

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

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  should_continue = True
  
  while should_continue:
      for key in operations:
          print(key)
      operation_symbol = input("Pick an operation from above: ")
      operation = operations[operation_symbol]
  
      num2 = float(input("What's the second number?: "))
  
      answer = operation(num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
  
      should_continue = input(
          f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
      ) == "y"
      if (should_continue):
          num1 = answer
      else:
          calculator()

calculator()
