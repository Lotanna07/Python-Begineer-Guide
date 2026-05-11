#simple calculator

num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your 2nd number:"))
operator = input("Enter an operator(+, -, *, /):")

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")