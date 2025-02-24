# conditional expression = A one-line shortcut for the if-else statement (called ternary operator in other programming langauge)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y (return x if condition is True, else return Y)

# Example 1:
num = 5

print("Positive" if num > 0 else "Negative")

# Example 2:
num = 5

result = "EVEN" if num % 2 == 0 else "ODD" # assign EVEN if our number is divisible by 2 else return ODD

print(result)

# Example 3:
num = 5
a = 6
b = 7

max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

# Example 4:
age = 13

status = "Adult" if age >= 18 else "Child"

print(status)

# Example 5:
temperature = 20

weather = "HOT" if temperature > 20 else "COLD"

print(weather)

# Example 6:
user_role = "guest"

access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)
