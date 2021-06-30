import random
import string
numbers = [str(n) for n in range(0, 10)]
lower_letters = [l for l in string.ascii_lowercase]
upper_letters = [u for u in string.ascii_uppercase]
special_letters = [s for s in string.punctuation]
choice = ["n", "l", "u", "s"]
se = set(["(", ")", "[", "]", "{", "}"])
special_letters = set(special_letters)
special_letters = special_letters.difference(se)
special_letters = list(special_letters)
rand = list()
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
