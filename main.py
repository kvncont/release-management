def addition(num1, num2):
    return num1 - num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by 0"
    return division

# Example usage
num1 = 10
num2 = 10
print(f"Addition: {addition(num1, num2)}")
print(f"Subtraction: {subtraction(num1, num2)}")
print(f"Multiplication: {multiplication(num1, num2)}")
print(f"Division: {division(num1, num2)}")