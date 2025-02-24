# activity_8 based on practice_9-10

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

print("Username")
print("Read the following instructions to create a user_name:")
print("Username is no more than 12 characters")
print("Username must not contain spaces")
print("Username must not contain digits")

user_name = input("Please enter a username: ")
user_12 = len(user_name)
user_space = user_name.rfind(" ")
user_digit = user_name.isdigit()

if user_12 >= 12 or user_space or user_digit:
    print("Invalid username. Please read the instructions again.")
else:
    print(f"Welcome, {user_name}!")
