from calculator import *

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
        "5": ("Square Root", sqrt),
        "6": ("Sin", sin),
        "7": ("Cos", cos),
        "8": ("Tan", tan),
        "9": ("Cot", cot),
    }

    print("Select an operation:")
    for key, (name, _) in operations.items():
        print(f"{key}: {name}")

    choice = input("Enter choice (1-9): ")

    if choice in operations:
        operation_name, operation = operations[choice]

        if choice in ["5", "6", "7", "8", "9"]:
            num1 = get_number("Enter number: ")
            result = operation(num1)
        else:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            result = operation(num1, num2)
        
        print(f"The result of {operation_name} is: {result}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
