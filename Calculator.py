a = float(input("Enter First number: "))
b = float(input("Enter Second number: "))
operation = input("Choose an operation: ")
result = None
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    print("Unsupported operation!")
if result is not None:
    print("Your result:", result)
