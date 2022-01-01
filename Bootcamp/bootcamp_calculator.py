#from art import logo

def add(n1, n2):
  return n1 + n2

def subtruct(a1, a2):
  return a1 - a2

def multiply(b1, b2):
  return b1 * b2

def division(x1, x2):
  return x1/x2

operations = {
  "+" : add, 
  "-" : subtruct, 
  "*" : multiply, 
  "/" : division
  }
def calculator():
  #print(logo)

  num1 = float(input("What is the first number?: "))
  for s in operations:
    print(s)
  should_continue = True

  while should_continue:
    op_s = input("Pick an operation from the line above: ")
    num2 = float(input("What is the second number?: "))
    calculation = operations[op_s]
    answer = calculation(num1, num2)

    print(f"{num1} {op_s} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:" ) == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()      




