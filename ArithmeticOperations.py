def arithmetic_operations():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"\nAddition of {num1} and {num2}: {num1 + num2}")
    print(f"Subtraction of {num1} and {num2}: {num1 - num2}")
    print(f"Multiplication of {num1} and {num2}: {num1 * num2}")
    if num2 != 0:
        print(f"Division of {num1} by {num2}: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed!")

arithmetic_operations()
