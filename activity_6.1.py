# activity_6 based on practice_8

# Python weight converter
# Create a weight converter using the if-else statement

# Convert lb - kg, kg - lb (lb = pounds, kg = kilograms)
# Formula for conversion: lb = (kg)(2.205), kg = lb/2.205

print("Weight Converter")
print("a. pounds to kilograms (lb to kg)")
print("b. kilograms to pounds (kg to lb)")
choice = input("What would you like to convert: ")

if choice == "a":
    mass = float(input("Enter a mass value: "))
    kg = mass/2.205
    print(f"{mass}lb / 2.205 = {round(kg, 2)}kgs")
elif choice == "b":
    mass = float(input("Enter a mass value: "))
    lb = mass * 2.205
    print(f"{mass}kg * 2.205 = {round(lb, 2)}lbs")
else:
    print("Your choice is invalid. Please choose between a and b only.")





