
word = "pog"
character = input("enter a character(e.g. \"t\") ").lower().strip()
count = 0

for letter in word:
    if letter == character:
        count += 1

print("the letter {} appears {} time(s) in the word".format(character, count))
