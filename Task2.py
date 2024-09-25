def main():
    print("Simple Calculator")

    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Choose operation
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operation = input("Enter the operation number (1-4): ")

    # Perform calculation
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} = {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation!")

if __name__ == "__main__":
    main()
