# activity_7.1 based on practice_8
# Temperature Conversion

# Formula:
# Celsius to Fahrenheit: (°C * 9/5) + 32 = °F
# Fahrenheit to Celsius: (°F - 32) * 5/9 = °C

print("Temperature Conversion")
print("What would you like to convert?")
print("a. Celsius to Fahrenheit")
print("b. Fahrenheit to Celsius")
choice = input("Type your choice (a/b): ")

if choice == "a":
    celsius = float(input("Enter a value: "))
    result_c = (celsius * 9/5) + 32
    print(f"({celsius}°C * 9/5) + 32 = {round(result_c, 2)}°F")
elif choice == "b":
    fahrenheit = float(input("Enter a value: "))
    result_f = (fahrenheit - 32) * 5/9
    print(f"({fahrenheit}°F - 32) * 5/9 = {round(result_f, 2)}°C")
else:
    print("Invalid choice. Please pick between a and b only.")


