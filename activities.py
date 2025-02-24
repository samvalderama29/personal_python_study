# Activity 1: Create a program that ask the user to input 2 numbers. Print the bigger number.
print("Find the bigger number")
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

if a > b:
    print(f"{a} is the bigger number")
else:
    print(f"{b} is the bigger number")

# Activity 2: Create a program that ask the user to input 2 numbers. Print the lower number.
print("Find the lower number")
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

if a > b:
    print(f"{b} is the lower number")
else:
    print(f"{a} is the lower number")

# Activity 3: Create a program that ask the user to input 2 numbers. Print equal when the numbers are the same.
print("Find if the numbers are equal")
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

if a == b:
    print("Both numbers are equal")
else:
    print("The numbers are NOT equal")

# Activity 4: Create a program that ask the user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
print("Find if the numbers are not equal")
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

if a != b:
    print("The numbers are not equal")
else:
    print("The numbers are both equal")

# Activity 5: Create a program that ask the user to input 2 number. Print the sum of the two numbers.
print("Addition of 2 numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 + num2

print(f"The sum of {num1} + {num2} is {result}")






