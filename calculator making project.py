#####  Project1 #####

import math

def calculator():
    print("Welcome to High-Level Calculator!")
    print("Operations: +, -, *, /, ** (power), sqrt, sin, cos, tan, log, exit")

    while True:
        op = input("\nEnter operation: ")

        if op == 'exit':
            print("Exiting Calculator.")
            break

        if op in ['+', '-', '*', '/', '**']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if op == '+':
                    print("Result:", num1 + num2)
                elif op == '-':
                    print("Result:", num1 - num2)
                elif op == '*':
                    print("Result:", num1 * num2)
                elif op == '/':
                    print("Result:", num1 / num2)
                elif op == '**':
                    print("Result:", math.pow(num1, num2))
            except Exception as e:
                print("Error:", e)

        elif op in ['sqrt', 'sin', 'cos', 'tan', 'log']:
            try:
                num = float(input("Enter number: "))

                if op == 'sqrt':
                    print("Result:", math.sqrt(num))
                elif op == 'sin':
                    print("Result:", math.sin(math.radians(num)))
                elif op == 'cos':
                    print("Result:", math.cos(math.radians(num)))
                elif op == 'tan':
                    print("Result:", math.tan(math.radians(num)))
                elif op == 'log':
                    base = input("Enter base (leave blank for natural log): ")
                    if base == '':
                        print("Result:", math.log(num))
                    else:
                        print("Result:", math.log(num, float(base)))
            except Exception as e:
                print("Error:", e)

        else:
            print("Invalid operation. Try again.")

calculator()
