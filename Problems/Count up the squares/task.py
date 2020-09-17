# put your python code here
numbers = []

while sum(numbers) != 0 or not numbers:
    numbers.append(int(input()))

print(sum(i * i for i in numbers))
