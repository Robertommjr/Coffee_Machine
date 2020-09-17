entry = input()
numbers = []

while entry != ".":
    numbers.append(float(entry))
    entry = input()

print(min(numbers))
