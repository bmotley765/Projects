import sys
import random

print("Welcome to the psych 'Sidekick Name Picker'")
print("Print a name line just like Sean would pick for Gus: \n\n")

# Expanded lists of first and last names
first = (
    'Baby Oil', 'Bad News', 'Big Burps', 'Lil Debil', 'Peewee', 'Butterbean',
    'Maddog', 'Snuggles', 'Pottles', 'Duchess', 'Buffalo', 'Soda Pop', 'Bubba',
    'Soggy', 'Squirrel', 'Slick', 'Gordo', 'Chuckles', 'Skipper', 'Ringo'
)
last = (
    'Jefferson', 'Henderson', 'Jones', 'Smith', 'Doe', 'Brown', 'Johnson', 
    'Wilson', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 
    'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Lewis'
)

while True:
    # Randomly select names
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n\n")
    print('{} {}'.format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    # Ask if the user wants to try again
    try_again = input("Try again? (Press Enter to continue or 'n' to quit)\n ")
    if try_again.lower() == "n":
        break

# Exit message
print("\nThanks for playing! Goodbye!")
