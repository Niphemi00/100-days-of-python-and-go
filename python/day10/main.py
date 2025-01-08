# day 10: CALCULATOR PROJECT

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

solved_value = 0
print("Welcome to this calcultor project!!")

first_number = float(input("What's your first number: "))
def calculator(first_number):
    """
    this accept a number and does basic arithmetic calculations!!
    """
    operation = input("Pick an operation ('+', '-', '/', '*'): ")
    next_number = float(input("What's your next number: "))
    if operation == "+":
        solved_value = add(first_number, next_number)
    elif operation == "-":
        solved_value = subtract(first_number, next_number)
    elif operation == "*":
        solved_value = multiply(first_number, next_number)
    elif operation == "/":
        solved_value = divide(first_number, next_number)
    else:
        print("Wrong operand")
    print(solved_value)
    wanna_continue = input(f"Type 'y' to continue calculating with {solved_value}, or type 'n' to start a new calculation or 'end' to quit: ").lower()
    cont = True
    while cont:
        if wanna_continue == 'y':
            calculator(solved_value)
        elif wanna_continue == 'end':
            cont = False
        else:
            print("New Calculation")
            first_number = float(input("What's your first number: "))
            calculator(first_number)

calculator(first_number)
