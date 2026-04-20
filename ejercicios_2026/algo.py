sentence = "me gusta el futbol"

vowels = "aeiou"

count = 0

for letter in sentence:

    letter_lower = letter.lower()
    

    if letter_lower in vowels:
        count = count + 1

print("la frase tiene un numero de vocales de :", count)