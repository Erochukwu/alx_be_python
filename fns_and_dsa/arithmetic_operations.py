def perform_operation(num1, num2, operation):
    if operation not in ["add", "subtract", "multiply", "divide"]:
        return "Error: Invalid operation"
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 -num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 /num2
    if num2 ==   0:
        return "Error: Cannot divide by zero"
print(perform_operation (5, 8, "divide"))
    
    