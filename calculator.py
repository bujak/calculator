"""
Calculator 1.0
Tomasz Bujakowski, Codecool 2016
"""

# calculatig function

def calc (num1, num2):
    if operator == "+":
        result = num1 + num2
        print(num1, '+', num2, '=', result)
    elif operator == "-":
            result = num1 - num2
            print(num1, '-', num2, '=', result)
    elif operator == "*":
            result = num1 * num2
            print(num1, '*', num2, '=', result)
    elif operator == "/":
            result = num1 / num2
            print(num1, '/', num2, '=', result)
    elif operator == "^":
            result = num1 ** num2
            print(num1, '^', num2, '=', result)

counting = True

# main program

while counting:

    try:
        num1 = int(input("Enter a number (or a letter to exit)\n"))
    except ValueError:
        counting = False
        print("END")
        break

    print(str(num1) + " entered")

    operator = input("Enter an operation (+, - , *, /, ^):\n")
    while operator not in ["+", "-", "*", "/", "^"]:
        operator = input("Enter valid operator (+, - , *, /, ^):\n")

    while True:
        try:
            num2 = int(input("Enter second number\n"))
            break
        except ValueError:
            print("Invalid number, try again")

    print(str(num2) + " entered")

    calc(num1, num2)
