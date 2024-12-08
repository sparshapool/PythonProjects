logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def add(n1, n2):
  return n1 + n2


def sub(n1, n2):
  return n1 - n2


def mul(n1, n2):
  return n1 * n2


def div(n1, n2):
  return n1 / n2


def calculator():
  operations = {"+": add, "-": sub, "*": mul, "/": div}
  num1 = float(input("Enter the first number: "))
  choice = False
  while (not choice):
    num2 = float(input("Enter the second number: "))
    for symbol in operations:
      print(symbol)

    op = input("Which operation would you like to perform? ")
    function = operations[op]
    result = function(num1, num2)
    print(f"{num1} {op} {num2} = {result}")
    choice = input(
        "Do you want to continue with the calculation or start a fresh one? Type y or n respectively: "
    )
    if (choice == "y"):
      num1 = result
      choice = False
    elif (choice == "n"):
      choice = True
      calculator()
    else:
      print("Invalid!")
      print("You have exited the program")


calculator()
