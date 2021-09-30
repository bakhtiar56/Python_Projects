import random
import string
#this program asks user the length of the password
#and whether to include brackets in the random generated password.
#this is a hardcoded approach but I can easily transform it into dynamic by user input
#and user can then select which characters type to include/exclude in the password
numbers = [str(n) for n in range(0, 10)]#initialize numbers list
lower_letters = [l for l in string.ascii_lowercase]
upper_letters = [u for u in string.ascii_uppercase]
special_letters = [s for s in string.punctuation]
choice = ["n", "l", "u", "s"]
se = set(["(", ")", "[", "]", "{", "}"])
#using set structure to exlude the user excluded characters from the 
#total list of characters which are to be included in the password'''
special_letters = set(special_letters)
special_letters = special_letters.difference(se)
special_letters = list(special_letters)
rand = list()
#while length of the password doesnt become 8
#keep on adding random elements from the final list
while len(rand) < 9:
    outcome = random.choice(choice)
    if outcome == "n":
        rand.append(random.choice(numbers))

    if outcome == "l":
        rand.append(random.choice(lower_letters))

    if outcome == "u":
        rand.append(random.choice(upper_letters))

    if outcome == "s":
        rand.append(random.choice(special_letters))

print("Your random password is: ")
print("".join(rand))
