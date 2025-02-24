# if statements
# if = Do some code only IF some condition is True
#      Else do something else
# Basic form of decision-making: True - we do something, False - we don't
# When a statement in if condition is false, the if condition is skipped and is continued by else

# Example 1:
# Prompt: A user wants to sign up for a credit card but in order to do so, age must be above 18
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!") # Any code under if statement should be indented
elif age < 0: # use when there is more than one condition
    print("You haven't been born yet!")
else: # else is used as a last resort
    print("You must be 18+ to signed up")

# Example 2:
response = input("Would you like food? (Y/N): ")

if response == "Y": # The == is a sign used to check if two values are equal
    print("Have some food!")
else:
    print("No food for you!")

# Example 3:
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}!")

# The use of boolean value of if statement
# Example 1:
for_sale = True # The for_sale is called a boolean variable

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

# Example 2:
online = False

if online:
    print("The user is on")
else:
    print("This user is offline")
