# activity_3 based on practice_1-4

# Mad Libs game
# Word game where you create a story by filling in blanks with random words.

# The story:
# It was a _, cold November day.
# I woke to the _ smell of _ roasting in the _ downstairs.
# I _ down the stairs to see if I could help the dinner.
# My mom said, "See if _ needs a fresh _."
# So I carried a tray of glasses full of _ into the room.
# When I got there, I couldn't believe my _!
# There were _ _ on the _!

print("Welcome to Mad Libs Game!\n")
print("Fill in the blanks to create a story\n")

print("The Dinner\n")
print("It was a _____, cold November day.")
print("I woke up to the _____ smell of _____ roasting in the _____ downstairs.")
print("I _____ down the stairs to see if I could help _____ the dinner.")
print('My mom said, "See if _____ needs a fresh _____."')
print("So I carried a tray of glasses full of _____ into the _____ room.")
print("When I got there, I couldn't believe my _____!")
print("There were _____ _____ on the _____!\n")

print("Fill in the words. Type your answer:")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
bird_type = input("Enter a type of bird: ")
house = input("Enter a room in a house: ")
verb1 = input("Enter a verb (past-tense): ")
verb2 = input("Enter a verb: ")
relative = input("Enter a relative's name: ")
noun1 = input("Enter a noun: ")
liquid = input("Enter a type of liquid: ")
verb3 = input("Enter a verb (ending in -ing): ")
body = input("Enter a part of body: ")
noun2 = input("Enter a plural noun: ")
verb4 = input("Enter a verb (ending in -ing): ")
noun3 = input("Enter a noun: ")

print("\nThe Dinner\n")
print(f"It was a {adjective1}, cold November day.")
print(f"I woke up to the {adjective2} smell of {bird_type} roasting in the {house} downstairs.")
print(f"I {verb1} down the stairs to see if I could help {verb2} the dinner.")
print(f'My mom said, "See if {relative} needs a fresh {noun1}."')
print(f"So I carried a tray of glasses full of {liquid} into the {verb3} room.")
print(f"When I got there, I couldn't believe my {body}!")
print(f"There were {noun2} {verb4} on the {noun3}!\n")
print("The End.")