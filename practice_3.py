# Typecasting = It is the process of converting a variable from one data type to another
#               str(), int(), float(), bool()
# Typecasting be useful in handling user input

# Example:
name = "Samantha Angel E. Valderama"
age = 19
gpa = 1.25
is_student = True

# The type() is a function in which you can get the data of a variable
# It will identify what type is used
# The typecasting will convert a variable to another type

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
age += "1" # This means that age = age + 1
print(age)

# String and numbers behave differently
# Numbers can be used to express arithmetic functions
# Strings = only add a number beside the original number

name = bool(name) # This function can be used to identify is someone input their name or not
print(name) # If they skip the name with only "" it will result to False

