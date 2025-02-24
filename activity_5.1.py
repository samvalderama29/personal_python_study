# activity_5 based on practice_8
# Create a calculator using the if-else statements

print("Calculator")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

table = input("Choose the following options: ")

if table == "1":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = a + b
    print(f"Result: {a} + {b} = {c}")
elif table == "2":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = a - b
    print(f"Result: {a} - {b} = {c}")
elif table == "3":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = a * b
    print(f"Result: {a} * {b} = {c}")
elif table == "4":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = a / b
    print(f"Result: {a} / {b} = {c}")
else:
    print("Invalid input. Please choose from 1-4 only.")
