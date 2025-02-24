# Variable = A container for value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains
# String = Is a series of text or characters in which it can be in double quotes ("") or single quotes ('')
# Integer = Is a whole number, can use an arithmetic numbers
# Float = Float means floating points number, a number in which has a decimal point
# Boolean = A boolean is either True or False


# Example of String:

first_name = "Sam" # The "Bro" is a string and a value while the first_name is the variable
food = "Carbonara"
email = "samanthaangelevalderama@gmail.com"

print(f"Hello, I am {first_name}")
print(f"I like {food}")
print(f"My email is: {email}")

# The print format when using a variable shouldn't be in quotes as it can print exactly what is inside the print

# When displaying a variable you can also use an f-string. It is a formatted string literal in which you can
# write a Python expression between {} in which can be referred to variable or values.

# Example of Integer:
age = 19
quantity = 2
amount_of_students = 52

# Integers should not be in quotes as it will be called a string

print(f"I am {age} years old")
print(f"I love Hironos and SkullPanda so I bought {quantity} of them")
print(f"In our class, we are {amount_of_students} students")

# Example of Float:
price = 99.99
gpa = 1.25
distance = 5.5

print(f"The price of the book is ₱{price}")
print(f"My gpa is: {gpa}")
print(f"I ran {distance}km")

# Example of Boolean:
is_student = True
for_sale = True
is_online = False
# A boolean starts with capital letter
# A boolean is used internally, such as in working with if statements

print(f"Are you a student? {is_student}")

# Example of if-else
if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

if is_online:
    print("You are online")
else:
    print("Your are offline")

