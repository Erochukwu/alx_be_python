def safe_divide(numerator, denominator):
    try:
        x = int(input("Enter a number"))
        y = int(input("Enter a number"))
        try:
            result = x/y
            return f"Result: {result}
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only"
