def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            # Get input from user
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation: ")
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on operation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation!")
                continue
            
            # Display result
            print(f"Result: {result}")
            
            # Ask if user wants to continue
            again = input("Calculate again? (yes/no): ").lower()
            if again != 'yes':
                print("Thank you for using the calculator!")
                break
                
        except ValueError:
            print("Please enter valid numbers!")
            continue

# Run the calculator
if __name__ == "__main__":
    calculator()