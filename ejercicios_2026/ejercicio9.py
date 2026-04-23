sentence = "Learning Python is fun!"

vowels = "aeiou"
count = 0

for letter in sentence:
    letter_lower = letter.lower()

    if letter_lower in vowels:
        count = count + 1

print("número de vocales de :", count)
#corregir