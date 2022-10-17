from art import logo
from replit import clear

def add(a, b):
  """This function adds 2 values"""
  return a + b

def subtract(a, b):
  "This function subtracts 2 values"
  return a - b

def multiply(a, b):
  """This function multiplies 2 values"""
  return a * b

def divide(a, b):
  """This function divides 2 values"""
  return a / b

def calculator():
  """This function acts as a calculator and does calculations with only 2 values simultaneously"""
  clear()
  print(logo)
  operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
  }
  num1 = float(input("Whats is the first number?: "))
  while True:
    num2 = float(input("What is the next number?: "))
    for symbol in operations:
      print(symbol)
    symbol_choice = input("Pick an operation from the above: ")
    calculation_function = operations[symbol_choice]
    answer = calculation_function(num1, num2)
    print(f"{num1} {symbol_choice} {num2} = {answer}")
    print(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. If you want to exit type 'e': ")
    wait = input().lower()
    if wait == 'e':
      clear()
      break
    elif wait == 'y':
      clear()
      num1 = answer
      continue
    elif wait == 'n':
      calculator()
      break

      
calculator()