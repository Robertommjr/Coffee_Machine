word = str(input())

for letter in word:
    if letter.isupper():
        word = word.replace(letter, "_" + str.lower(letter))

print(word)
