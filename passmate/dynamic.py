
#A Random Password Generator v0.1
#Functionalities present:
#   User can set the length of password in command line argument
#   User can get help on the usage of command line arguments
#   User can recieve a password with a random sequence of alphabet,numbers and symbols
#Functionalities to add:
#   Add command line arguments to include and exclude
#   certain characters from the password
#   for example: -n to include only numbers
#   and -nas to include all types of characters

import random
import string
import argparse


# initialize argparse for command-line arguments processing
parser = argparse.ArgumentParser(description="A random password generator")
parser.add_argument("-l", "--length", type=int, metavar="", help="length",default=10)
args = parser.parse_args()
# initialize numbers list
numbers = [str(n) for n in range(0, 10)]
# initialize lower_case_letters list
lower_letters = [l for l in string.ascii_lowercase]
# initialize upper_case_letters list
upper_letters = [u for u in string.ascii_uppercase]
# initialize symbols list
special_letters = [s for s in string.punctuation]
choice = ["n", "l", "u", "s"]
sequence=[]



# while length of the password doesnt become the length of the 
#command line argument for length,
# keep on adding random elements from the randomly chosen list
while len(sequence) < args.length:
    outcome = random.choice(choice)
    if outcome == "n":
        sequence.append(random.choice(numbers))

    if outcome == "l":
        sequence.append(random.choice(lower_letters))

    if outcome == "u":
        sequence.append(random.choice(upper_letters))

    if outcome == "s":
        sequence.append(random.choice(special_letters))


print("Your random password is: ")
print("".join(sequence))
