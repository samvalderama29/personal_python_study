# activity_2 based on practice_4

# Exercise 1 Rectangle Area Calculator
# Let the user input a number to find the area of the rectangle
# Formula of a Rectangle: A = wl (l = length, w = width)

print("Rectangle Area Calculator")

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width

print(f"The area of the rectangle is: {area}cm^2")

# Can used a float or an integer
# {} - These brackets are called placeholder in f-string
# Superscript (for exponent) - NumLock + Alt + 0178

# Exercise 2 Shopping Cart Program
# 3 variable is needed: item, price, quantity

print("Welcome to Dali Shop!")
item =input("What item would you like to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many will you buy?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ₱{total}:")