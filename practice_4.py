# input() = A function that prompts the used to enter data
#           Returns the entered data as a string
# Used to enable user to input from an answer from the given prompt

name = input("What is your name?: ")
age = int(input("How old are you?: ")) # When using integer you can enclosed it

# String cannot be used in arithmetic expressions, you need to typecast it
# age = int(age)

age = age + 1

# When using the input() and you want to use an integer or a float, convert it first as it is only a string

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old")

# The f-string can only be used if you want to insert a variable