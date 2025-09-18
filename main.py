from calculator.calculator import add, subtract, multiply, divide

def get_number(prompt):
    """Get a valid float number from the user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    """Get a valid operation from the user"""
    operations = {
        'add': 'add',
        '+': 'add',
        'subtract': 'subtract',
        '-': 'subtract',
        'multiply': 'multiply',
        '*': 'multiply',
        'divide': 'divide',
        '/': 'divide',
        'exit': 'exit'
    }
    while True:
        op = input("Choose operation (add, subtract, multiply, divide, +, -, *, /) or 'exit' to quit: ").lower()
        if op in operations:
            return operations[op]
        else:
            print("Invalid operation. Try again.")

def log_history(operation_name, num1, num2, result):
    """Log the calculation history to a file"""
    with open("calculation_history.txt", "a") as file:
        file.write(f"{operation_name}: {num1} and {num2} = {result}\n")

def main():
    print("Welcome to Terminal Calculator!")
    operation_names = {
        'add': 'Addition',
        'subtract': 'Subtraction',
        'multiply': 'Multiplication',
        'divide': 'Division'
    }
    while True:
        operation = get_operation()
        if operation == 'exit':
            print("Thank you for using the calculator. Goodbye!")
            break

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if operation == 'add':
                result = add(num1, num2)
                operation_name = operation_names['add']
            elif operation == 'subtract':
                result = subtract(num1, num2)
                operation_name = operation_names['subtract']
            elif operation == 'multiply':
                result = multiply(num1, num2)
                operation_name = operation_names['multiply']
            elif operation == 'divide':
                result = divide(num1, num2)
                operation_name = operation_names['divide']
            print(f"Result of {operation_name}: {result}")
            
            # Log the calculation to the history file
            log_history(operation_name, num1, num2, result)
        except ZeroDivisionError as e:
            print(e)

        print("-" * 40)

if __name__ == "__main__":
    main()