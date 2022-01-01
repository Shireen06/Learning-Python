MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resorce_sufficient(order_ingredients):
  """Returns true if enough resources"""
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"Sorry, not enough {item}.")
      return False
  return True

def process_coins():
  """Returns the total calculated"""
  print("Please insert coins")
  total = int(input("How many quaters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.1
  total += int(input("How many nickels?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total

def is_transaction_successful(money_received, drink_cost):
  """Returns true if enough money"""
  if money_received >= drink_cost:
    change = round(money_received - drink_cost, 2)
    print(f"Here is your change: ${change}")
    global profit
    profit += drink_cost
    return True
  else:
    print("Sorry, not enough money. Money refunded")
    return False

def make_coffee(drink_name, order_ingredients):
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Here is your {drink_name}.")

is_on = True

while is_on:
  order = input("What would you like: espresso, latte, cappucchino? \n")
  if order == "off":
    is_on = False
  elif order == "report":
    print(f"water: {resources['water']} ml")
    print(f"milk: {resources['milk']} ml")
    print(f"coffee: {resources['coffee']} g")
    print(f"money: ${profit}")
  else:
    drink = MENU[order]  
    if is_resorce_sufficient(drink["ingredients"]):
      payment = process_coins()
      if is_transaction_successful(payment, drink["cost"]):
          make_coffee(order, drink["ingredients"])






