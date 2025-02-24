# activity_4 based on practice_6 and practice_7

# Exercise 1 Calculate the circumference of a circle
# Formula of circumference of a circle: C = 2πr (r = radius)

import math

print("Circumference of a Circle")
radius = float(input("Enter the radius of a circle: "))
print(f"C = (2)({radius})(π)")
circumference_circle = 2 * radius * math.pi
print(f"The circumference of a circle is: {round(circumference_circle, 2)}cm")
# You can typecast/combine the input to insert the round or any arithmetic operation to the variable

# Exercise 2 Calculate the area of a circle
# Formula of area of a circle: A = πr^2

print("Area of a Circle")
radius_1 = float(input("Enter the radius of a circle: "))
print(f"A = (π)({radius_1})^2")
area_circle = math.pi * pow(radius_1, 2)
print(f"Area of a circle is: {round(area_circle, 2)}cm^2")

# Exercise 3 Calculate the hypotenuse of a right triangle
# Formula of hypotenuse of a right triangle: c = sqrt/a^2 + b^2

print("Hypotenuse of a Right Triangle")
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
print(f"c = sqrt/{a}^2 + {b}^2")
c =  math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The hypotenuse of the right triangle is: {round(c, 2)}cm")