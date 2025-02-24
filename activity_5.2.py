# Python calculator
# Create a calculator using the if-else statement

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")

# print(num1 + num2)
# If the code only includes an input() without a float()/int(), it will result to a string concatenation
# The string concatenation will result to a combination of both inputs
# Example of string concatenation: 10 + 11 = 1011