num1_str = input("Enter the first number: ")
operator = input("Enter an operator (+, -, *, /): ")
num2_str = input("Enter the second number: ")

num1 = float(num1_str)
num2 = float(num2_str)

if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
        print("Error: Invalid operator entered. Please use +, -, *, or /.")