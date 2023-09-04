# Prompt the user for their name.  Then, display their
# name along with a simulated throw of two dice.
import random

# Inputname
name = input("Enter your name: ")

# Throw two dice and add them
throw1 = random.randint(1, 6)
throw2 = random.randint(1, 6)
total = throw1 + throw2

# Output
print (name,"you threw a",total)
