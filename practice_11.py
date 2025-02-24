# String Methods
# A string is a series of characters

# Example 1:
name = input("Enter your full name: ")

result = len(name)
# the len() functions give you the length of a string
# len() identifies how many characters is it, including spaces
# the len() function returns an integer

print(result)

# Example 2:
name = input("Enter your full name: ")

result = name.find("o")
# find() method will return the first occurence of a giving character, its position
# when working in indexes, it always begin in zero

print(result)

# Example 3:
name = input("Enter your full name: ")

result = name.rfind("q")
# the rfind() is used to return the last occurence of a giving character, r = reverse
# if python isn't giving a returning character it will return -1

print(result)

# Example 4:
name = input("Enter your full name: ")

name = name.capitalize()
# capitalize() will make the first character capitalize

print(name)

# Example 5:
name = input("Enter your full name: ")

name = name.upper()
# upper() will make all the characters in a string and make them all upper case

print(name)

# Example 6:
name = input("Enter your full name: ")

name = name.lower()
# lower() will make all the characters in a string and make them all lower case

print(name)

# Example 7:
name = input("Enter your full name: ")

result = name.isdigit()
# isdigit() method will return either True or False
# if the string contains all digits the result will be Boolean (True or False)

print(result)

# Example 8:
name = input("Enter your full name: ")

result = name.isalpha()
# isalpha() method will return either True or False
# if the string contains all alphabetical characters
# isalpha does not include the space

print(result)

# Example 9:
phone_number = input("Enter your phone #: ")

result = phone_number.count("-")
# count() method counts characters within a string

print(result)

# Example 10:
phone_number = input("Enter your phone #: ")

phone_number = phone_number.replace("-", " ")
# replace() any occurence with one character with another

print(phone_number)

# Example 11:
# print(help(str))
# This code is a comprehensive list of all the string methods available.